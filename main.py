import json
import asyncio
import logging
from pathlib import Path
import discord
from pystyle import Colorate, Colors, Center


CONFIG_PATH = Path("config.json")


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            "config.json was not found. Please put it in the same folder as main.py."
        )

    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        cfg = json.load(f)

    if not cfg.get("token"):
        raise RuntimeError("Missing 'token' entry in config.json.")

    if not cfg.get("command_prefix"):
        cfg["command_prefix"] = "!"

    return cfg


config = load_config()

logging.getLogger("discord").setLevel(logging.CRITICAL)
logging.getLogger("discord.http").setLevel(logging.CRITICAL)
logging.getLogger("discord.gateway").setLevel(logging.CRITICAL)


class MyClient(discord.Client):
    async def on_ready(self):
        text = f"Logged on as {self.user} (ID: {self.user.id})"
        banner = Center.XCenter(Colorate.Horizontal(Colors.blue_to_purple, text, 1))
        print(banner)

    async def on_message(self, message: discord.Message):
        if message.author.id != self.user.id:
            return

        prefix = config.get("command_prefix", "!")
        content = message.content

        if not content.startswith(prefix):
            return

        without_prefix = content[len(prefix) :].strip()
        if not without_prefix:
            return

        parts = without_prefix.split(maxsplit=1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if command == "ping":
            await message.channel.send(f"Pong! ({round(self.latency * 1000)} ms)")
            return

        if command == "say" and args:
            await message.channel.send(args)
            return

        if command == "clear":
            deleted = 0

            async for msg in message.channel.history(limit=None, oldest_first=False):
                if msg.author.id == self.user.id:
                    try:
                        await msg.delete()
                        deleted += 1
                        info = f"[CLEAR] Deleted message {deleted} (ID: {msg.id}) in channel {message.channel.id}"
                        print(Colorate.Horizontal(Colors.cyan_to_white, info, 1))
                        await asyncio.sleep(0.3)
                    except Exception:
                        continue

            await message.channel.send(
                f"✅ Successfully cleared `{deleted}` messages with user <@{self.user.id}>"
            )


if __name__ == "__main__":
    client = MyClient()
    client.run(config["token"])

