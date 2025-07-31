from flask import Flask, render_template, request
from mors import MorseConverter

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        code = None
        action = request.form.get("text")
        word = request.form.get("string")
        if action == "text to morse":
            code = 1
        elif action == "morse to text":
            code = 2
        morse = MorseConverter()
        output = morse.convert(word, code, filename="morse_alphabet.json")
        return render_template("home.html", output=output)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)