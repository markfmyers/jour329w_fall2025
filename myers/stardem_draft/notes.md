Star-Democrat Draft Beak Book - Nov. 19, 2025

### Choose Your Approach
I chose option one for the education beat. Based on my results, I have a ton of important entity data, and the demographic covered spans across multiple districts.

### Design Your Beat Book Format
I chose the narrative guide as my format. For this topic and the Star-Democrat as a news source, it is critical to understand how the important people/organizations/places are and in which parts of the Eastern Shore they are. This format will make it readable while still containing crucial data.

**Command for first subset**
cat prompt.txt stories_subset_100_metadata.json | uv run llm -m groq/openai/gpt-oss-120b > prototype_v1.md

jq '.[0:10]' stories_metadata_only.json > stories_subset_10_metadata.json
cat prompt.txt stories_subset_10_metadata.json | uv run llm -m groq/openai/gpt-oss-120b > prototype_v1.md