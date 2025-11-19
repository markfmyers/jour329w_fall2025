Star-Democrat Draft Beat Book - Nov. 19, 2025

### Choose Your Approach
I chose option one for the education beat. Based on my results, I have a ton of important entity data, and the demographic covered spans across multiple districts.

### Design Your Beat Book Format
I chose the narrative guide as my format. For this topic and the Star-Democrat as a news source, it is critical to understand how the important people/organizations/places are and in which parts of the Eastern Shore they are. This format will make it readable while still containing crucial data.

**Command for first subset**
```bash
jq '[.[] | del(.llm_classification, .llm_classification_meta, .entity_extraction_model, .content_source, .article_id, .people, .places, .organizations)]' stories_with_entities_v2.json > alternate_stories_with_entities_v1.json

jq '[.[] | select(. != null)] | sort_by(now * (1 + (.docref | length))) | .[0:200]' stories_with_entities_v4.json > stories_sample_200.json

cat prompt.txt stories_sample_200.json | uv run llm -m groq/openai/gpt-oss-120b > prototype_v1.md
```
