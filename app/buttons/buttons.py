from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup , KeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import *
from bot_instance import bot

admin_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Subscribers", callback_data="sub")],
        [InlineKeyboardButton(text="Channels", callback_data="channel")],
        [InlineKeyboardButton(text="Admins", callback_data="admin")],
    ]
)



sahifa = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ma'lumot topish")]
    ],resize_keyboard=True
)