from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    review = ""

    if request.method == "POST":

        code = request.form["code"]

        prompt = f"""
You are a senior software engineer.

Review the following code and provide:

1. Bugs
2. Security Issues
3. Performance Improvements
4. Code Quality Suggestions

Code:

{code}
"""

        try:
            response = model.generate_content(prompt)
            review = response.text

        except Exception as e:
            review = f"Error: {str(e)}"

    return render_template(
        "index.html",
        review=review
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )