import json
import asyncio
import os
import time
import sys
import logging
import discord
import colorama
from colorama import Fore
from pystyle import Colors, Colorate, Center
from pathlib import Path

colorama.init(autoreset=True)
logging.getLogger("discord").setLevel(logging.CRITICAL)
logging.getLogger("discord.http").setLevel(logging.CRITICAL)
logging.getLogger("discord.gateway").setLevel(logging.CRITICAL)

config = {}
CONFIG_PATH = Path("config.json")
def print_header():
    os.system("cls" if os.name == "nt" else "clear")
    text = """
██████╗ ██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗ 
██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝
██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║
 ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝"""
    
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 80

    lines = text.splitlines()
    max_len = max(len(line) for line in lines)
    
    centered_lines = []
    for line in lines:
        left_padding = (terminal_width - max_len) // 2
        centered_lines.append((" " * left_padding) + line.ljust(max_len))
    
    full_centered_text = "\n".join(centered_lines)
    
    print()
    print(Colorate.Vertical(Colors.cyan_to_green, full_centered_text))
    
    version_text = f"Cleaner v.1.0.1 by Beatsbyluca"
    print(version_text.center(terminal_width))
    print() 

def log(msg, status="info"):
    timestamp = f"{Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}]{Fore.RESET}"
    if status == "info":
        prefix = f"{Fore.CYAN}[INFO]{Fore.RESET}"
    elif status == "success":
        prefix = f"{Fore.GREEN}[SUCCESS]{Fore.RESET}"
    elif status == "error":
        prefix = f"{Fore.RED}[ERROR]{Fore.RESET}"
    elif status == "action":
        prefix = f"{Fore.YELLOW}[ACTION]{Fore.RESET}"
    
    print(f"{timestamp} {prefix} {msg}", flush=True)

def load_config() -> dict:
    if not CONFIG_PATH.exists():
        log("config.json not found!", "error")
        return None
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)

class CleanerClient(discord.Client):
    async def on_ready(self):
        log(f"Logged on as {Fore.WHITE}{self.user}{Fore.RESET}", "success")
        log(f"Prefix: {Fore.YELLOW}{config.get('command_prefix', '!')}{Fore.RESET}", "info")
        log("Ready to clean! Use !clear in any channel.", "info")

    async def on_message(self, message: discord.Message):
        if message.author.id != self.user.id:
            return

        prefix = config.get("command_prefix", "!")
        if not message.content.startswith(prefix):
            return

        cmd_parts = message.content[len(prefix):].strip().split(maxsplit=1)
        command = cmd_parts[0].lower()
        args = cmd_parts[1] if len(cmd_parts) > 1 else ""

        if command == "clear":
            log(f"Starting clear in channel: {Fore.CYAN}{message.channel.id}{Fore.RESET}", "action")
            deleted = 0
            async for msg in message.channel.history(limit=None, oldest_first=False):
                if msg.author.id == self.user.id:
                    try:
                        await msg.delete()
                        deleted += 1
                        if deleted % 5 == 0:
                            log(f"Deleted {deleted} messages...", "info")
                        await asyncio.sleep(0.4)
                    except:
                        continue
            
            log(f"Finished! Successfully cleared {deleted} messages.", "success")
            try:
                await message.channel.send(f"✅ Successfully cleared `{deleted}` messages.")
            except:
                pass

        elif command == "ping":
            latency = round(self.latency * 1000)
            log(f"Ping: {latency}ms", "info")
            await message.channel.send(f"🏓 Pong! ({latency}ms)")

async def main():
    print_header()
    global config
    config = load_config()
    
    if config and config.get("token"):
        client = CleanerClient()
        try:
            await client.start(config["token"])
        except Exception as e:
            log(f"Failed to start: {e}", "error")
    else:
        log("Invalid or missing token in config.json", "error")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log("Cleaner terminated.", "info")
    except Exception as e:
        print(f"\n{Fore.RED}Critical Error: {e}")
    
    input("\nPress Enter to exit...")
