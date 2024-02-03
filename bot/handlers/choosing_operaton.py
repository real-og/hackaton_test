from loader import dp, AVAILABLE_CURRENCIES, AVAILABLE_BANKS
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import buttons


@dp.message_handler(state=State.choosing_operation)
async def send_welcome(message: types.Message, state: FSMContext):
    user_input = message.text.strip()
    if user_input == buttons.choose_another_bank:
        await message.answer(texts.choose_bank, reply_markup=kb.choose_bank_kb)
        await State.choosing_bank.set()
    elif user_input == buttons.choose_another_currency:
        await message.answer(texts.choose_another_currency, reply_markup=kb.choose_currency_kb)
        await State.choosing_currency.set()
    else:
        pass


