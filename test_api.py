import openai
import os

client = openai.OpenAI()

# Example chat completion request
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You will be provided with a description of a mood, and your task is to generate the CSS code for a color that matches it. Write your output in a single string start with #."},
        {"role": "user", "content": "Nice day."},
    ],
    temperature=0.7,
    max_tokens=64,
    top_p=1
)
color_suggestion = response.choices[0].message.content
print(color_suggestion)
