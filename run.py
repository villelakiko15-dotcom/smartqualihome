"""SMARTQUALIHOME Flask entry point.

Run with:
    python run.py
or:
    flask run
or (production):
    gunicorn run:app
"""
import os
from dotenv import load_dotenv

# Load project environment variables before importing the app package.
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

from app import create_app

app = create_app()

if __name__ == "__main__":
    # Local development only
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
