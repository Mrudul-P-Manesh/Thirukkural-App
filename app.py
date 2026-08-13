from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():

    number = request.args.get("number", 1)

    url = f"https://tamil-kural-api.vercel.app/api/kural/{number}"

    response = requests.get(url)

    data = response.json()

    return render_template("index.html", kural=data)


if __name__ == "__main__":
    app.run(debug=True)