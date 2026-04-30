# Installation Guide

## 1. Clone the repository

```bash
git clone <repository_url>
cd <repository_directory>
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Create a Discord Application

Go to the [Discord Developer Portal](https://discord.com/developers/home)

* Sign in
* Go to **Applications**
* Click and create a **New Application**

## 4. Configure the Bot

* Open your application
* Go to the **Bot** section
* Enable **Public Bot** (if needed)
* Click **Reset Token** and copy it

## 5. Create environment file

Create a file named `.env` in the project root:

```env
TOKEN=your_bot_token_here
```

Note: Never share your token with anyone.

## 6. Enable intents

In the **Bot** section, enable:

* Server Members Intent
* Message Content Intent

## 7. Set up OAuth2 link

* Go to **OAuth2** under **Overview** menu, just above **Bot**.
* Under **Scopes**, select:

  * `bot`
* Under **Bot Permissions**, enable:

### General Permissions

* Manage Roles
* View Channels

### Text Permissions

* Send Messages
* Create Public Threads
* Send Messages in Threads
* Manage Threads
* Embed Links
* Attach Files
* Use External Emojis
* Add Reactions
* Create Polls

## 8. Invite the bot

* Copy the generated URL from the bottom of the page
* Paste and open it in your browser
* Add the bot to your server

## 9. Run the bot

```bash
python bot.py
```
