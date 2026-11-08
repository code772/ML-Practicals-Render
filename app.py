
from flask import Flask, Response
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
PRACTICALS_DIR = BASE_DIR / "practicals"

@app.route("/")
def home():
    return "ML Practicals Server is Running!"

@app.route("/t/<int:number>")
def get_practical(number):
    file_path = PRACTICALS_DIR / f"{number}.txt"

    if not file_path.exists():
        return "Practical not found", 404

    content = file_path.read_text(encoding="utf-8")

    return Response(content, mimetype="text/plain")

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
