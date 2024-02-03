
from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import logic


@dp.callback_query_handler(state=State.choosing_date)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    user_input = callback.data
    data = await state.get_data()
    bank = data.get('chosen_bank')
    currency = data.get('chosen_currency')
    month = data.get('month')
    year = data.get('year')
    if user_input == '<' or user_input == '>':
        inc = 0
        if user_input == '<':
            inc = -1
        else:
            inc = 1
        month, year = logic.get_next_month_year_pair(int(month), int(year), inc)
        await callback.message.edit_reply_markup(reply_markup=kb.generate_calendar_kb(month, year))
        await state.update_data(month=month)
        await state.update_data(year=year)
    if user_input.isdigit():
        await state.update_data(day=user_input)
        await callback.message.delete()
        await callback.message.answer(texts.generate_rate_by_day(user_input, month, year, bank, currency), reply_markup=kb.choose_operation_kb)
        await State.choosing_operation.set()

    await bot.answer_callback_query(callback.id)