"""
Ejemplo básico de web utilizando Flask
"""

from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    """
    Función base
    """
    return "Hello, CI/CD with Docker! Miercoles 27"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
