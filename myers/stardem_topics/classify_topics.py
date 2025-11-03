import json
import subprocess
from pathlib import Path

# Configuration
INPUT_FILE = "stardem_sample.json"
OUTPUT_FILE = "stardem_topics_classified2.json"
MODEL = "groq/meta-llama/llama-4-scout-17b-16e-instruct"

def classify_story(story):
    """Use LLM to classify a single story into a topic."""
    prompt = f"""
Analyze this news story and assign it a BROAD topic category.

CRITICAL INSTRUCTIONS:
1. Use ONLY broad, general topic names (1-2 words maximum)
2. Avoid overly specific or narrow topics
3. Choose from common news categories when possible

PREFERRED BROAD TOPICS (use these whenever applicable):
- Sports (all sports stories, specific sports, athletes, games)
- Politics (elections, candidates, government policy, inaugurations, political events)
- Government (local/state operations, budgets, regulations, public meetings)
- Crime (arrests, investigations, court cases, law enforcement)
- Education (schools, teachers, students, academics, school events)
- Business (economy, companies, real estate, jobs, development)
- Health (medical, hospitals, wellness, public health, disease)
- Environment (conservation, climate, pollution, nature)
- Arts (museums, galleries, exhibitions, artists, cultural events)
- Entertainment (movies, TV, music, concerts, performances, books, authors)
- Community (local events, festivals, celebrations, neighborhoods)
- Transportation (roads, traffic, infrastructure, transit)
- Weather (storms, forecasts, seasonal)
- Religion (churches, faith, worship)
- Military (veterans, armed forces, defense)
- Technology (digital, internet, cybersecurity)
- Agriculture (farming, crops, livestock)

AVOID narrow topics like:
- "Inauguration Gifts" → use "Politics"
- "Adventurous Travel" → use "Travel" or "Entertainment"
- "Books Authors" → use "Entertainment"
- "Women's Basketball" → use "Sports"
- "Field Hockey" → use "Sports"
- "Food Competition" → use "Community" or "Entertainment"
- "Museum Artifact" → use "Arts"
- "Phone Scams" → use "Crime"

Title: {story['title']}
Content: {story['content']}

Return ONLY the broad topic name (1-2 words). Be consistent - use the same broad category for similar stories.
"""
    
    # Call the llm command-line tool
    result = subprocess.run(
        ["uv", "run", "llm", "-m", MODEL],
        input=prompt,
        text=True,
        capture_output=True
    )
    
    if result.returncode != 0:
        print(f"Error classifying story: {result.stderr}")
        return "Error"
    
    # Extract topic from response (strip whitespace and quotes)
    topic = result.stdout.strip().strip('"').strip("'")
    return topic

def main():
    # Load the input data
    print(f"Loading stories from {INPUT_FILE}...")
    with open(INPUT_FILE, 'r') as f:
        stories = json.load(f)
    
    print(f"Processing {len(stories)} stories...")
    
    # Classify each story
    for i, story in enumerate(stories, 1):
        topic = classify_story(story)
        story['topic'] = topic
        print(f"[{i}/{len(stories)}] {story['title'][:60]}... -> {topic}")
    
    # Save the results
    print(f"\nSaving results to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(stories, f, indent=2)
    
    print("Done!")
    
    # Print summary of topics
    from collections import Counter
    topics = [s['topic'] for s in stories]
    topic_counts = Counter(topics)
    
    print("\nTopic Distribution:")
    for topic, count in topic_counts.most_common():
        print(f"  {topic}: {count}")

if __name__ == "__main__":
    main()