from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import buttons

choose_bank_kb = ReplyKeyboardMarkup([[buttons.national_bank_btn], [
                                    buttons.alfa_bank_btn, buttons.belarus_bank_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)