from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os
import traceback

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Flask App
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    review = ""

    if request.method == "POST":

        code = request.form.get("code", "")

        prompt = f"""
You are a Senior Software Engineer.

Review the following code and provide:

1. Bugs
2. Security Issues
3. Performance Improvements
4. Code Quality Suggestions
5. Overall Rating (/10)

Code:
{code}
"""

        try:
            response = model.generate_content(prompt)
            review = response.text

        except Exception:
            review = traceback.format_exc()

    return render_template(
        "index.html",
        review=review
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )