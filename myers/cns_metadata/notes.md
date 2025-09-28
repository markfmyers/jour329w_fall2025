CNS Metadata - September 27, 2025

Maryland colleges have produced over 300 NFL Draft picks
https://cnsmaryland.org/2024/04/23/maryland-colleges-have-produced-over-300-nfl-draft-picks/

Key People:
- Stefon Diggs
- Randy White
- Stan Jones
Main Organizations/Institutions:
- NFL
- Maryland Football
Geographic Locations:
- Maryland
Topics:
- Maryland Football
- NFL Draft
- NFL Terps
Story Type: Analysis
Story Rating: 1

Sellouts and snowstorms: The history of Opening Day in Baltimore
https://cnsmaryland.org/2024/03/27/sellouts-and-snowstorms-the-history-of-opening-day-in-baltimore/

Key People:
- Corbin Burnes
- Rodrigo López
- Jay Gibbons
Main Organizations/Institutions:
- Baltimore Orioles
Geographic Locations:
- Baltimore, Maryland
- Oriole Park at Camden Yards
- Memorial Stadium
Topics:
- Baltimore Orioles
- Opening Day
- Baltimore Baseball
Story Type: Analysis
Story Rating: 1

Los Angeles Rams script storybook ending in Super Bowl win
https://cnsmaryland.org/2022/02/14/los-angeles-rams-win-super-bowl-lvi-cincinnati-bengals/

Key People:
- Sean McVay
- Aaron Donald
- Matthew Stafford
Main Organizations/Institutions:
- National Football League
- Los Angeles Rams
- Cincinnati Bengals
Geographic Locations
- Inglewood, California
- SoFi Stadium
Topics:
- Super Bowl
- LA Rams
- Cincinnati Bengals
Story Type: Game Story
Story Rating: 2

The numbers behind the US men’s national soccer team in Europe’s top five leagues
https://cnsmaryland.org/2021/05/06/the-numbers-behind-the-us-mens-national-soccer-team-in-europes-top-five-leagues/

Key People:
- Christian Pulisic
- Giovanni Reyna
- Weston McKennie
Main Organizations/Institutions:
- U.S. Soccer
- Chelsea FC
- Borussia Dortmund
Geographic Locations:
- Europe
Topics:
- US Soccer
- European Football
- Market Value
Story Type: Analysis
Story Rating: 1

Maryland is at the forefront of youth cricket in the U.S.
https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/

Key People:
- Sham Chotoo
Main Organizations/Institutions:
- Maryland Youth Cricket Association
- Maryland Youth Cricket League
- International Cricket Council
Geographic Locations:
- Maryland
- Prince George's County
- Montgomery County
Topics:
- US Cricket
- Maryland Cricket
- Youth Cricket
Story Type: Feature
Story Rating: 3

@markfmyers ➜ /workspaces/jour329w_fall2025 (main) $ uv run python -m newspaper --url=https://cnsmaryland.org/2024/04/23/maryland-colleges-have-produced-over-300-nfl-draft-picks/ -of=text | uv run llm -m groq/moonshotai/kimi-k2-instruct-0905 "Extract structured metadata from this news story 
and return as JSON with these exact fields:
{                                                                                                           
  \"url\": \"https://cnsmaryland.org/2024/04/23/maryland-colleges-have-produced-over-300-nfl-draft-picks/\",
  \"people\": [\"list of up to 3 people with their titles/roles\"],
  \"organizations\": [\"government agencies, companies, groups mentioned\"],  
  \"locations\": [\"cities, counties, states, specific places\"],
  \"topics\": [\"3-5 topic tags, max 2 words each\"],
  \"story_type\": \"breaking news, feature, analysis, investigation, other\",
  \"impact\": \"a rating of the story's importance on a scale from 1 to 5, taking into account its impact on people\",
  \"
}"

```json
{
  "url": "https://cnsmaryland.org/2024/04/23/maryland-colleges-have-produced-over-300-nfl-draft-picks/",
  "people": ["Beau Brade (safety prospect)", "Stefon Diggs (wide receiver)", "Randy White (Hall of Fame defensive lineman)"],
  "organizations": ["NFL", "University of Maryland", "Morgan State University", "U.S. Naval Academy", "Towson University", "Minnesota Vikings", "Dallas Cowboys"],
  "locations": ["Maryland", "College Park", "Annapolis", "Baltimore"],
  "topics": ["NFL Draft", "Maryland football", "NFL history"],
  "story_type": "feature",
  "impact": 2
}
```

