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

This is for an EASTERN SHORE MARYLAND EDUCATION BEAT BOOK - focus on entities a reporter covering Talbot, Caroline, Dorchester, and Queen Anne's counties would need to track regularly. Statewide Maryland education issues are also relevant.

CRITICAL: Extract ONLY entities that are CENTRAL and VITAL to the story. If an entity is mentioned in passing or tangentially, DO NOT include it. Quality over quantity - a story may have only 1-2 key entities, or even none if it's just background/context.

ENTITY STANDARDIZATION RULES:
- People: Extract with professional/official title IF it directly precedes or follows their name in the text.
  For regional titles (superintendent, principal, board member), INCLUDE the organization/region:
  Examples: 
  * "Talbot County Public Schools Superintendent Dr. Maria Williams" → "Talbot County Superintendent Maria Williams"
  * "Easton Middle School Principal John Smith" → "Easton Middle School Principal John Smith"
  * "Board President Jennifer Martinez" → "Board President Jennifer Martinez"
  * "Caroline County Superintendent Sarah Johnson" → "Caroline County Superintendent Sarah Johnson"
  * "Maria Williams" (with no title nearby) → "Maria Williams"
  If person appears multiple ways, use the MOST INFORMATIVE form once (with title AND region/school if stated).
  Do NOT include: courtesy titles alone (Mr., Ms., Mrs., Dr. without role), generic descriptors ("parent", "resident")
- Organizations: Use official full names as they appear
- Places: Use complete official names

IMPORTANCE CRITERIA - ONLY EXTRACT IF CENTRAL TO THE STORY:

1. People - Extract ONLY if they are:
   - Making key decisions or taking significant actions in THIS story
   - Being quoted or featured as main subjects
   - Central newsmakers (not just mentioned in passing)
   
   YES - Include these if central to story:
   - School administrators making decisions or being featured
   - School board members voting, being appointed/resigned, or taking action
   - Teachers/staff who are main subjects (award recipients, spokespersons, those at center of story)
   
   NO - Skip these even if named:
   - People mentioned briefly in background context
   - National figures mentioned for context only
   - Students, parents, or community members mentioned in passing
   - Anyone who is not essential to understanding this specific story
   
   Each person should appear only ONCE using their most complete form (preferably with title if stated)

2. Places - Extract ONLY if they are:
   - The primary location where story events occur
   - Directly affected by or central to the story's main action
   
   YES - Include these if central to story:
   - Counties, towns where main events occur
   - Specific facilities directly involved in the story (buildings being renovated, sites of events)
   
   NO - Skip these even if named:
   - Individual schools (these are organizations, not places)
   - Locations mentioned for general context or background
   - Distant or tangential locations
   - Generic references (classroom, hallway, etc.)

3. Organizations - Extract ONLY if they are:
   - Taking action or being directly affected in THIS story
   - Central to the main narrative or decision-making
   
   YES - Include these if central to story:
   - School districts and individual schools that are main subjects
   - School boards when making decisions featured in the story
   - Organizations taking action or being directly impacted
   
   NO - Skip these even if named:
   - Organizations mentioned only for context or background
   - National organizations referenced tangentially
   - Vendors or commercial entities unless central to the story
   - Any organization not essential to this specific story

REMEMBER: It's better to extract TOO FEW entities than too many. Only include entities that someone would need to remember when following up on THIS specific story. Many stories may have only 1-3 total entities across all categories.

Example for an Eastern Shore education story:
Story Title: "Talbot County Schools approve new STEM program"
Story Content: "Talbot County Public Schools Superintendent Dr. Maria Williams announced Monday that the school board approved a new STEM program for middle schools. The program will launch at Easton Middle School and St. Michaels Middle School next fall. Board President Jennifer Martinez praised the initiative, which received $500,000 in state funding from the Maryland State Department of Education."

Output:
{{
  "people": ["Talbot County Superintendent Maria Williams", "Board President Jennifer Martinez"],
  "places": ["Easton", "St. Michaels"],
  "organizations": ["Talbot County Public Schools", "Easton Middle School", "St. Michaels Middle School", "Maryland State Department of Education"]
}}

Now extract entities from this education story:

Story Title: {story_title}
Story Content: {story_content}

