SMARTQUALIHOME - Setup Guide

1) Prerequisites
- Python 3.11+ (3.12/3.13 supported)
- pip
- MySQL 8+ (optional; SQLite is the default)

2) Create and activate a virtual environment (Windows PowerShell)
  py -m venv .venv
  .\.venv\Scripts\Activate.ps1

3) Install dependencies
  pip install -r requirements.txt

4) Configure environment
Create a .env file in the project root.

Minimum example:
  SECRET_KEY=change-this-in-production
  DB_USE_SQLITE=true

Optional MySQL configuration:
  DB_USE_SQLITE=false
  DB_HOST=localhost
  DB_PORT=3306
  DB_USER=root
  DB_PASSWORD=your_password
  DB_NAME=smartqualihome

Optional SMTP (forgot password flow):
  MAIL_SERVER=smtp.yourprovider.com
  MAIL_PORT=587
  MAIL_USERNAME=your_email@example.com
  MAIL_PASSWORD=your_app_password
  MAIL_USE_TLS=true
  MAIL_USE_SSL=false
  MAIL_FROM=no-reply@yourdomain.com

IMPORTANT: Railway Deployment SMTP Setup
========================================
To enable password reset emails on Railway:

1. Configure these environment variables in your Railway project:
   - MAIL_SERVER: Your SMTP server (e.g., smtp.gmail.com, smtp.sendgrid.net)
   - MAIL_PORT: SMTP port (587 for TLS, 465 for SSL, 25 for unencrypted)
   - MAIL_USERNAME: Your SMTP username or email
   - MAIL_PASSWORD: Your SMTP password or API key (NOT your regular password for Gmail)
   - MAIL_USE_TLS: true (for port 587 with STARTTLS)
   - MAIL_USE_SSL: false (change to true for port 465)
   - MAIL_FROM: Sender email address (e.g., noreply@example.com)

2. For Gmail:
   - Use: MAIL_SERVER=smtp.gmail.com, MAIL_PORT=587, MAIL_USE_TLS=true
   - Generate an App Password (not your main password):
     https://support.google.com/accounts/answer/185833
   - Use the 16-character app password as MAIL_PASSWORD

3. For SendGrid:
   - Use: MAIL_SERVER=smtp.sendgrid.net, MAIL_PORT=587, MAIL_USE_TLS=true
   - MAIL_USERNAME=apikey
   - MAIL_PASSWORD=your_sendgrid_api_key

4. Test in Railway logs:
   - Deploy the app and check logs for "Password reset email sent" messages
   - If it shows "Failed to send password reset email", check the error message in logs

5) Initialize database
- SQLite mode: created automatically on app startup.
- MySQL mode:
  a) Run migrations/schema.sql
  b) Start app (runtime applies safe incremental schema checks)

6) Run the app
  py run.py

7) Open in browser
  http://127.0.0.1:5000

Default seeded accounts (created only when missing)
- Admin
  Email: admin@smartqualihome.com
  Password: Admin@2026!
- Agent
  Email: agent@smartqualihome.com
  Password: Agent@2026!
- Client
  Email: client@smartqualihome.com
  Password: Client@2026!

Recent dashboard notes
- Admin notifications are merged and sorted by latest timestamp.
- Admin Activity Log includes full detail request event filtering.
- Client Home includes a Qualified Properties for You section.
- Client Browse includes a Qualified Only filter.
- Client Profile read-only blocks now retain left icon alignment.

Notes
- Uploaded files: instance/uploads
- SQLite database: instance/smartqualihome.db
- Never commit real credentials in .env
