Star-Democrat Topic Classification - Nov. 3, 2025

I am choosing option one. In previous assignments when working with metadata we had to run simulations for the llm to sort CNS stories into different groups and I was pleased with its performance. I want to try this again today.

Co-Pilot conversation:
python
prompt = f"""
Analyze this news story and assign it a single topic category.
Choose a 1 or 2-word broad topic that best represents what this story is about.
Use consistent topic names - if you've used a topic before, use the same name.

Title: {story['title']}
Content: {story['content']}

Return only the topic name as a single string.
"""

I can see you're working on the Star-Democrat topic classification assignment. The code snippet you've selected shows the prompt structure for Option 1 (letting the LLM decide topics).

Here's a complete classify_topics.py script that implements this approach:
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
This script:

Reads your stardem_sample.json file
For each story, calls the LLM via the llm command-line tool
Adds a topic field to each story
Shows progress as it processes
Saves results to stardem_topics_classified.json
Prints a summary of topic distribution
To run it:
uv run python classify_topics.py
The script uses subprocess to call the llm tool and implements the Option 1 approach where the LLM decides topics on its own.

Results Analysis:
#### Quality Assessment
- Did the LLM (or you and the LLM) do a good job with the list of topics?
The LLM provided 125 unique topics, which was more than I expected. With that being said, that makes sense considering the stories it took were randomly selected. The most frequently used topics make a lot of sense, as they are broad and relevant subjects for readers, such as sports, history, and entertainment.
- Are there topics that seem too broad or too narrow?
The most repeated topics are very broad, which is not necessarily a bad thing. Sometimes people just want to read about sports, history, or entertainment. WHen it gets to the unique topics, they get a little too narrow. Topics including: 'inauguration gifts', 'adventurous travel', and 'books authors' are not things that most people would gravitate towards. 
- Are there stories that seem mis-categorized?
Some do, but for the most part they are spot-on.
- Give specific examples of stories and their topics:
Multiple stories about tv listings are labeled under 'sports.' Others have relevant topics, but maybe still are too broad. For example, a story about a dog park opening is labeled 'local news,' which is fair, but also the topic could be more specific to the park or pets/pet-owners consdering the range of unique topics the llm generated.

#### Topic Refinement
- What topics should be consolidated or combined?
A primary example can be seen among the most repeated topics. Sports, history, and goverment/politics are the top three most used topics, but there are also many sports, history, and government/politics stories with more specific topics that do not fall under the broader topics. For example, there are 18 stories under 'sports,' but 15 other sports-related stories with more narrow topic names. If combined, that would simplify things. The same goes for history and government politics. Consolidating those three alone would reduce the number of unique topics considerably.
- What topics are missing that would be useful?
Considering the number of unique topics (125/200), almost every subject mentioned in the stories is here. Missing topics aren't as much of an issue as misidentified/overlapping topics.
- Are there redundant or overlapping topics?
The redundant/overlapping topics are like those described in my first answer for this section of questions. Alongside the three topics I mentioned, redundancy/overlap also appears for topics such as entertainment, crime, and environment/conservation.
- How would you revise the topic list?
I would go first tell the llm to combine the topics that overlap in an effort to reduce the number of unique topics. After that, I would do a run-through myself to make sure it didn't miss any. I think that would greatly improve the quality of the topic list.

#### Approach Evaluation
- Did your chosen approach (Option 1 or 2) work well?
My chosen approach definitely worked well. The main benefit is the time saved by having the llm do the task in less than 10 minutes when it would have taken me far longer. As a result, there is some checking that has to be done after because I am not the one responsible for the choices, but for the most part, it did a good job.
- Would the other approach have been better? Why or why not?
I think the other approach would have been better for a smaller sample size. For 200 stories, I think option one is the more efficient choice, because, when paired with a powerful llm such as Claude Sonnet 4.5, it limits the errors made and provides quality answers. If the sample size was smaller, like no more than 50, I think option two would be more appealing.
- What surprised you about the results?
I was most surprised by the number of unique results considering the script instructed the llm to use repeat topics if the stories are similar. In future projects, I will work to improve with the prompts to avoid such a high number. I was also surprise by the low number of total misfires when it came to assigning topics. Most of the ones that weren't spot-on were due to the style of the story, such as tv listings or other forms of content that weren't narrative-structured articles.