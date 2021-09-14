import asyncio
import os
import random
import sys
from datetime import datetime

import telethon.utils
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl import functions, types
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

from Config import (
    API_HASH,
    API_ID,
    STRING,
    STRING2,
    STRING3,
    STRING4,
    STRING5,
    STRING6,
    STRING7,
    STRING8,
    STRING9,
    STRING10,
    SUDO,
)
from Utils import HFUK, RAID

a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""


que = {}

SMEX_USERS = []
for x in SUDO:
    SMEX_USERS.append(x)


async def start_MLO():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception:
            pass

    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 2 not Found")
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await wdk.start()
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 3 not Found")
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 4 not Found")
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 5 not Found")
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception:
            pass

    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 6 not Found")
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 7 not Found")
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception:
            pass

    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 8 not Found")
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception:
            pass

    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 9 not Found")
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception:
            pass

    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 10 not Found")
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(start_MLO())


async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass


@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        MLO = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = MLO[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        MLO = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = MLO[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bleave"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.bleave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        MLO = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = MLO[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bspam <count> <message to spam>\n\n.bspam <count> <reply to a message>\n\nCount must be a integer."
    error = (
        "bspam Module can only be used till 100 count. For bigger spams use Bigbspam."
    )
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        MLO = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(MLO) == 2:
            message = str(MLO[1])
            counter = int(MLO[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(MLO[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(MLO[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.delaybspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.delaybspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.delaybspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.delaybspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.delaybspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.delaybspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.delaybspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.delaybspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.delaybspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.delaybspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delaybspam <sleep time> <count> <message to spam>\n\n.delaybspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        MLO = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Professorsexy = MLO[1:]
        if len(Professorsexy) == 2:
            message = str(Professorsexy[1])
            counter = int(Professorsexy[0])
            sleeptime = float(MLO[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Professorsexy[0])
            sleeptime = float(MLO[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Professorsexy[0])
            sleeptime = float(MLO[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bigbspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigbspam <count> <message to spam>\n\n.bigbspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        MLO = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(MLO) == 2:
            message = str(MLO[1])
            counter = int(MLO[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:
            counter = int(MLO[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(MLO[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.fuk"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝐅𝐮𝐤\n\nCommand:\n\n.fuk <count> <Username of User>\n\n.fuk <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Lallan = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(Lallan) == 2:
            message = str(Lallan[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(Lallan[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(Lallan[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(HFUK)),
            reply_to=event.message.id,
        )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.hardcore"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.hardcore"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.hardcore"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.hardcore"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.hardcore"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.hardcore"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.hardcore"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.hardcore"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.hardcore"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.hardcore"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝐇𝐚𝐫𝐝𝐜𝐨𝐫𝐞\n\nCommand:\n\n.hardcore <Username of User>\n\n.hardcore <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        MLO = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 11:
            message = str(MLO[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Hardcore Mode"
            await e.reply(text, parse_mode=None, link_preview=None)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Hardcore Mode"
            await e.reply(text, parse_mode=None, link_preview=None)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.dhardcore"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dhardcore"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dhardcore"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dhardcore"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dhardcore"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dhardcore"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dhardcore"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dhardcore"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dhardcore"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dhardcore"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝐇𝐚𝐫𝐝𝐜𝐨𝐫𝐞\n\nCommand:\n\n.dhardcore <Username of User>\n\n.dhardcore <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        MLO = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 12:
            message = str(MLO[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            text = "De-Activated Hardcore Mode"
            await e.reply(text, parse_mode=None, link_preview=None)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            text = "De-Activated Hardcore Mode"
            await e.reply(text, parse_mode=None, link_preview=None)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bot"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Wait!"
        event = await e.reply(text, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit(
            f"𝑩𝑶𝑶𝑴 𝑩𝑶𝑶𝑴 ✋\n❌𝑱𝑰𝑵𝑫𝑨 𝑯𝑼 𝑩𝑶𝑺𝑺❌\n𝑲𝑰𝑺𝑲𝑰 𝑴𝑨𝑨 𝑿𝑯𝑶𝑫𝑼?\n\n`{ms}` 𝗺𝘀\n\n🔥 @MLO_EMPIRE 🔥\n🔥 @RAIDERS_FIGHTER🔥 "
        )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.reboot"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝑹𝒆𝒃𝒐𝒐𝒕𝒆𝒅\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await idk.disconnect()
        except Exception:
            pass
        try:
            await ydk.disconnect()
        except Exception:
            pass
        try:
            await wdk.disconnect()
        except Exception:
            pass
        try:
            await hdk.disconnect()
        except Exception:
            pass
        try:
            await sdk.disconnect()
        except Exception:
            pass
        try:
            await adk.disconnect()
        except Exception:
            pass
        try:
            await bdk.disconnect()
        except Exception:
            pass
        try:
            await cdk.disconnect()
        except Exception:
            pass
        try:
            await ddk.disconnect()
        except Exception:
            pass
        try:
            await edk.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
        text = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bot\n.reboot\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.join\n.pjoin\n.bleave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bspam\n.delaybspam\n.bigbspam\n.fuk\n.hardcore\n.dhardcore\n\n\nFor more help regarding usage of plugins type plugins name"
        await e.reply(text, parse_mode=None, link_preview=None)


text = """
 ███╗░░░███╗██╗░░░░░░█████╗░
████╗░████║██║░░░░░██╔══██╗
██╔████╔██║██║░░░░░██║░░██║
██║╚██╔╝██║██║░░░░░██║░░██║
██║░╚═╝░██║███████╗╚█████╔╝
╚═╝░░░░░╚═╝╚══════╝░╚════╝░"""

print(text)
print("")
print("BHOSHDIKO CHAL GYA H BOT AB JAKE SPAM ME GAAND MARAO KAHI.........")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception:
        pass
    try:
        ydk.disconnect()
    except Exception:
        pass
    try:
        wdk.disconnect()
    except Exception:
        pass
    try:
        hdk.disconnect()
    except Exception:
        pass
    try:
        sdk.disconnect()
    except Exception:
        pass
    try:
        adk.disconnect()
    except Exception:
        pass
    try:
        bdk.disconnect()
    except Exception:
        pass
    try:
        cdk.disconnect()
    except Exception:
        pass
    try:
        edk.disconnect()
    except Exception:
        pass
    try:
        ddk.disconnect()
    except Exception:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception:
        pass
    try:
        adk.run_until_disconnected()
    except Exception:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception:
        pass
    try:
        edk.run_until_disconnected()
    except Exception:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception:
        pass
