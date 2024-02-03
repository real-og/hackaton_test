from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import buttons
import logic
from loader import NAME_BY_MONTH_NUM

choose_bank_kb = ReplyKeyboardMarkup([[buttons.national_bank_btn], [
                                    buttons.alfa_bank_btn, buttons.belarus_bank_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

choose_currency_kb = ReplyKeyboardMarkup([[buttons.usd_btn, 
                                       buttons.eur_btn, 
                                       buttons.gbp_btn, 
                                       buttons.jpy_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

choose_operation_kb = ReplyKeyboardMarkup([[buttons.rate_today, buttons.rate_by_day, buttons.collect_stats],
                                           [buttons.choose_another_bank, 
                                            buttons.choose_another_currency]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

def generate_calendar_kb(month, year):
    month_table = logic.create_month_table(int(year), int(month))
    month_table[0].pop(0)
    kb = InlineKeyboardMarkup(row_width=7)
    kb.add(InlineKeyboardButton(text=f"{NAME_BY_MONTH_NUM[int(month)]} {year}", callback_data='invalid'))
    kb.add(InlineKeyboardButton(text="Mon", callback_data='Mon'))

    for row in month_table:
        for day in row:
            kb.insert(InlineKeyboardButton(text=str(day) if str(day) != '0' else ' ', callback_data=str(day)))
    kb.add(InlineKeyboardButton(text="<", callback_data='<'))
    kb.insert(InlineKeyboardButton(text=">", callback_data='>'))
    return kb
    
