from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import buttons

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