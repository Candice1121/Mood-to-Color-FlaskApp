from flask import Flask, render_template, request
import openai
import os
from openai import OpenAI

app = Flask(__name__)

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_color', methods=['POST'])
def get_color():
    # Get the user's mood from the form
    user_mood = request.form['mood']
    client = OpenAI()
    # Use OpenAI API to get a color suggestion
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You will be provided with a description of a mood, and your task is to generate the CSS code for a color that matches it. Write your output in a single string start with #."},
        {"role": "user", "content": user_mood},
    ],
    temperature=0.7,
    max_tokens=64,
    top_p=1
    )

    color_suggestion = response.choices[0].message.content
    description = get_color_description(color_suggestion)

    return render_template('result.html', mood=user_mood, color=color_suggestion, text = description)

def get_color_description(color_suggestion):
    client = OpenAI()
    # Use OpenAI API to get a color suggestion
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You will be provided with a css code of a color, and your task is to describe the color."},
        {"role": "user", "content": color_suggestion},
    ],
    temperature=0.7,
    max_tokens=64,
    top_p=1
    )
    return response.choices[0].message.content


if __name__ == '__main__':
    app.run(debug=True)