@markfmyers ➜ /workspaces/jour329w_fall2025 (main) $ uv run python -m newspaper --url=https://cnsmaryland.org/2024/03/27/sellouts-and-snowstorms-the-history-of-opening-day-in-baltimore/ -of=text | uv run llm -m groq/moonshotai/kimi-k2-instruct-0905 "Extract structured metadata from this news story 
and return as JSON with these exact fields:
{                                                                                                           
  \"url\": \"https://cnsmaryland.org/2024/03/27/sellouts-and-snowstorms-the-history-of-opening-day-in-baltimore/\",
  \"people\": [\"list of up to 3 people with their titles/roles\"],
  \"organizations\": [\"government agencies, companies, groups mentioned\"],  
  \"locations\": [\"cities, counties, states, specific places\"],
  \"topics\": [\"3-5 topic tags, max 2 words each\"],
  \"story_type\": \"breaking news, feature, analysis, investigation, other\",
  \"impact\": \"a rating of the story's importance on a scale from 1 to 5, taking into account its impact on people\",
  \"
}"

```json
{
  "url": "https://cnsmaryland.org/2024/03/27/sellouts-and-snowstorms-the-history-of-opening-day-in-baltimore/",
  "people": [
    "Corbin Burnes – starting pitcher, 2024 Orioles debut",
    "Rodrigo López – starting pitcher, 2003 snow-delayed opener",
    "Jay Gibbons – right fielder, 2003 snow-delayed opener"
  ],
  "organizations": [
    "Baltimore Orioles",
    "Los Angeles Angels",
    "Camden Yards",
    "Memorial Stadium"
  ],
  "locations": [
    "Baltimore, MD",
    "Camden Yards",
    "Memorial Stadium",
    "Eutaw Street"
  ],
  "topics": [
    "Opening Day",
    "weather",
    "attendance",
    "history"
  ],
  "story_type": "feature",
  "impact": 2
}
```

@markfmyers ➜ /workspaces/jour329w_fall2025 (main) $ uv run python -m newspaper --url=https://cnsmaryland.org/2022/02/14/los-angeles-rams-win-super-bowl-lvi-cincinnati-bengals/ -of=text | uv run llm -m groq/moonshotai/kimi-k2-instruct-0905 "Extract structured metadata from this news story 
and return as JSON with these exact fields:
{                                                                                                           
  \"url\": \"https://cnsmaryland.org/2022/02/14/los-angeles-rams-win-super-bowl-lvi-cincinnati-bengals/\",
  \"people\": [\"list of up to 3 people with their titles/roles\"],
  \"organizations\": [\"government agencies, companies, groups mentioned\"],  
  \"locations\": [\"cities, counties, states, specific places\"],
  \"topics\": [\"3-5 topic tags, max 2 words each\"],
  \"story_type\": \"breaking news, feature, analysis, investigation, other\",
  \"impact\": \"a rating of the story's importance on a scale from 1 to 5, taking into account its impact on people\",
  \"
}"

{
  "url": "https://cnsmaryland.org/2022/02/14/los-angeles-rams-win-super-bowl-lvi-cincinnati-bengals/",
  "people": ["Cooper Kupp (Super Bowl MVP, Rams WR)", "Aaron Donald (Rams DT)", "Eric Weddle (Rams S, came out of retirement)"],
  "organizations": ["Los Angeles Rams", "Cincinnati Bengals", "NFL"],
  "locations": ["Los Angeles", "SoFi Stadium"],
  "topics": ["Super Bowl LVI", "Rams victory", "Championship rings"],
  "story_type": "feature",
  "impact": 4
}

@markfmyers ➜ /workspaces/jour329w_fall2025 (main) $ uv run python -m newspaper --url=https://cnsmaryland.org/2021/05/06/the-numbers-behind-the-us-mens-national-soccer-team-in-europes-top-five-leagues/ -of=text | uv run llm -m groq/moonshotai/kimi-k2-instruct-0905 "Extract structured metadata from this news story 
and return as JSON with these exact fields:
{                                                                                                           
  \"url\": \"https://cnsmaryland.org/2021/05/06/the-numbers-behind-the-us-mens-national-soccer-team-in-europes-top-five-leagues/\",
  \"people\": [\"list of up to 3 people with their titles/roles\"],
  \"organizations\": [\"government agencies, companies, groups mentioned\"],  
  \"locations\": [\"cities, counties, states, specific places\"],
  \"topics\": [\"3-5 topic tags, max 2 words each\"],
  \"story_type\": \"breaking news, feature, analysis, investigation, other\",
  \"impact\": \"a rating of the story's importance on a scale from 1 to 5, taking into account its impact on people\",
  \"
}"

