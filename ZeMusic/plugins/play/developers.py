import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
  @app.on_message(filters.command(["مودي","المبرمج حمد","مبرمج السورس","مبرمج"],"")

async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/64b768cff9c90461692d5.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𓏺 𝑨꯭𝑩꯭𝑶˹꯭ 𝑺꯭𝑨꯭𝑸꯭𝑹 𝘴͜͡𝘢](https://t.me/O_U_QA)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @O_U_QA ❫
◉ 𝙸𝙳      : ❪ `6189288231` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@O_U_QA) my world (@O_U_Q1 - @O_U_QA) my bro (@O_U_QA) ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𓏺 𝑨꯭𝑩꯭𝑶˹꯭ 𝑺꯭𝑨꯭𝑸꯭𝑹 𝘴͜͡𝘢", url=f"https://t.me/O_U_QA"), 
                 ],[
                   InlineKeyboardButton(
                        "🔱 𓏺 𝑨꯭𝑩꯭𝑶˹꯭ 𝑺꯭𝑨꯭𝑸꯭𝑹 𝘴͜͡𝘢 🔱", url=f"https://t.me/O_U_QA"),
                ],

            ]

        ),

    )
