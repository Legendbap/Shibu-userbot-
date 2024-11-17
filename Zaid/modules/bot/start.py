from Zaid import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤͟͟͞͞★**\n**┆◍ ʜᴇʏ, ɪ ᴀᴍ : [ρнσєηιχ ꭙ 𝐔sᴇꝛвσᴛ](https://t.me/DADDY_SAIM) **\n**┆● ρнσєηιχ  Bᴏᴛ Vᴇʀsɪᴏɴ :** `2.1.3`\n**┊● Pᴏᴡᴇʀғᴜʟ & Usᴇғᴜʟ Usᴇʀʙᴏᴛ**\n**╰─────────────────────────**\n**──────────────────────────**\n**❖ Hᴏᴡ Tᴏ Usᴇ Tʜɪs Bᴏᴛ - [Cʟɪᴄᴋ Hᴇʀᴇ](https://t.me/SAIM_WORLD) **\n**──────────────────────────**\n**❖ Sᴇssɪᴏɴs Gᴇɴ Bᴏᴛ ⁚ [Sᴇssɪᴏɴ-Bᴏᴛ](https://t.me/PHOENIX_SESSION_ROBOT) **\n**──────────────────────────**\n**❖ Cʟᴏɴᴇ Bᴏᴛ  ⁚ /clone [ Sᴛʀɪɴɢ Sᴇssɪᴏɴ ]**\n**──────────────────────────**\n**❖ Uᴘᴅᴀᴛᴇ ⏤͟͟͞͞  [❖ ∣ sᴀɪᴍ ᴡᴏʀʟᴅ ∣ ❖](https://t.me/SAIM_WORLD) **\n**──────────────────────────**"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
              [
                  InlineKeyboardButton(text="🍁 sᴇssɪᴏɴ ɢᴇɴ ʙᴏᴛ 🍁️", url="https://t.me/PHOENIX_SESSION_ROBOT"),
              ],
              [
                  InlineKeyboardButton(text="🌿 ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 🌿", url="https://t.me/xyz_own_world"),
              ],
              [
                  InlineKeyboardButton("⌯ ˹𝐀𝐋𝐄𝐗 ♡ 𝐗ᴅ𓆪 ⌯ 🥂 / ‹𝟹 #𝐅ᴜᴄᴋ_𝐓ʜᴇ_𝐇ᴀᴛᴇʀ𝗌 ˼ 🇮🇳", url="https://t.me/LX_FOREVER"),
                  InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ❄️️️", url="https://t.me/SAIM_WORLD"),
              ],
              [
                  InlineKeyboardButton("🦅⃤𓆩𝛅 ⋏ ι 𝚳 <🥀/>𓆩❤️𓆪 ﹛🇨🇦﹜", url="https://t.me/DADDY_SAIM"),
              ],
              ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By ѕαιм  Your motherfucker if uh Don't gives credits.
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("❍ HOW TO USE \n\n𔓕 /clone session \n𔓕 /clone save msg code")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("❖ яυκ jα ϐнοѕ∂κ")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Zaid/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"❖ ѕαιм κο ϐααρ ϐοℓ καя jαα αϐ \n\n❍ [❖ │ ρнσєηιχ ꭙ ʙᴏᴛ │ ❖](https://t.me/DADDY_SAIM)\n\n❖ {user.first_name}")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
