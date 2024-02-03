from loader import dp, AVAILABLE_CURRENCIES, AVAILABLE_BANKS
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import buttons
import datetime


@dp.message_handler(state=State.choosing_bank)
async def send_welcome(message: types.Message, state: FSMContext):
    user_input = message.text.strip()
    if user_input in AVAILABLE_BANKS:
        data = await state.get_data()
        currency = data.get('chosen_currency')

        if currency:
            await message.answer(texts.generate_choose_operation(user_input, currency), 
                             reply_markup=kb.choose_operation_kb)
            await State.choosing_operation.set()
        else:
            await message.answer(texts.generate_choose_currency(user_input), 
                                reply_markup=kb.choose_currency_kb)
            await State.choosing_currency.set()

        await state.update_data(chosen_bank=user_input)
    else:
        await message.answer(texts.invalid_input, reply_markup=kb.choose_bank_kb)
        
