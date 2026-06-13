from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    review = ""

    if request.method == "POST":

        code = request.form["code"]

        review = f"""
Code Review

Lines: {len(code.splitlines())}

Suggestions:
- Add comments
- Handle exceptions
- Improve variable naming
"""

    return render_template(
        "index.html",
        review=review
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )