Star-Dem Entities - Nov. 5, 2025

For the first run, I used groq/openai/gpt-oss-120b.

For the second run, I used groq/meta-llama/llama-4-maverick-17b-128e-instruct.

Use facets and filters to explore the new metadata and evaluate the results in your `notes.md` file. Do the results look accurate? Do the results from the two models agree? What's the best prompt for this? Take your time and use the stories to help you understand things better.
- My results are somewhat different, and the first run seems to have run more successfully. The script changes for the second run led to some extraction errors, that I found from copilot. For example, the first run had 11 stories that tagged Donald Trump under people, but the second only had five. At first glance, I thought that was a result of the changes to the prompt, specifically where I had it not include names that are only mentioned briefly, without being integral to the story. I found out that there were errors in the extraction that led to the same stories where his name was tagged in the first run, having no names tagged in the second.
- Although the intention of the second prompt was to be more concise and trim out the fat, the first run was more successful. If I were to keep perfecting them, I think it could change, but the consequence of a more specific prompt is that the llm can fail more often when trying to execute. Outside of the aforementioned errors, the prompts do mostly agree, which is a result of them being fairly similar, just the second run being more streamlined. I think this was an interesting exercise.