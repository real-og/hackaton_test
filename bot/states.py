from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    choosing_currency = State()
    choosing_bank = State()
    choosing_currency = State()
    choosing_operation = State()
    choosing_date = State()