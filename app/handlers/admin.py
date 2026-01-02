import asyncio
import logging
from aiogram import Bot, Dispatcher, F, Router, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import callback_query, Message, FSInputFile, InputFile
from config import *
from app.buttons.buttons import *
from app.states.states import *
from app.db.base import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from bot_instance import bot
import pandas as pd
router_admin = Router()


@router_admin.message(Command('admin'),F.from_user.id.in_(admin))
async def star(message: Message, state:FSMContext):
    # admin_add1()
    await message.answer('👤 Admin nima qilmoqchisiz ? ', reply_markup=admin_buttons)
    await message.delete()


'-----------------------------------------------------------------------'


@router_admin.callback_query(F.data == 'sub')
async def star(call: callback_query, state:FSMContext):
    data = {"№": [], "User_Id": [], "Username": []}
    cnt=0
    for i in Read_Users():
        data["№"].append(i[0])
        data["User_Id"].append(i[1])
        data["Username"].append(i[2])
        cnt+=1
    df = pd.DataFrame(data)
    df.to_excel("Subscribers.xlsx", index=False)
    file_path = FSInputFile("Subscribers.xlsx")
    await call.message.answer_document(document=file_path, caption=f'Count : {cnt}')
    await call.message.delete()


'-----------------------------------------------------------------------'


@router_admin.callback_query(F.data == 'admin')
async def star(call: callback_query, state:FSMContext):
    admins = InlineKeyboardBuilder()
    admin_add2()
    for i in admin:
        admins.button(text=f"{(await call.bot.get_chat(i)).username or "NoUsername"}", url=f"tg://user?id={i}")
    admins.button(text=f'➕ ADD admin', callback_data=f"ADD_admin")
    admins.button(text=f'➖ Remove admin', callback_data=f"Remove_admin")
    admins.adjust(1)
    await call.message.answer('👤 Adminlar ', reply_markup=admins.as_markup())
    await state.set_state(Admin_state.start)
    await call.message.delete()



@router_admin.callback_query(F.data, Admin_state.start)
async def star(call: callback_query, state:FSMContext):
    text = call.data
    if text == 'ADD_admin':
        await call.message.answer('Id kiriting : ')
        await state.update_data({'manba':'add'})
        await state.set_state(Admin_state.finish)
        await call.message.delete()
    else:
        await call.message.answer('Id kiriting : ')
        await state.update_data({'manba':'remove'})
        await state.set_state(Admin_state.finish)
        await call.message.delete()


@router_admin.message(F.text, Admin_state.finish)
async def S(message: Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    if data.get('manba') == 'add':
        ADD_Admins(int(text))
        await message.answer_sticker(sticker='CAACAgEAAxkBAAENST9nU6nRQSsmjCO4viJLrCIquE-DpwACnwMAAonfWETOikC8ytx7RTYE')
        await state.clear()
        await message.delete()
        admin_add2()
    else:
        Delete_Admins(int(text))
        await message.answer_sticker(sticker='CAACAgEAAxkBAAENST9nU6nRQSsmjCO4viJLrCIquE-DpwACnwMAAonfWETOikC8ytx7RTYE')
        await state.clear()
        await message.delete()
        admin_add2()

'-----------------------------------------------------------------------'

@router_admin.callback_query(F.data == 'channel')
async def star(call: callback_query, state:FSMContext):
    channels = InlineKeyboardBuilder()
    channels_view()
    for i in CHANNELS:
        channels.button(text=f"{i}", url=f"https://t.me/{i.lstrip('@')}")
    channels.button(text=f'➕ ADD channel', callback_data=f"ADD_channel")
    channels.button(text=f'➖ Remove channel', callback_data=f"Remove_channel")
    channels.adjust(1)
    await call.message.answer('👤 Channels ', reply_markup=channels.as_markup())
    await state.set_state(Channel_state.start)
    await call.message.delete()



@router_admin.callback_query(F.data, Channel_state.start)
async def star(call: callback_query, state:FSMContext):
    text = call.data
    if text == 'ADD_channel':
        await call.message.answer('Channel username kiriting : ')
        await state.update_data({'manba':'add'})
        await state.set_state(Channel_state.finish)
        await call.message.delete()
    else:
        await call.message.answer('Channel username kiriting : ')
        await state.update_data({'manba':'remove'})
        await state.set_state(Channel_state.finish)
        await call.message.delete()


@router_admin.message(F.text, Channel_state.finish)
async def S(message: Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    if data.get('manba') == 'add':
        ADD_Channels(text)
        await message.answer_sticker(sticker='CAACAgEAAxkBAAENST9nU6nRQSsmjCO4viJLrCIquE-DpwACnwMAAonfWETOikC8ytx7RTYE')
        await state.clear()
        await message.delete()
        channels_view()
    else:
        Delete_Channels(text)
        await message.answer_sticker(sticker='CAACAgEAAxkBAAENST9nU6nRQSsmjCO4viJLrCIquE-DpwACnwMAAonfWETOikC8ytx7RTYE')
        await state.clear()
        await message.delete()
        channels_view()

