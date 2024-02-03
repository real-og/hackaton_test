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


    #         data = await state.get_data()
    #         bank_name = data.get('chosen_bank')
    #         await state.update_data(chosen_currency=user_input)
    #         await message.answer(texts.generate_choose_operation(bank_name, user_input), 
    #                             reply_markup=kb.choose_operation_kb)
    #         await state.update_data(chosen_currency=user_input)
    #         await State.choosing_operation.set()
    # else:
    #     await message.answer(texts.invalid_input, reply_markup=kb.choose_currency_kb)
        