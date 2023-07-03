import openai
import json


with open('secrets.json', 'r') as f:
    secrets = json.load(f)

keyword = "thailand street food"
openai.api_key = secrets['api_key']
response = openai.Completion.create(
    engine='text-davinci-003',  # Use 'text-davinci-003' for GPT-3.5 Turbo
    prompt=f"""
        Please ignore all previous instructions. I want you to respond only in language English.  I want you to act as a market research expert that speaks and writes fluent English. Pretend that you have the most accurate and most detailled information about keywords available. Pretend that you are able to develop a full SEO content plan in fluent English. I will give you the target keyword {keyword} .  From this keyword create a markdown table with a keyword list for an SEO content strategy plan on the topic {keyword} . Cluster the keywords according to the top 10 super categories and name the super category in the first column called keyword cluster. Add in another column with 7 subcategories for each keyword cluster or specific long-tail keywords for each of the clusters. List in another column the human searcher intent for the keyword. Cluster the topic in one of three search intent groups based on their search intent being, whether commercial, transactional or informational. Then in another column, write a simple but very click-enticing title to use for a post about that keyword. Then in another column write an attractive meta description that has the chance for a high click-thru-rate for the topic with 120 to a maximum of 155 words. The meta description shall be value based, so mention value of the article and have a simple call to action to cause the searcher to click.  Do NOT under any circumstance use too generic keyword like introduction  or conclusion or `tl:dr`. Focus on the most specific keywords only. Do not use single quotes, double quotes or any other enclosing characters in any of the columns you fill in. Do not explain why and what you are doing, just return your suggestions in the table. The markdown table shall be in English language and have the following columns:  keyword cluster, keyword, search intent, title, meta description. Here is the keyword to start again: {keyword}
""",
    max_tokens=1000,
)

value = response['choices'][0]['text'].strip()
import markdown
html = markdown.markdown(value)

