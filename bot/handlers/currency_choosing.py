from loader import dp, AVAILABLE_CURRENCIES, AVAILABLE_BANKS
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import buttons


@dp.message_handler(state=State.choosing_currency)
async def send_welcome(message: types.Message, state: FSMContext):
    user_input = message.text.strip()
    if user_input in AVAILABLE_CURRENCIES:
        data = await state.get_data()
        bank_name = data.get('chosen_bank')
        await message.answer(texts.generate_choose_operation(bank_name, user_input), 
                             reply_markup=kb.choose_operation_kb)
        await state.update_data(chosen_currency=user_input)
        await State.choosing_operation.set()
    else:
        await message.answer(texts.invalid_input, reply_markup=kb.choose_currency_kb)
        
