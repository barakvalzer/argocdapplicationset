from flask import Flask
import os

app = Flask(__name__)
env = os.environ.get("ENV", "unknown")

@app.route("/")
def home():
    return f"<h1>Hello from Flask in {env}!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
