import asyncio
import logging
from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import callback_query, Message, FSInputFile,CallbackQuery
import app.handlers
import app.handlers.admin
import app.handlers.start
from config import *
from bot_instance import bot
import app
from app.handlers.checking import get_missing_channels, subscribe_keyboard

class ForceSubscribeMiddleware:
    async def __call__(self, handler, event, data):
        bot: Bot = data["bot"]
        user = data.get("event_from_user")
        if not user:
            return await handler(event, data)

        # 1️⃣ Qaysi kanallarga foydalanuvchi obuna bo'lmaganini aniqlash
        missing = await get_missing_channels(bot, user.id)

        if missing:  # Faqat yetishmagan kanallar bo'lsa
            text = "Hali barcha kanallarga obuna bo‘lmadingiz:"
            keyboard = subscribe_keyboard(missing)

            try:
                if isinstance(event, Message):
                    await event.answer(text, reply_markup=keyboard)

                elif isinstance(event, CallbackQuery):
                    if (event.message.text != text) or (event.message.reply_markup != keyboard):
                        await event.message.edit_text(text, reply_markup=keyboard)
                    await event.answer("Avval kanallarga obuna bo‘ling!", show_alert=True)

            except Exception as e:
                # Har qanday xatolar uchun fallback
                if isinstance(event, CallbackQuery):
                    await event.answer("Avval kanallarga obuna bo‘ling!", show_alert=True)
                elif isinstance(event, Message):
                    await event.answer(text, reply_markup=keyboard)
                logging.warning(f"ForceSubscribeMiddleware xatolik: {e}")

            return  # handler ishlamaydi, foydalanuvchi faqat obuna qilgunga qadar

        # Agar foydalanuvchi barcha kanallarga obuna bo‘lgan bo‘lsa → handler ishlaydi
        return await handler(event, data)

logging.basicConfig(level=logging.INFO)


async def main():
    dp = Dispatcher()
    dp.message.middleware(ForceSubscribeMiddleware())
    dp.callback_query.middleware(ForceSubscribeMiddleware())
    dp.include_router(app.handlers.start.router)
    dp.include_router(app.handlers.admin.router_admin)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
