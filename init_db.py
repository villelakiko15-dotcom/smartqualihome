#!/usr/bin/env python
"""Initialize the database for local development (SQLite or MySQL)."""

import os
from app import create_app, db

def init_database():
    """Create all database tables."""
    app = create_app()
    
    with app.app_context():
        print("Initializing database...")
        db.create_all()
        print("✓ Database tables created successfully!")
        print(f"  Database: {app.config.get('SQLALCHEMY_DATABASE_URI', 'Unknown')}")

if __name__ == "__main__":
    init_database()