```json
{
  "url": "https://cnsmaryland.org/2021/05/06/the-numbers-behind-the-us-mens-national-soccer-team-in-europes-top-five-leagues/",
  "people": [
    "Christian Pulisic - Chelsea winger / USMNT standout",
    "Giovanni Reyna - Borussia Dortmund midfielder / USMNT prospect",
    "Weston McKennie - Juventus midfielder / USMNT regular"
  ],
  "organizations": [
    "USMNT",
    "Chelsea FC",
    "Borussia Dortmund",
    "Juventus",
    "FC Barcelona",
    "RB Leipzig",
    "CONCACAF",
    "FIFA"
  ],
  "locations": [
    "Europe",
    "England",
    "Germany",
    "Spain",
    "Italy",
    "France",
    "Russia",
    "Trinidad & Tobago",
    "Switzerland",
    "Honduras"
  ],
  "topics": [
    "USMNT players",
    "transfer values",
    "World Cup"
  ],
  "story_type": "feature",
  "impact": 3
}
```

@markfmyers ➜ /workspaces/jour329w_fall2025 (main) $ uv run python -m newspaper --url=https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/ -of=text | uv run llm -m groq/moonshotai/kimi-k2-instruct-0905 "Extract structured metadata from this news story  
and return as JSON with these exact fields:
{                                                                                                           
  \"url\": \"https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/\",
  \"people\": [\"list of up to 3 people with their titles/roles\"],
  \"organizations\": [\"government agencies, companies, groups mentioned\"],  
  \"locations\": [\"cities, counties, states, specific places\"],
  \"topics\": [\"3-5 topic tags, max 2 words each\"],
  \"story_type\": \"breaking news, feature, analysis, investigation, other\",
  \"impact\": \"a rating of the story's importance on a scale from 1 to 5, taking into account its impact on people\",
  \"
}"

```json
{
  "url": "https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/",
  "people": [
    "Sham Chotoo – founder, Maryland Youth Cricket Association",
    "Lisa Ramjit – middle-schooler, U.S. women’s national squad",
    "Wesley Jackson – 13-year-old record-setting player"
  ],
  "organizations": [
    "Maryland Youth Cricket Association (MYCA)",
    "Bowie Boys and Girls Club",
    "Major League Cricket",
    "International Cricket Council (ICC)",
    "Prince George’s County government"
  ],
  "locations": [
    "Maryland",
    "Prince George’s County",
    "Montgomery County",
    "Howard County",
    "Bowie",
    "Silver Spring",
    "Washington, D.C.",
    "Virginia"
  ],
  "topics": ["youth cricket", "grassroots growth", "school programs", "infrastructure", "girls cricket"],
  "story_type": "feature",
  "impact": 4
}
```

@markfmyers ➜ /workspaces/jour329w_fall2025 (main) $ uv run python -m newspaper --url=https://cnsmaryland.org/2024/04/23/maryland-colleges-have-produced-over-300-nfl-draft-picks/ -of=text | uv run llm -m claude-4-sonnet "Extract structured metadata from this news story 
and return as JSON with these exact fields:
{                                                                                                           
  \"url\": \"https://cnsmaryland.org/2024/04/23/maryland-colleges-have-produced-over-300-nfl-draft-picks/\",
  \"people\": [\"list of up to 3 people with their titles/roles\"],
  \"organizations\": [\"government agencies, companies, groups mentioned\"],  
  \"locations\": [\"cities, counties, states, specific places\"],
  \"topics\": [\"3-5 topic tags, max 2 words each\"],
  \"story_type\": \"breaking news, feature, analysis, investigation, other\",
  \"impact\": \"a rating of the story's importance on a scale from 1 to 5, taking into account its impact on people\",
  \"
}"

```json
{
  "url": "https://cnsmaryland.org/2024/04/23/maryland-colleges-have-produced-over-300-nfl-draft-picks/",
  "people": [
    "Stefon Diggs - Wide receiver, former University of Maryland player",
    "Randy White - Former Maryland Terrapins standout, second overall pick in 1975",
    "Joe Cardona - New England Patriots long snapper, drafted from Navy in 2015"
  ],
  "organizations": [
    "NFL",
    "University of Maryland",
    "Dallas Cowboys",
    "Minnesota Vikings",
    "New England Patriots",
    "Morgan State",
    "Naval Academy",
    "Towson",
    "Maryland Eastern Shore",
    "Philadelphia Eagles"
  ],
  "locations": [
    "Maryland",
    "College Park"
  ],
  "topics": [
    "NFL Draft",
    "College Football",
    "Maryland Universities",
    "Hall Fame",
    "Sports Statistics"
  ],
  "story_type": "feature",
  "impact": 2
}
```

