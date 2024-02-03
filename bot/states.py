from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    choosing_currency = State()
    choosing_bank = State()