Return only valid JSON with three arrays: people, places, and organizations. Remember: include professional titles with names when they appear together in text, schools are organizations not places, each entity should appear only once in its most complete form, and ONLY include entities that are truly central and vital to THIS story. If no entities are found for a category, use an empty array.
"""
    
    try:
        result = subprocess.run([
            'uv', 'run', 'llm', '-m', model, prompt
        ], capture_output=True, text=True, timeout=120)
        
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
    """Determine if a story should be included based on relevance criteria.
    
    INCLUDE examples (local education stories):
    - "Delean-Botkin resigns from Talbot Board of Education" - Local school board news
    - "Community invited to celebrate completion of KI Branch Library renovation" - Local facility
    - "Fair offers lots of fun, much more" - Caroline/Dorchester County Fair with 4-H education
    - "School district saves thousands in energy costs" - Caroline County Public Schools operations
    
    EXCLUDE examples (non-local education stories):
    - "Public TV plans shows on Black colleges" - National PBS programming topic
    - "Students paying less for college than 15 years ago" - National college cost trends/opinion
    - Stories mentioning Congress, federal policy, or out-of-state universities as primary focus
    
    INCLUDE examples (statewide but relevant):
    - "Contracted Out - Maryland public school spending" - Statewide investigation relevant to local districts
    """
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
    
    # Exclude stories mentioning states/locations outside Maryland
    # Check for out-of-state locations (common patterns in education news)
    out_of_state_indicators = [
        'virginia', 'va ', 'delaware', 'de ', 'pennsylvania', 'pa ',
        'washington, d.c.', 'washington d.c.', 'district of columbia',
        'new york', 'new jersey', 'california', 'texas', 'florida',
        'national', 'nationwide', 'across the country', 'united states',
        'u.s. department', 'federal government', 'congress',
        'white house', 'senate', 'house of representatives',
        # College/University indicators outside Maryland
        'harvard', 'yale', 'princeton', 'stanford', 'mit',
        'penn state', 'ohio state', 'duke university',
    ]
    
    # More flexible check - look for out-of-state indicators
    for indicator in out_of_state_indicators:
        if indicator in content:
            # But allow if Maryland is prominently featured
            maryland_mentions = content.count('maryland') + content.count('eastern shore') + \
                              content.count('talbot') + content.count('caroline') + \
                              content.count('dorchester') + content.count('queen anne')
            
            # If Maryland is mentioned less than the out-of-state location, skip it
            out_of_state_mentions = content.count(indicator)
            if maryland_mentions < out_of_state_mentions:
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
    parser.add_argument('--resume', action='store_true', help='Resume processing from where it left off')
    
    # Show help if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    args = parser.parse_args()
    
    # Determine output file name
    if args.version == 'test':
        output_file = 'stories_with_entities_test_education.json'
    else:
        output_file = f'stories_with_entities_{args.version}.json'
    
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
    
    # Check if resuming from previous run
    enhanced_stories = []
    processed_docrefs = {}
    
    if args.resume and Path(output_file).exists():
        print(f"Resuming from existing file: {output_file}")
        with open(output_file) as f:
            previous_results = json.load(f)
        
        # Build a map of successfully processed stories by docref
        for story in previous_results:
            docref = story.get('docref')
            if docref and 'entity_error' not in story:
                processed_docrefs[docref] = story
        
        successful_count = len(processed_docrefs)
        failed_count = len(previous_results) - successful_count
        print(f"Found {successful_count} successfully processed, {failed_count} failed")
        print(f"Will keep successful ones and retry failed stories")
    
    # Process each story
    for i, story in enumerate(stories):
        docref = story.get('docref')
        
        # Skip if already successfully processed - just add the previous result
        if args.resume and docref in processed_docrefs:
            enhanced_stories.append(processed_docrefs[docref])
            continue
        
        print(f"Processing {i+1}/{len(stories)}: {story['title'][:60]}")
        
        entities = extract_entities(story['title'], story['content'], args.model, topic="Education")
        
        # Add entities to story
        enhanced_story = story.copy()
        
        # If entity extraction was successful, add the arrays
        if 'error' not in entities:
            enhanced_story['people'] = entities.get('people', [])
            enhanced_story['places'] = entities.get('places', [])
            enhanced_story['organizations'] = entities.get('organizations', [])
            enhanced_story['entity_extraction_model'] = args.model
        else:
            # If there was an error, add empty arrays and error info
            enhanced_story['people'] = []
            enhanced_story['places'] = []
            enhanced_story['organizations'] = []
            enhanced_story['entity_error'] = entities.get('error', 'Unknown error')
            
        enhanced_stories.append(enhanced_story)
        
        # Write after each story is processed
        with open(output_file, 'w') as f:
            json.dump(enhanced_stories, f, indent=2)
        
        # Be respectful to the API
        time.sleep(1)

    print(f"\nProcessed {len(enhanced_stories)} stories with entities")
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    main()