@markfmyers ➜ /workspaces/jour329w_fall2025 (main) $ uv run python -m newspaper --url=https://cnsmaryland.org/2024/03/27/sellouts-and-snowstorms-the-history-of-opening-day-in-baltimore/ -of=text | uv run llm -m claude-4-sonnet "Extract structured metadata from this news story 
and return as JSON with these exact fields:
{                                                                                                           
  \"url\": \"https://cnsmaryland.org/2024/03/27/sellouts-and-snowstorms-the-history-of-opening-day-in-baltimore/\",
  \"people\": [\"list of up to 3 people with their titles/roles\"],
  \"organizations\": [\"government agencies, companies, groups mentioned\"],  
  \"locations\": [\"cities, counties, states, specific places\"],
  \"topics\": [\"3-5 topic tags, max 2 words each\"],
  \"story_type\": \"breaking news, feature, analysis, investigation, other\",
  \"impact\": \"a rating of the story's importance on a scale from 1 to 5, taking into account its impact on people\",
  \"
}"

```json
{
  "url": "https://cnsmaryland.org/2024/03/27/sellouts-and-snowstorms-the-history-of-opening-day-in-baltimore/",
  "people": [
    "Rodrigo López - Former Orioles starting pitcher",
    "Corbin Burnes - Orioles starting pitcher and former Cy Young winner", 
    "Ellis Burks - Former Cleveland player"
  ],
  "organizations": [
    "Baltimore Orioles",
    "Los Angeles Angels",
    "Cleveland Indians",
    "Major League Baseball"
  ],
  "locations": [
    "Baltimore",
    "Camden Yards",
    "Memorial Stadium",
    "Eutaw Street",
    "Maryland"
  ],
  "topics": [
    "Baseball",
    "Opening Day",
    "Weather",
    "Attendance",
    "Sports History"
  ],
  "story_type": "feature",
  "impact": 2
}
```

@markfmyers ➜ /workspaces/jour329w_fall2025 (main) $ uv run python -m newspaper --url=https://cnsmaryland.org/2022/02/14/los-angeles-rams-win-super-bowl-lvi-cincinnati-bengals/ -of=text | uv run llm -m claude-4-sonnet "Extract structured metadata from this news story 
and return as JSON with these exact fields:
{                                                                                                           
  \"url\": \"https://cnsmaryland.org/2022/02/14/los-angeles-rams-win-super-bowl-lvi-cincinnati-bengals/\",
  \"people\": [\"list of up to 3 people with their titles/roles\"],
  \"organizations\": [\"government agencies, companies, groups mentioned\"],  
  \"locations\": [\"cities, counties, states, specific places\"],
  \"topics\": [\"3-5 topic tags, max 2 words each\"],
  \"story_type\": \"breaking news, feature, analysis, investigation, other\",
  \"impact\": \"a rating of the story's importance on a scale from 1 to 5, taking into account its impact on people\",
  \"
}"

```json
{
  "url": "https://cnsmaryland.org/2022/02/14/los-angeles-rams-win-super-bowl-lvi-cincinnati-bengals/",
  "people": [
    "Eric Weddle - Los Angeles Rams safety",
    "Sean McVay - Rams coach", 
    "Aaron Donald - Rams defensive tackle"
  ],
  "organizations": [
    "Los Angeles Rams",
    "Cincinnati Bengals", 
    "NFL"
  ],
  "locations": [
    "Los Angeles",
    "SoFi Stadium"
  ],
  "topics": [
    "Super Bowl",
    "Championship",
    "Football",
    "Sports",
    "Comeback"
  ],
  "story_type": "breaking news",
  "impact": 4
}
```

