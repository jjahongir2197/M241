from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    count = 0
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        count = len(text.split())

    return render_template("index54.html", text=text, count=count)

if __name__ == "__main__":
    app.run(debug=True)
