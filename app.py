"""Flask application for the CI/CD greeting."""

from flask import Flask  # pylint: disable=import-error



app = Flask(__name__)

@app.route("/")
def home():
    """Return the home page greeting."""
    return "--- Hello, CI/CD with Docker! Miercoles 25"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
