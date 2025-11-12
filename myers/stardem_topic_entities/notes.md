Star-Dem Topic Entities - Nov. 11, 2025

I chose sports as my topic because it is a primary interest of mine, and a subject I have often chosen in previous assignments like this.

For my first run, I used groq/openai/gpt-oss-120b.

For my second run, I chose to pivot to education stories, because there is an overlap between the high school sports being written about the education stories that cover the same schools. I used glm-4.6:cloud.

When updating my prompt, I had copilot give more context, including examples of people/organizations worth and not worth including, as well as story types to avoid, like obituaries, legal notices, or other miscellaneous stories that do not fit with the subject.

I figured these changes would make for a more streamlined output, with less fluff and only the important data.

#### Accuracy Assessment (Sports)
Are the extracted entities accurate? Check 5-10 stories in detail
- Yes. The entities are accurate and match the content of the stories.
Are there false positives (entities that shouldn't be there)?
- There are some false positives in the 5-10 stories I checked in detail. While the entities I am describing are named in the stories, they are often only mentioned once, like a baseball team, or a location, and do not serve a key purpose to the story. There are stories where too many entities are listed that are not central to the content itself, like the story about Ronald Acuna Jr. or the story about the Seventh Annual Solomons Dragon Boat Festival.
Are there false negatives (important entities that were missed)?
- I did not notice entities missing that are key to the stories. If anything, too many entities are named, rather than not enough.
Do the entities match what you see when reading the stories?
- Yes.

#### Accuracy Assessment (Education)
Are the extracted entities accurate? Check 5-10 stories in detail
- Yes. The entities are accurate and match the content of the stories.
Are there false positives (entities that shouldn't be there)?
- No, and this run did a much better job ignoring briefly mentioned names/organizations than the sports run.
Are there false negatives (important entities that were missed)?
- No.
Do the entities match what you see when reading the stories?
- Yes.

#### Entity Quality
**People**: Are full names captured correctly? Are titles/roles included appropriately?
- Yes. The entities are exactly as mentioned in the stories, for both names and titles/roles.
**Places**: Are location names consistent (e.g., "Easton" vs "Easton, MD")? Are they specific enough?
- Yes. For the most part, if a location is mentioned, it is repeated later if in another story and not split up like the Easton example.
**Organizations**: Are organization names complete and accurate? Are abbreviations expanded?
- Yes, they are accurate. Abbreviations are listed in the entities as the appear in the story, unless expanded upon in the story, in which the entity follows such usage.

#### Comparison Between Models/Prompts
How do the results differ between your two runs?
- The second prompt followed the instructions better. It adhered more to the "ignore" sections, leaving out names/locations/organizations that were not essential to the story.
Which model/prompt produced better results? Why?
- The second prompt was better for the reason listed above.
Did focusing on "important" entities improve quality?
- Yes, especially for the second prompt/run.
Are there systematic differences in how entities are extracted?
- Yes. For my sports stories, more people, places, and organizations were extracted per story (6.8 compared to 3.2, 4.0 compared to 1.9, and 3.6 compared to 2.7, respectively). The sports stories also had a 2.5% empty result rate, compared to 10% for the education stories.

#### Topic-Specific Patterns
What are the most common places? Organizations?
- Easton, MD is by far the most frequently mentioned place, at 14 times. No other location has more than three mentions. For organizations, the Bayside Conference is mentioned most with six, which makes sense for a high-school sports centric newspaper. Second to that is the Baltimore Orioles with 3, which again makes sense for a paper in Maryland. All other organizations are mentioned no more than twice.
Do these patterns make sense for your chosen topic?
- Yes, these patterns make sense for both sports and education.
Are there any surprising or unexpected entities?
- I was surprised to see Wrexham AFC, since that is a bit niche for the paper to cover, but the owners are popular and there is a TV show that people in the US watch, so I guess I shouldn't have been surprised that it could sneak into an article.
What changes would you need to make to ensure that a beat book built with this information would be properly scoped?
- Any duplications would need to be identified and removed. There should be standardization for all entities named for the sake of clarity. Names should be presented in the same style, and the same would go for organizations and places. Non-local content could be filtered out to maintain an emphasis on the stories relevant to the beat. Roles that go with names mentioned in stories should be compiled alongside the names of the people (for example, a member of local government should have their title with their name, or a coach of a sports team). These changes would improve the quality of a beat book for this subject and area.