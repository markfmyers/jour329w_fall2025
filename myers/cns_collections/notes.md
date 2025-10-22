CNS Collections - Myers - Oct. 15 2025

I chose Baltimore as my topic. There are 64 stories.

I added primary_beat to the fields of metadata, because I think that would help break down the variety of subjects that are covered across the 64 stories. Baltimore is a very broad subject, so it will make it easier to draw conclusions with a more specific categories of news.

1. **Key Players**: Who appears most frequently?
Former Baltimore Mayor Catherine Pugh and state representative Elijah Cummings appear in four of the 64 stories. Current governor Wes Moore appears in three. Current Baltimore Mayor Brandon Scott, resident Dawn Ford, and Freddie Gray appear in two stories. These names make sense, as four of them served or still serve as prominent members of the state government. Gray died in Baltimore in a story that concerned the nation, so his inclusion is also not a surprise. Ford's inclusion was a surprise, as I had not heard of her. She was featured in two CNS stories published on December 4, 2017.

2. **Geographic Patterns**: Which areas get the most coverage?
Baltimore City and Baltimore (the county) get the most coverage by far. Only one other location was listed more than once (Hagerstown, named twice).

3. **Institutional Network**: Which organizations appear in stories?
For the most part there is a wide variety in CNS coverage of Baltimore. Only a few institutions/organizations appear multiple times. Subjects written about include high schools in the city, branches of local government, and notable venues in the city such as the Pimlico Race Course.

** copy paste for prototype**
cat prompt.txt enhanced_beat_stories.json | uv run llm -m anthropic/claude-opus-4-0 > prototype.md

- What did the structured metadata reveal about this beat?
It revealed key people, locations, organizations, and issues in the city.
- Does your `prototype.md` result seem useful? What does it do well and what does it not do well?
It provided more information than the initial findings of the json file. It gave more examples for each category which provides a wider scope for the topics discussed.
- Did you change your prompt, and if so, how? Did that work better?
I added "issue_type" to identify trends in the reasons behind each story. I also updated the sample names in the "people" category to include more relevant individuals than were previously listed. The names I used earliest only showed up once, so I thought providing examples of names that repeat throughout the stories would help generate more useful information.
- What would you do differently with more time or data?
I plan to add more metadata tags to further expand on trends that can be found in this data. I also plan to assess the quality of each prompt to see whether their inclusion is necessary once I have added more.