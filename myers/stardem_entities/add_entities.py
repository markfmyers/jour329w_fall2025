import json
import subprocess
import time
import argparse
import sys
from pathlib import Path

def extract_entities(story_title, story_content, model):
    """Use LLM to extract named entities from story title and content."""
    prompt = f"""
Extract named entities from this news story and return them as JSON arrays.

Extract three types of entities:
1. People - Names of individuals mentioned (e.g., politicians, officials, residents, athletes)
2. Places - Geographic locations (e.g., cities, counties, states, neighborhoods, buildings)
3. Organizations - Companies, government agencies, schools, nonprofits, businesses

Example:
Story Title: "Mayor Cook announces new park funding at Town Council meeting"
Story Content: "Easton Mayor Megan Cook announced Tuesday that the Town Council approved $2 million for improvements to Idlewild Park. The funding came from a partnership with the Maryland Department of Natural Resources."

Output:
{{
  "people": ["Megan Cook"],
  "places": ["Easton", "Idlewild Park", "Maryland"],
  "organizations": ["Town Council", "Maryland Department of Natural Resources"]
}}

Now extract entities from this story:

Story Title: {story_title}
Story Content: {story_content}

Return only valid JSON with three arrays: people, places, and organizations. If no entities are found for a category, use an empty array.
"""
    
    try:
        result = subprocess.run([
            'llm', '-m', model, prompt
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            # Parse and validate the JSON response
            response_text = result.stdout.strip()
            # Remove any markdown code blocks if present
            if response_text.startswith('```'):
                response_text = response_text.split('\n', 1)[1]
                response_text = response_text.rsplit('\n', 1)[0]
            
            metadata = json.loads(response_text)
            return metadata
        else:
            return {"error": "LLM failed", "stderr": result.stderr}
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description='Extract named entities from news stories using LLM')
    parser.add_argument('--model', required=True, help='LLM model to use (e.g., gpt-4o-mini, claude-3.5-haiku)')
    parser.add_argument('--input', default='../stardem_topics/stardem_topics_classified2.json', help='Input JSON file with stories')
    
    # Show help if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    args = parser.parse_args()
    
    # Load stories
    try:
        with open(args.input) as f:
            stories = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find input file '{args.input}'")
        return

    # Process each story
    enhanced_stories = []
    for i, story in enumerate(stories):
        print(f"Processing {i+1}/{len(stories)}: {story['title']}")
        
        entities = extract_entities(story['title'], story['content'], args.model)
        
        # Add entities to story
        enhanced_story = story.copy()
        
        # If entity extraction was successful, add the arrays
        if 'error' not in entities:
            enhanced_story['people'] = entities.get('people', [])
            enhanced_story['places'] = entities.get('places', [])
            enhanced_story['organizations'] = entities.get('organizations', [])
        else:
            # If there was an error, add empty arrays and error info
            enhanced_story['people'] = []
            enhanced_story['places'] = []
            enhanced_story['organizations'] = []
            enhanced_story['entity_error'] = entities.get('error', 'Unknown error')
            
        enhanced_stories.append(enhanced_story)
        
        # Be respectful to the API
        time.sleep(1)

    # Save the enhanced collection
    with open('stories_with_entities.json', 'w') as f:
        json.dump(enhanced_stories, f, indent=2)

    print(f"Processed {len(enhanced_stories)} stories with entities")

if __name__ == "__main__":
    main()
