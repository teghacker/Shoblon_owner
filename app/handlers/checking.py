from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.exceptions import TelegramBadRequest
from config import *
# 1️⃣ Kanal ro'yxati – o'zingizga moslab o'zgartiring
channels_view()


# 2️⃣ Foydalanuvchi qaysi kanallarga obuna bo'lmaganini tekshirish
async def get_missing_channels(bot: Bot, user_id: int) -> list[str]:
    missing = []
    for ch in CHANNELS:
        try:
            member = await bot.get_chat_member(ch, user_id)
            if member.status not in ("member", "administrator", "creator"):
                missing.append(ch)
        except TelegramBadRequest:
            # Kanal topilmasa yoki foydalanuvchi a'zosi bo'lmasa
            missing.append(ch)
    return missing

# 3️⃣ Inline tugmalar yaratish
def subscribe_keyboard(missing: list[str]):
    buttons = [
        [InlineKeyboardButton(text=f"➕ {ch}", url=f"https://t.me/{ch.lstrip('@')}")]
        for ch in missing
    ]
    buttons.append([InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_sub")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
