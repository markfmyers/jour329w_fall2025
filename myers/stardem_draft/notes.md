Star-Democrat Draft Beak Book - Nov. 19, 2025

### Choose Your Approach
I chose option one for the education beat. Based on my results, I have a ton of important entity data, and the demographic covered spans across multiple districts.

### Design Your Beat Book Format
I chose the narrative guide as my format. For this topic and the Star-Democrat as a news source, it is critical to understand how the important people/organizations/places are and in which parts of the Eastern Shore they are. This format will make it readable while still containing crucial data.

**Command for first subset**
cat prompt.txt stories_subset_100_metadata.json | uv run llm -m groq/openai/gpt-oss-120b > prototype_v1.md

jq '.[0:10]' stories_metadata_only.json > stories_subset_10_metadata.json
cat prompt.txt stories_subset_10_metadata.json | uv run llm -m groq/openai/gpt-oss-120b > prototype_v1.md

Create a comprehensive narrative guide for a new reporter joining the Star-Democrat to cover education on Maryland's Eastern Shore. This guide should serve as an onboarding document that introduces all significant people, places, and organizations in the region's education landscape.

Using the provided education stories, create a beat book organized by major themes (not alphabetically) that covers:

**Key Players**: Identify superintendents, principals, school board members, teachers, union leaders, and other influential figures. Note their roles, which districts/schools they represent, and their positions on major issues.

**Institutions & Geography**: Map out the school districts, individual schools, colleges, education-related organizations, and community groups across the Eastern Shore. Explain the geographic and demographic context that shapes education coverage in this region.

**Recurring Issues & Patterns**: Highlight the major education topics that drive coverage—funding challenges, student achievement, facility issues, policy debates, community tensions. Use specific story examples to illustrate these patterns.

**Relationships & Power Dynamics**: Explain how different entities interact—district vs. state relationships, community vs. administration dynamics, inter-district cooperation or competition.

Write in a business casual, conversational tone that balances being informative with being readable. Think of this as a practical field guide that will help a new reporter quickly understand who matters, where to focus attention, and what issues define education coverage in this market.

