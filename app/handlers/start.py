import asyncio
import logging
from aiogram import Bot, Dispatcher, F, Router, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import callback_query, Message, FSInputFile, InputFile, CallbackQuery
from config import *
from app.buttons.buttons import *
from app.states.states import *
from app.db.base import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from bot_instance import bot
from app.handlers.checking import get_missing_channels, subscribe_keyboard


router = Router()



@router.message(CommandStart())
async def star(message: Message, state: FSMContext):
    admin_add2()
    for i in Read_Users():
        if message.from_user.id == i[1]:
            await message.answer(f'''👋 Salom <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
ID : <code>{message.from_user.id}</code>
Username : <code>{message.from_user.username}</code>
Fullname : <code>{message.from_user.full_name}</code>''',parse_mode="HTML",disable_web_page_preview=True, reply_markup=sahifa)
            await message.delete()
            break
    else:
        ADD_Users(message.from_user.id,message.from_user.username)
        await message.answer(f'''👋 Salom <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
ID : <code>{message.from_user.id}</code>
Username : <code>{message.from_user.username}</code>
Fullname : <code>{message.from_user.full_name}</code>''',parse_mode="HTML",disable_web_page_preview=True, reply_markup=sahifa)
        await message.delete()



@router.callback_query(F.data == "check_sub")
async def check_sub(callback: CallbackQuery):
    missing = await get_missing_channels(callback.bot, callback.from_user.id)
    if missing:
        await callback.message.edit_text(
            "Hali barcha kanallarga obuna bo‘lmadingiz:",
            reply_markup=subscribe_keyboard(missing)
        )
        await callback.answer("Avval kanallarga obuna bo‘ling!", show_alert=True)
        return
    print(CHANNELS,123)

    await callback.message.edit_text(
        "Rahmat! Endi botdan foydalanishingiz mumkin.",
        reply_markup=None  # kerak bo'lsa yangi inline tugmalar qo'yishingiz mumkin
    )









