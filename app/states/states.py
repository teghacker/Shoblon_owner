from aiogram.fsm.state import State, StatesGroup


class Admin_state(StatesGroup):
    start = State()
    finish = State()


class Channel_state(StatesGroup):
    start = State()
    finish = State()



