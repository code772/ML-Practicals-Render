from flask import Flask, send_file, abort
from pathlib import Path
import re

app = Flask(__name__)

PRACTICALS_FOLDER = Path(__file__).parent


@app.route("/")
def home():
    return "ML Practicals Server is Running!"


@app.route("/t/<practical_id>")
def get_practical(practical_id):

    # Allow names such as 1, 2a, 2b, 10, 11
    if not re.fullmatch(r"[0-9]+[a-z]?", practical_id):
        abort(404)

    file_path = PRACTICALS_FOLDER / f"{practical_id}.txt"

    if not file_path.is_file():
        abort(404, description="Practical not found")

    return send_file(
        file_path,
        mimetype="text/plain; charset=utf-8"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
