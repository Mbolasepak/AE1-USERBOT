# Copyright (C) 2020 AE1™-USERBOT
#
""" Userbot module for getting information about the social media. """

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.follow$")
async def follow(follow):
    """ For .follow command, check if the bot is running.  """
    await follow.edit(
                     f"`FOLLOW @THEALIFHAKER1 ON` \n\n"
                     f"[InstaGram](https://www.instagram.com/thealifhaker1) \n\n"
                     f"[Telegram](t.me/THEALIFHAKER1) \n\n"
                     f"[YouTube](https://www.youtube.com/channel/UCw7qTq7f--Ft2ONNI1cpiVw) \n\n"
                     f"[Paypal](https://www.paypal.me/AEALIFDANIEL2003) \n\n"
                     )    



CMD_HELP.update({
    "follow":
    ".follow\
    \nUsage: Type .follow to provide your follow links."
    })
