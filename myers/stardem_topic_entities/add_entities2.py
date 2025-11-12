import json
import subprocess
import time
import argparse
import sys
from pathlib import Path

def extract_entities(story_title, story_content, model, topic="Education"):
    """Use LLM to extract named entities from an education story."""
    prompt = f"""
Extract key named entities from this EDUCATION news story and return them as JSON arrays.

This is for a LOCAL EDUCATION BEAT BOOK - focus on entities a reporter would need to track regularly:

IMPORTANCE CRITERIA:
1. People - Extract ONLY key decision-makers and newsmakers:
   - School administrators (superintendents, principals, assistant principals)
   - School board members (voting members, especially those quoted or making decisions)
   - Teachers/staff if they're central to the story (award winners, union reps, spokespersons)
   - SKIP: General mentions of students without names, parents in passing, national figures

2. Places - Extract LOCAL institutions and specific locations:
   - Individual schools (high schools, middle schools, elementary schools)
   - School districts (county or city school systems)
   - Specific facilities (libraries, gyms, new buildings)
   - SKIP: Generic locations like "classroom" or distant places not central to local coverage

3. Organizations - Extract LOCAL education organizations and key partners:
   - School districts and individual schools (as organizations)
   - School boards and committees
   - Parent-teacher organizations (PTA/PTO)
   - Local education foundations, teacher associations
   - Key partners (county government, state education dept when involved in local decisions)
   - SKIP: National organizations mentioned in passing, commercial vendors

Example for a local education story:
Story Title: "Talbot County Schools approve new STEM program"
Story Content: "Talbot County Public Schools Superintendent Dr. Maria Williams announced Monday that the school board approved a new STEM program for middle schools. The program will launch at Easton Middle School and St. Michaels Middle School next fall. Board President Jennifer Martinez praised the initiative, which received $500,000 in state funding from the Maryland State Department of Education."

Output:
{{
  "people": ["Maria Williams", "Jennifer Martinez"],
  "places": ["Easton Middle School", "St. Michaels Middle School"],
  "organizations": ["Talbot County Public Schools", "Maryland State Department of Education"]
}}

Now extract entities from this education story:

Story Title: {story_title}
Story Content: {story_content}

Return only valid JSON with three arrays: people, places, and organizations. Focus ONLY on entities a local education reporter would need for their beat book. If no entities are found for a category, use an empty array.
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

def should_include_story(story):
    """Determine if a story should be included based on relevance criteria."""
    title = story.get('title', '').lower()
    content = story.get('content', '').lower()
    
    # Exclude stories that are not relevant to local education beat
    exclude_keywords = [
        'obituar',  # Obituaries
        'wedding', 'engagement', 'anniversary',  # Social announcements
        'today in history',  # Historical features
        'public notice', 'legal notice',  # Legal notices
        'classified', 'advertisement',  # Ads
        'letter to the editor', 'opinion:',  # Opinion pieces (unless about education policy)
    ]
    
    # Check if story should be excluded
    for keyword in exclude_keywords:
        if keyword in title or (keyword in content[:200]):  # Check title and first 200 chars
            return False
    
    # If content is very short (less than 100 words), might be a brief/notice
    word_count = len(content.split())
    if word_count < 100:
        return False
    
    return True

def main():
    parser = argparse.ArgumentParser(description='Extract named entities from education news stories')
    parser.add_argument('--model', required=True, help='LLM model to use')
    parser.add_argument('--input', default='topic_stories.json', help='Input JSON file with stories')
    parser.add_argument('--limit', type=int, help='Process only first N stories (for testing)')
    parser.add_argument('--version', default='v2', help='Output version suffix (e.g., v1, v2)')
    parser.add_argument('--skip-filter', action='store_true', help='Skip the relevance filter and process all stories')
    
    # Show help if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    args = parser.parse_args()
    
    # Load stories
    try:
        with open(args.input) as f:
            all_stories = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find input file '{args.input}'")
        return

    # Filter stories for relevance unless skip-filter is specified
    if args.skip_filter:
        stories = all_stories
        print("Processing all stories (filter disabled)")
    else:
        stories = [s for s in all_stories if should_include_story(s)]
        excluded_count = len(all_stories) - len(stories)
        print(f"Filtered stories: {len(stories)} relevant, {excluded_count} excluded")
    
    # Apply limit if specified
    if args.limit:
        stories = stories[:args.limit]
        print(f"Processing first {args.limit} stories (testing mode)")
    
    # Process each story
    enhanced_stories = []
    for i, story in enumerate(stories):
        print(f"Processing {i+1}/{len(stories)}: {story['title'][:60]}")
        
        entities = extract_entities(story['title'], story['content'], args.model, topic="Education")
        
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

    # Save the enhanced collection with version suffix
    if args.version == 'test':
        output_file = 'stories_with_entities_test_education.json'
    else:
        output_file = f'stories_with_entities_{args.version}.json'
    
    with open(output_file, 'w') as f:
        json.dump(enhanced_stories, f, indent=2)

    print(f"\nProcessed {len(enhanced_stories)} stories with entities")
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    main()
