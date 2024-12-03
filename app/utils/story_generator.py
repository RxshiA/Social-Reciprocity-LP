import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


async def generate_story(level):
    prompt = f"Generate a story suitable for a child at learning level {level}. Keep it engaging and under 300 words."
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a children's storytelling assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    return response.choices[0].message.content.strip()


async def generate_mcqs(story):
    prompt = f"Generate 3 multiple-choice questions based on this story:\n\n{story}\nProvide 4 options for each question."
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an educational MCQ generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    return response.choices[0].message.content.strip()