@markfmyers ➜ /workspaces/jour329w_fall2025 (main) $ uv run python -m newspaper --url=https://cnsmaryland.org/2021/05/06/the-numbers-behind-the-us-mens-national-soccer-team-in-europes-top-five-leagues/ -of=text | uv run llm -m claude-4-sonnet "Extract structured metadata from this news story 
and return as JSON with these exact fields:
{                                                                                                           
  \"url\": \"https://cnsmaryland.org/2021/05/06/the-numbers-behind-the-us-mens-national-soccer-team-in-europes-top-five-leagues/\",
  \"people\": [\"list of up to 3 people with their titles/roles\"],
  \"organizations\": [\"government agencies, companies, groups mentioned\"],  
  \"locations\": [\"cities, counties, states, specific places\"],
  \"topics\": [\"3-5 topic tags, max 2 words each\"],
  \"story_type\": \"breaking news, feature, analysis, investigation, other\",
  \"impact\": \"a rating of the story's importance on a scale from 1 to 5, taking into account its impact on people\",
  \"
}"

```json
{
  "url": "https://cnsmaryland.org/2021/05/06/the-numbers-behind-the-us-mens-national-soccer-team-in-europes-top-five-leagues/",
  "people": [
    "Christian Pulisic - Chelsea player, most valuable USMNT player",
    "Giovanni Reyna - Borussia Dortmund player, second most valuable",
    "Weston McKennie - Juventus player"
  ],
  "organizations": [
    "United States men's national soccer team (USMNT)",
    "FIFA",
    "Chelsea",
    "Borussia Dortmund",
    "Juventus",
    "FC Barcelona",
    "RB Leipzig",
    "CONCACAF"
  ],
  "locations": [
    "United States",
    "Europe",
    "England",
    "Germany", 
    "Spain",
    "Italy",
    "France",
    "Russia",
    "Trinidad & Tobago"
  ],
  "topics": [
    "Soccer",
    "World Cup",
    "Player Transfers",
    "International Competition",
    "European Leagues"
  ],
  "story_type": "analysis",
  "impact": "3"
}
```

@markfmyers ➜ /workspaces/jour329w_fall2025 (main) $ uv run python -m newspaper --url=https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/ -of=text | uv run llm -m claude-4-sonnet "Extract structured metadata from this news story 
and return as JSON with these exact fields:
{                                                                                                           
  \"url\": \"https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/\",
  \"people\": [\"list of up to 3 people with their titles/roles\"],
  \"organizations\": [\"government agencies, companies, groups mentioned\"],  
  \"locations\": [\"cities, counties, states, specific places\"],
  \"topics\": [\"3-5 topic tags, max 2 words each\"],
  \"story_type\": \"breaking news, feature, analysis, investigation, other\",
  \"impact\": \"a rating of the story's importance on a scale from 1 to 5, taking into account its impact on people\",
  \"
}"

```json
{
  "url": "https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/",
  "people": [
    "Sham Chotoo - Founder of Maryland Youth Cricket Association",
    "Wesley Jackson - 13-year-old cricket player from Silver Spring",
    "Lisa Ramjit - Middle school student on women's national squad"
  ],
  "organizations": [
    "Bowie Boys and Girls Club",
    "Maryland Youth Cricket Association",
    "Maryland Youth Cricket League", 
    "Major League Cricket",
    "International Cricket Council",
    "United States Girls' U-19 team",
    "Prince George's County",
    "Montgomery County",
    "Howard County"
  ],
  "locations": [
    "Maryland",
    "Prince George's County",
    "Montgomery County", 
    "Howard County",
    "Silver Spring",
    "Bowie",
    "Virginia",
    "Washington D.C.",
    "Trinidad and Tobago"
  ],
  "topics": [
    "Youth Cricket",
    "Sports Development", 
    "Community Programs",
    "Athletic Infrastructure",
    "Cultural Integration"
  ],
  "story_type": "feature",
  "impact": 3
}
```

Below is my updated command to see what changed:

@markfmyers ➜ /workspaces/jour329w_fall2025 (main) $ uv run python -m newspaper --url=https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/ -of=text | uv run llm -m claude-4-sonnet "You are a data extraction expert. Study the article and return as JSON strictly following the guidelines below:
{                                                                                                           
  \"url\": \"https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/\",
  \"people\": [\"MAXIMUM of 3 people with their titles/roles, determined by who is most prominent in the article\"],
  \"organizations\": [\"government agencies, companies, groups mentioned\"],  
  \"locations\": [\"cities, counties, states, specific places\"],
  \"topics\": [\"3-5 topic tags, MAXIMUM 2 words each\"],
  \"story_type\": \"ONE OF: breaking news, feature, analysis, investigation, other\",
  \"impact\": \"a rating of the story's importance on a scale from 1 to 5, taking into account its severity\",
  \"
}"

