"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet, check pinned in @TeleBotHelp"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("   **Welcome To TeleBot ** \n\n"
        "**`Hey! I'm alive. All systems online and functioning normally... ψ(｀∇´)ψ`**\n\n"
                     "` 🔸 Database Status:` **All OK 👌!**\n"
                     f"` 🔹 My Peru Owner:⚜️SeekingLegend⚜️
