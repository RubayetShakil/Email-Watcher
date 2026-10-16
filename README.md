# Email Monitoring Automation

A Python-based email monitoring script that connects to Gmail using IMAP over SSL, searches for unread emails, and filters messages using a configurable keyword.

The project was developed to reduce repetitive manual inbox checking and explore email automation on Linux.

## Features

- Connects securely to Gmail using IMAP over SSL.
- Searches the inbox for unread emails.
- Filters messages by a configurable keyword in the sender or subject.
- Extracts and displays plain-text email content.
- Loads configuration from environment variables.
- Can be run as a background Linux service using systemd (once configured).

## Technologies

- Python 3
- IMAP / Gmail
- `imaplib` and `email`
- `python-dotenv`
- Linux and systemd (optional)

## Project Structure

```text
therap-mail-watcher/
├── watcher.py
├── requirements.txt
├── config.example.json
├── README.md
├── .gitignore
└── logs/
```

The actual files may differ depending on your local configuration.

## Prerequisites

- Python 3
- A Gmail account with IMAP access enabled
- A Google App Password, if required by your account's authentication configuration
- Git (optional)

## Installation

Clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
cd therap-mail-watcher
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project directory:

```dotenv
EMAIL=your_email@gmail.com
APP_PASSWORD=your_gmail_app_password
EMAIL_KEYWORD=therap
```

Replace the example values with your own configuration.

**Security:** Never commit `.env`, passwords, or other secrets to GitHub. Use an account-specific App Password when applicable, and revoke it if it is exposed.

## Running the Script

Activate the virtual environment and run:

```bash
python watcher.py
```

The script checks for unread emails matching the configured keyword and prints the contents of matching plain-text messages.

Stop the script using `Ctrl+C`.

## Running at Startup with systemd

On Linux systems using systemd, the script can be configured to run as a service and start automatically at boot.

A systemd service requires the correct Python executable, project directory, service user, and environment configuration.

This section should be considered optional until the service has been configured and tested on your system.

## Current Limitations

- The script uses periodic polling rather than push notifications.
- Network failures and reconnection may require additional handling.
- Email parsing currently focuses on plain-text message content.
- Behavior with unread-message flags should be tested with a separate inbox before regular use.
