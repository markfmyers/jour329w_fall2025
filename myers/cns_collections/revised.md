**Revised Prompt**
import json
import subprocess
import time
import argparse
import sys
from pathlib import Path

def extract_metadata(story_title, story_content, schema_prompt, model):
    """Use LLM to extract structured metadata from story title and summary."""
    prompt = f"""
Extract metadata from this news story in JSON format using only the title and summary provided.

Schema to follow:
{schema_prompt}

Story Title: {story_title}
Story Summary: {story_content}

Return only valid JSON with the metadata. If information is not available, use an empty array:
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
    parser = argparse.ArgumentParser(description='Add metadata to CNS beat stories using LLM')
    parser.add_argument('--model', required=True, help='LLM model to use (e.g., gpt-4o-mini, claude-3.5-haiku)')
    parser.add_argument('--input', default='story_summaries_elections.json', help='Input JSON file with stories')
    
    # Show help if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    args = parser.parse_args()
    
    # Load your beat stories
    try:
        with open(args.input) as f:
            stories = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find input file '{args.input}'")
        print("Make sure to update the --input parameter to match your topic file!")
        return

    # Define your schema prompt based on your beat - CUSTOMIZE THIS!
    schema_prompt = """
    {
    "people": {
        "elected_officials": ["Wes Moore", "Brandon Scott"],
        "community_leaders": [],
        "other_newsmakers": [] 
    },
    "geographic_focus": "Baltimore City",
    "key_institutions": {
        "government": ["Baltimore City Council"],
        "military": ["U.S. Army Corps of Engineers"], 
        "nonprofits": ["Su Casa Furniture"],
        "businesses": ["&Pizza"],
        "education": ["Johns Hopkins University"],
        "healthcare": ["Lifebridge Health Center"]
  },      "beat_specific_field": ["government", "business"],
      "issue_type": ["gun violence", "drugs", "infrastructure"],
      "equity_angle": ["racial inequality", "economic inequality", "environmental justice"],
      "data_elements": ["contains statistics", "public records", "visualized data"]
    }
    """

    # Process each story
    enhanced_stories = []
    for i, story in enumerate(stories):
        print(f"Processing {i+1}/{len(stories)}: {story['title']}")
        
        metadata = extract_metadata(story['title'], story['content'], schema_prompt, args.model)
    # Process each story
    enhanced_stories = []
    for i, story in enumerate(stories):
        print(f"Processing {i+1}/{len(stories)}: {story['title']}")
        
        metadata = extract_metadata(story['title'], story['summary'], schema_prompt, args.model)
        
        # Add metadata fields as separate columns instead of nested object
        enhanced_story = story.copy()
        
        # If metadata extraction was successful, add each field separately
        if 'error' not in metadata:
            # Add each metadata field as a top-level column
            for key, value in metadata.items():
                # Convert arrays to JSON strings for storage
                if isinstance(value, list):
                    enhanced_story[f'metadata_{key}'] = json.dumps(value)
                else:
                    enhanced_story[f'metadata_{key}'] = value
        else:
            # If there was an error, add error information
            enhanced_story['metadata_error'] = metadata.get('error', 'Unknown error')
            
        enhanced_stories.append(enhanced_story)
        
        # Be respectful to the API
        time.sleep(1)

    # Save the enhanced collection
    with open('enhanced_beat_stories.json', 'w') as f:
        json.dump(enhanced_stories, f, indent=2)

    print(f"Processed {len(enhanced_stories)} stories with metadata")

if __name__ == "__main__":
    main()

**End of Prompt**

Looking at the stories about Baltimore, I can see several key themes and community dynamics:

## Major Challenges Facing Baltimore:

**Crime and Violence**
- The city struggles with persistent gun violence, despite recent reductions in homicides
- Programs like Safe Streets work to interrupt violence cycles but face funding threats
- Juvenile crime remains high even as overall crime decreases
- The trauma from violence deeply affects communities, especially youth

**Infrastructure and Urban Decay**
- The Francis Scott Key Bridge collapse in 2024 severely disrupted the port economy and transportation
- Many neighborhoods have high vacancy rates (14% in Mondawmin, nearly 20% in Midway)
- Aging sewer systems cause sewage backups in homes, with few residents receiving reimbursement
- The city struggles with abandoned properties that contribute to crime

**Economic Inequality**
- Deep disparities exist between neighborhoods (Bolton Hill vs. Mondawmin)
- Many residents face food insecurity, worsened by COVID-19
- The property tax sale system threatens low-income homeowners
- Small businesses struggle but show resilience through strong community connections

## Community Responses and Resilience:

**Grassroots Leadership**
- Faith-based organizations fill gaps left by city services, providing food and support
- Barbershops serve as unofficial mental health and wellness centers
- Community activists like Wesley Hawkins mentor at-risk youth
- Residents create informal support networks to help each other survive

**Political Engagement**
- Mayor Brandon Scott won reelection in 2024 with increased support
- The Elijah Cummings Healing City Act mandates trauma training for city employees
- Squeegee workers remain a contentious issue requiring policy solutions
- Community members actively advocate for change at City Hall

**Economic Innovation**
- Small businesses survive through deep community connections ("Smalltimore")
- The gig economy provides alternative income (meal-sharing, personal chefs)
- Major investments in areas like Mondawmin show promise but face skepticism
- The Port of Baltimore's recovery from the bridge collapse demonstrated resilience

## Persistent Themes:

1. **Trauma as a Central Issue**: Many stories highlight how violence and poverty create intergenerational trauma that shapes daily life

2. **Community Over Systems**: Residents often rely more on each other and local organizations than official city services

3. **Historical Legacy**: Redlining and systematic discrimination continue to shape neighborhood outcomes decades later

4. **Youth at Risk**: Children face particular challenges from violence, poor schools, and lack of opportunities

5. **Hope Despite Hardship**: Even in the most challenging circumstances, residents show remarkable resilience and determination to improve their communities

The overall picture is of a city where official systems often fail to meet residents' needs, but where strong community bonds and grassroots efforts provide crucial support. While major challenges persist, there are also signs of positive change through both community action and some policy reforms.
