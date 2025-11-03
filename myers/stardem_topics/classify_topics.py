import json
import subprocess
from pathlib import Path

# Configuration
INPUT_FILE = "stardem_sample.json"
OUTPUT_FILE = "stardem_topics_classified.json"
MODEL = "groq/meta-llama/llama-4-scout-17b-16e-instruct"

def classify_story(story):
    """Use LLM to classify a single story into a topic."""
    prompt = f"""
Analyze this news story and assign it a single topic category.
Choose a 1 or 2-word broad topic that best represents what this story is about.
Use consistent topic names - if you've used a topic before, use the same name.

Title: {story['title']}
Content: {story['content']}

Return only the topic name as a single string.
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