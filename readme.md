# Discord Message Cleaner

Discord Message Cleaner is a **self-bot** script written in Python that lets you quickly delete **all your own messages** in any channel (DM or server) using a simple command.

> ⚠️ **Important:** Self-bots violate the Discord Terms of Service. Use this project **only at your own risk** and preferably in test / private environments.

---

## Features

- `!clear` – deletes **all of your messages** in the current channel
- `!ping` – latency check (`Pong! (X ms)`)
- `!say <text>` – makes your account repeat the given text
- Colorful console output using **pystyle**
  - Clean login banner
  - Per‑message delete log in cyan → white gradient
- Small delay between deletions to reduce rate-limits

---

## Requirements

- **Python** 3.10+
- A Discord **user account token** (self-bot use – against ToS)
- Installed Python packages:
  - `discord.py-self`
  - `pystyle`

Install dependencies:

py -m pip install -U discord.py-self pystyle---

## Setup

1. **Clone the repository**

git clone https://github.com/beatsbyluca/Discord-Message-Cleaner.git
cd Discord-Message-Cleaner2. **Create / edit `config.json`**

{
  "token": "YOUR_USER_TOKEN_HERE",
  "target_user_id": 0,
  "command_prefix": "!"
}- `token`: your **Discord account token** (do **not** commit or share this)
- `command_prefix`: command prefix you want to use (default: `!`)
- `target_user_id`: currently unused, can stay `0`

3. **Run the script**

py main.pyIf everything works, the console will show a styled “Logged on as …” line.

---

## Usage

In any channel (DM or server) where your account can see messages:

- **Clear all your own messages**

 
  !clear
    The bot will:

  - walk the channel history from newest to oldest
  - delete only messages authored by **you**
  - log each deleted message in the console, for example:

 
  [CLEAR] Deleted message 5 (ID: 1234567890) in channel 1234567890
    At the end it sends a success message in Discord:

 
  ✅ Successfully cleared `X` messages with user <@YOUR_ID>
  - **Ping**

 
  !ping
  - **Say**

 
  !say Hello world
  ---

## How It Works

- Uses `discord.py-self`’s `discord.Client` to log in with your user token.
- Listens to `on_message` and only reacts to **your own** messages (`message.author.id == self.user.id`).
- Simple command parser:
  - Checks for configured `command_prefix`
  - Splits into command + args
- For `!clear`, it iterates over `message.channel.history()` and deletes only your messages, with a short `asyncio.sleep(0.3)` between each delete.

---

## Security & Warnings

- **Never** commit your token to Git, share it in screenshots, or paste it anywhere public.
- If your token is ever exposed, immediately:
  - Change your Discord password
  - Re‑login on all devices to invalidate the old token
- Using a self‑bot can result in **account termination** by Discord.

---

## License

You can choose a license that fits your needs (MIT is common). For example:

MIT License – see LICENSE file for details.