```json
{
  "url": "https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/",
  "people": [
    "Sham Chotoo - Founder/Leader of Maryland Youth Cricket Association",
    "Wesley Jackson - 13-year-old cricket player from Silver Spring",
    "Lisa Ramjit - Middle school student on women's national squad"
  ],
  "organizations": [
    "Bowie Boys and Girls Club",
    "Maryland Youth Cricket Association",
    "Maryland Youth Cricket League",
    "Major League Cricket",
    "International Cricket Council",
    "United States Girls' U-19 team"
  ],
  "locations": [
    "Maryland",
    "Prince George's County",
    "Montgomery County",
    "Howard County",
    "Virginia",
    "Silver Spring",
    "Washington D.C.",
    "Trinidad and Tobago"
  ],
  "topics": [
    "youth cricket",
    "sports development",
    "community programs",
    "athletic leagues"
  ],
  "story_type": "feature",
  "impact": 3
}
```

Another change below:

@markfmyers ➜ /workspaces/jour329w_fall2025 (main) $ uv run python -m newspaper --url=https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/ -of=text | uv run llm -m claude-4-sonnet "You are a data extraction expert. Study the article and return as JSON strictly following the guidelines below. Be concise and only include relevant data:
{                                                                                                           
  \"url\": \"https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/\",
  \"people\": [\"MAXIMUM of 3 people with their titles/roles, determined by who is most prominent in the article\"],
  \"organizations\": [\"government agencies, companies, groups mentioned\"],  
  \"locations\": [\"cities, counties, states, specific places\"],
  \"topics\": [\"3-5 topic tags, MAXIMUM 2 words each\"],
  \"story_type\": \"ONE OF: breaking news, feature, analysis, investigation, other\",
  \"impact\": \"a rating of the story's importance on a scale from 1 to 5, taking into account its severity\",
  \"
}"

```json
{
  "url": "https://cnsmaryland.org/2021/04/23/maryland-is-at-the-forefront-of-youth-cricket-in-the-u-s/",
  "people": [
    "Sham Chotoo - Founder of Maryland Youth Cricket Association",
    "Wesley Jackson - 13-year-old cricket player",
    "Lisa Ramjit - Middle school student on women's national squad"
  ],
  "organizations": [
    "Bowie Boys and Girls Club",
    "Maryland Youth Cricket Association",
    "Maryland Youth Cricket League",
    "Major League Cricket",
    "International Cricket Council",
    "United States Girls' U-19 team"
  ],
  "locations": [
    "Maryland",
    "Prince George's County",
    "Montgomery County",
    "Howard County",
    "Virginia",
    "Silver Spring",
    "Washington D.C.",
    "Trinidad and Tobago"
  ],
  "topics": [
    "youth cricket",
    "sports development",
    "community programs",
    "athletic infrastructure"
  ],
  "story_type": "feature",
  "impact": 3
}
```

The LLMs on average labelled each story as of greater significance than I did. I gave multiple articles a score of 1, but neither LLM went below a 2. We also differed on the story classifications, and the LLM’s opposed each other’s classifications for two of the articles. The key persons, locations, and organizations were essentially the same, with the exception of some instances of more context (Claude was more detailed for the USMNT article, specifically noting Christian Pulisic as the most valuable American player, as noted in the article, whereas Groq classified him as a “standout.”

I decided to tell Claude that it was an expert for data extraction, specified word counts and the number of items in a list for multiple of the categories, and changed the wording for some (such as the impact and story type groups). I then changed it again telling it to be concise and avoid irrelevant datapoints. Neither change provided much of a difference. The LLM adjusted to the commands with the number of list items it provided, but did not change its tone, takeaways, or specific answers like the impact rating.

An issue of repeating this would be the shift in value of some of the answers. If I continued assessing the LLM’s with more articles from a different tag, the quality of the answers could shift due to the increased variety of the subjects and a shift in importance of each article, at least as it pertains to that specific question. I think the consistency could be improved by imposing specific limits on how many answers are given. Some of the LLM’s responses listed seven to eight names, locations, or organizations, whereas others only had a couple. That variance increases the margin for error. I think giving each prompt a hard cap, like the topic prompt has, would made the answers more consistent. 

The most complicated part was the inputting of the commands. The tiniest error can cause a setback, and cause the LLM to not respond the way I hoped. If the commands could be simplified, at least after it has been inputted once, and simply reduced to just supplying the link of the next article without having to repeat each detail of the prompt, I believe that would make this process much easier.