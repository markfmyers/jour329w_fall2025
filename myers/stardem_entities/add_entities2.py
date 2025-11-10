import json
import subprocess
import time
import argparse
import sys
from pathlib import Path

def extract_entities(story_title, story_content, model):
    """Use LLM to extract the most important named entities from story title and content."""
    prompt = f"""
Extract the MOST IMPORTANT named entities from this news story. Focus on key figures, main locations, and primary organizations.

Extract only:
1. People - Key individuals central to the story (officials, main subjects, spokespersons). Skip minor mentions.
2. Places - Primary geographic locations (cities, counties, specific venues). Skip generic or minor locations.
3. Organizations - Main organizations driving the story (government agencies, businesses, institutions). Skip casual mentions.

Example:
Story Title: "Easton Mayor Cook announces new park funding"
Story Content: "Easton Mayor Megan Cook announced Tuesday that the Town Council approved $2 million for Idlewild Park improvements through a partnership with Maryland DNR."

Output:
{{
  "people": ["Megan Cook"],
  "places": ["Easton", "Idlewild Park"],
  "organizations": ["Easton Town Council", "Maryland Department of Natural Resources"]
}}

Story Title: {story_title}
Story Content: {story_content}

Return only JSON with three arrays: people, places, organizations. Use empty arrays if none found.
"""
    
    try:
        result = subprocess.run(['llm', '-m', model, prompt], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            response_text = result.stdout.strip()
            # Remove markdown code blocks if present
            if response_text.startswith('```'):
                response_text = response_text.split('\n', 1)[1].rsplit('\n', 1)[0]
            return json.loads(response_text)
        else:
            return {"error": f"LLM failed: {result.stderr}"}
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description='Extract key named entities from news stories')
    parser.add_argument('--model', default='groq/openai/gpt-oss-20b', help='Groq model to use')
    parser.add_argument('--input', default='../stardem_topics/stardem_sample.json', help='Input JSON file')
    args = parser.parse_args()
    
    # Load stories
    try:
        with open(args.input) as f:
            stories = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{args.input}' not found")
        return

    # Process stories
    enhanced_stories = []
    for i, story in enumerate(stories, 1):
        print(f"Processing {i}/{len(stories)}: {story['title']}")
        
        entities = extract_entities(story['title'], story['content'], args.model)
        
        enhanced_story = story.copy()
        if 'error' not in entities:
            enhanced_story.update({
                'people': entities.get('people', []),
                'places': entities.get('places', []),
                'organizations': entities.get('organizations', [])
            })
        else:
            enhanced_story.update({
                'people': [], 'places': [], 'organizations': [],
                'entity_error': entities['error']
            })
            
        enhanced_stories.append(enhanced_story)
        time.sleep(1)  # API rate limiting

    # Save results
    with open('stories_with_entities.json', 'w') as f:
        json.dump(enhanced_stories, f, indent=2)

    print(f"\nProcessed {len(enhanced_stories)} stories. Saved to stories_with_entities.json")

if __name__ == "__main__":
    main()
