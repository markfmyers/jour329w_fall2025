import json
import subprocess
import time
import argparse
import sys
from pathlib import Path

def should_include_story(story):
    """Determine if a story should be included based on relevance criteria."""
    title = story.get('title', '').lower()
    content = story.get('content', '').lower()
    
    # Exclude stories that are not relevant to local sports beat
    exclude_keywords = [
        'obituary',  # Obituaries
        'wedding', 'engagement', 'anniversary',  # Social announcements
        'today in history',  # Historical features
        'public notice', 'legal notice',  # Legal notices
        'classified', 'advertisement',  # Ads
        'letter to the editor', 'opinion:',  # Opinion pieces
    ]
    
    # Check if story should be excluded
    for keyword in exclude_keywords:
        if keyword in title or (keyword in content[:200]):
            return False
    
    # If content is very short (less than 100 words), might be a brief/notice
    word_count = len(content.split())
    if word_count < 100:
        return False
    
    return True

def extract_entities(story_title, story_content, model, topic="Sports"):
    """Use LLM to extract named entities from a sports story."""
    prompt = f"""
Extract key named entities from this SPORTS news story and return them as JSON arrays.

This is for a LOCAL SPORTS BEAT BOOK - focus on entities a sports reporter would need to track regularly:

IMPORTANCE CRITERIA:
1. People - Extract ONLY key athletes, coaches, and officials:
   - Star players and team leaders (especially those quoted or making plays)
   - Head coaches and key assistant coaches
   - Athletic directors and team officials
   - SKIP: Minor player mentions, fans, parents, distant national figures

2. Places - Extract LOCAL teams and venues:
   - High schools and colleges/universities (as teams)
   - Stadiums, fields, gyms, specific venues
   - Cities/towns where games occur
   - SKIP: Generic locations like "field" or distant places

3. Organizations - Extract LOCAL sports organizations:
   - High school and college teams (use team names)
   - Leagues, conferences, divisions
   - Athletic departments and associations
   - SKIP: National organizations mentioned in passing, commercial sponsors

Example for a local high school sports story:
Story Title: "Easton High takes regional title"
Story Content: "Easton High School's basketball team defeated Cambridge-South Dorchester 65-58 Friday to win the Class 2A East Regional championship. Junior guard Marcus Thompson scored 24 points while coach Dave Miller earned his third regional title. The Warriors will face Wicomico High in the state semifinals at the University of Maryland."

Output:
{{
  "people": ["Marcus Thompson", "Dave Miller"],
  "places": ["Easton High School", "Cambridge-South Dorchester", "Wicomico High", "University of Maryland"],
  "organizations": ["Easton High School Warriors", "Class 2A East Regional"]
}}

Now extract entities from this sports story:

Story Title: {story_title}
Story Content: {story_content}

Return only valid JSON with three arrays: people, places, and organizations. Focus ONLY on entities a local sports reporter would need for their beat book. If no entities are found for a category, use an empty array.
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
    parser = argparse.ArgumentParser(description='Extract named entities from sports news stories')
    parser.add_argument('--model', required=True, help='LLM model to use')
    parser.add_argument('--input', default='topic_stories.json', help='Input JSON file with stories')
    parser.add_argument('--limit', type=int, help='Process only first N stories (for testing)')
    parser.add_argument('--version', default='v1', help='Output version suffix (e.g., v1, v2)')
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
        
        entities = extract_entities(story['title'], story['content'], args.model, topic="Sports")
        
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
        output_file = 'stories_with_entities_test_sports.json'
    else:
        output_file = f'stories_with_entities_{args.version}.json'
    
    with open(output_file, 'w') as f:
        json.dump(enhanced_stories, f, indent=2)

    print(f"\nProcessed {len(enhanced_stories)} stories with entities")
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    main()
