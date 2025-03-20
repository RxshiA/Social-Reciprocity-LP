import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


async def generate_story(level):
    prompt = f"Generate a story suitable for a child at learning level {level}. There are levels of 1 to 10, 1 being the easiest to understand by a kid with Autism Spectrum Disorder and 10 being the hardest understand by a kid with Autism Spectrum Disorder. Keep it engaging and under 200 words."
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a children's storytelling assistant and you're a professional at it. You're creating a story for a child with Autism Spectrum Disorder. You know the child's learning level. You know how to keep the story engaging and easy to understand. You have experience in creating stories for children with Autism Spectrum Disorder."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    return response.choices[0].message.content.strip()


async def generate_mcqs(story):
    prompt = f"Generate 10 multiple-choice questions based on this story:\n\n{story}\nProvide 4 options for each question. Keep the questions simple and engaging for a child with Autism Spectrum Disorder. The questions should be easy to understand and answer. And give the correct answer for each question. The return object's one question should look like this: \n\n1. What is the color of the sky?\nA. Blue\nB. Red\nC. Green\nD. Yellow\n\nCorrect Answer: A"
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an educational MCQ generator. You're creating multiple-choice questions based on a story for a child with Autism Spectrum Disorder. You know how to keep the questions simple and engaging. You have experience in creating questions for children with Autism Spectrum Disorder."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        # max_tokens=00
    )
    return response.choices[0].message.content.strip()
