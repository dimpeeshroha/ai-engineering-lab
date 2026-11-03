import os

from dotenv import load_dotenv
from groq import Groq
from shared.scraper import fetch_website_contents

load_dotenv()  # <-- this reads your .env file
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


system_prompt = """You analyze the contents of a website and
give a short, friendly summary. Ignore navigation menus.
Respond in markdown."""


def summarize(url):
    website = fetch_website_contents(url)
    print(website)
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Summarize this website:\n\n{website}"},
        ],
    )
    return response.choices[0].message.content
