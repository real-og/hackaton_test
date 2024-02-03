from loader import dp, AVAILABLE_CURRENCIES, AVAILABLE_BANKS, NUM_BY_MONTH_NAME, NAME_BY_MONTH_NUM
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import buttons
import logic


@dp.message_handler(state=State.choosing_operation)
async def send_welcome(message: types.Message, state: FSMContext):
    user_input = message.text.strip()
    data = await state.get_data()
    bank = data.get('chosen_bank')
    currency = data.get('chosen_currency')

    if user_input == buttons.choose_another_bank:
        await message.answer(texts.choose_bank, reply_markup=kb.choose_bank_kb)
        await State.choosing_bank.set()
    elif user_input == buttons.choose_another_currency:
        await message.answer(texts.choose_another_currency, reply_markup=kb.choose_currency_kb)
        await State.choosing_currency.set()
    elif user_input == buttons.rate_today:
        await message.answer(texts.generate_today_rate(bank, currency), reply_markup=kb.choose_operation_kb)
    elif user_input == buttons.rate_by_day:
        year, month = logic.get_current_month_and_year()
        month = NUM_BY_MONTH_NAME[month]
        await state.update_data(month=month)
        await state.update_data(year=year)
        await message.answer(texts.choose_date, reply_markup=kb.generate_calendar_kb(month, year))
        await State.choosing_date.set()
    elif user_input == buttons.collect_stats:
        await message.answer(texts.generate_stats(bank, currency), reply_markup=kb.choose_operation_kb)
    else:
        await message.answer(texts.invalid_input)


