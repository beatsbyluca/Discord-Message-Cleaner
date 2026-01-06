# 🔷 DISCORD MESSAGE CLEANER

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

**Automatic Discord Self-Bot Message Cleaner**

[Installation](#-installation) • [Features](#-features) • [Usage](#-usage) • [Configuration](#-configuration)

</div>

---

## 📸 Preview

                        ____  _      _                     1.0.0
                       |  _ \| | ___| |__   ___  _ __
                       | | | | |/ _ \ '_ \ / _ \| '_ \
                       | |_| | |  __/ |_) | (_) | | | |
                       |____/|_|\___|_.__/ \___/|_| |_|

                           Discord Message Cleaner
                                  Beatsbyluca*Light blue → white gradient console output using `pystyle`.*

---

## 🚀 Installation

### Prerequisites

- Python **3.10+**
- Discord **user account token** (self-bot – against ToS, see [Disclaimer](#-disclaimer))
- Git (optional, for cloning)

### Quick Start

# Clone the repository
git clone https://github.com/beatsbyluca/Discord-Message-Cleaner
cd Discord-Message-Cleaner

# Install dependencies
py -m pip install -U discord.py-self pystyle

# Configure your token (see below), then run
py main.py### Dependencies

discord.py-self
pystyle---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🧹 **Clear Channel** | `!clear` deletes **all your own messages** in the current channel (DM or server) |
| 📡 **Ping** | `!ping` shows latency (e.g. `Pong! (42 ms)`) |
| 🗣️ **Say** | `!say <text>` makes your account repeat the given text |
| 🎨 **Pystyle Logs** | Colored console output (light blue → white) for each deleted message |
| ⏱️ **Mini Delay** | Small async delay between deletions to reduce rate limits |

---

## 📖 Usage

1. **Configure the bot**

   - Edit `config.json` and add your user token and preferred prefix (see [Configuration](#-configuration)).

2. **Start the cleaner**

  
   py main.py
      You should see a styled login line such as:

  
   Logged on as YourName#0000 (ID: 123456789012345678)
   3. **Run commands in Discord**

   From your **own account**, in any channel:

   - Clear all your own messages in the current channel:

    
     !clear
          The script will:

     - Walk through the channel history
     - Delete only messages authored by **you**
     - Print a light-blue/white log line in the console for each delete, e.g.:

      
       [CLEAR] Deleted message 5 (ID: 123456789012345678) in channel 123456789012345678
            - Send a success message in the channel:

      
       ✅ Successfully cleared `X` messages with user <@YOUR_ID>
          - Ping:

    
     !ping
        - Say:

    
     !say Hello world
     ---

## ⚙️ Configuration

All settings are stored in `config.json`:

{
  "token": "YOUR_USER_TOKEN_HERE",
  "target_user_id": 0,
  "command_prefix": "!"
}- `token` – **Your Discord user account token**  
  - Never commit or share this.
- `command_prefix` – Prefix for commands (`!`, `.`, `?`, …).  
  - Example: `"command_prefix": "."` → `.clear`, `.ping`, `.say`.
- `target_user_id` – Currently unused; can stay `0` (reserved for future features).

> Tip: Consider putting `config.json` into your local `.gitignore` so it never gets pushed.

---

## 🛠 How It Works

- Uses `discord.py-self`’s `discord.Client` with your **user token**.
- Listens to `on_message` and only reacts when:
  - The author is **you**.
  - The content starts with the chosen `command_prefix`.
- Simple parser splits your message into `command` + `args`.
- For `!clear`, it:
  - Iterates `message.channel.history()` from newest to oldest.
  - Deletes only messages where `msg.author.id == self.user.id`.
  - Waits a short `asyncio.sleep` between deletions.
  - Logs each deletion with a light blue → white `pystyle` gradient.

---

## ⚠️ Disclaimer

**This tool is for educational and personal use only.**

- ❗ Automating user accounts (**self-bots**) violates **Discord’s Terms of Service**.
- ❗ Using this script can result in **account termination** or other enforcement.
- ❗ Do **not** use on servers or channels without explicit permission.
- ❗ You are fully responsible for any consequences of using this project.

By using this software, you agree that the author is **not liable** for any damage, bans, or losses resulting from its use.

---

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it under the terms of that license.

---

## 👤 Credits

**Developer:** [Beatsbyluca](https://github.com/beatsbyluca)  
**Repository:** [Discord-Message-Cleaner](https://github.com/beatsbyluca/Discord-Message-Cleaner)  
**Version:** 1.0.0

---

<div align="center">

**⭐ Star this repo if you find it useful!**

[🔗 Open on GitHub](https://github.com/beatsbyluca/Discord-Message-Cleaner)

</div>
