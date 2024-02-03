import api_interface
from datetime import datetime
from loader import CURRENCY_CODE

def generate_choose_currency(bank_name):
    return f"Ты выбрал банк: <b>{bank_name}</b>. Теперь выбери нужную тебе валюту из списка ниже."

def generate_choose_operation(bank_name, currency_name):
    return f"Выбранная валюта: <b>{currency_name}</b>. Выбранный банк: <b>{bank_name}</b>."

help_mess = " Plain help"

start_mess = """<b>Привет!</b>👋
Чтобы воспользоваться функционалом бота, сперва выбери банк из меню внизу ⤵️"""

choose_bank = 'Выбери банк из меню внизу'
choose_another_currency = 'Выбери другую валюту'


choose_date = 'Выберите дату'

invalid_input = 'Вы ввели что-то не так... Воспользуйтесь ккнопками'

def generate_today_rate(bank, currency):
    currency_code = CURRENCY_CODE[currency]
    rate = api_interface.get_exchange_rate(bank, currency_code, datetime.now().strftime("%Y-%m-%d"))
    return f"На данный момент курс обмена для банка {bank} в валюте {currency} равен \n\n<b>{rate}</b>"

def generate_rate_by_day(day, month, year, bank, currency):
    currency_code = CURRENCY_CODE[currency]
    date = f'{year}-{month}-{day}'
    rate = api_interface.get_exchange_rate(bank, currency_code, f'{year}-{month}-{day}')
    return f"На {date} курс обмена для банка {bank} в валюте {currency} равен \n\n<b>{rate}</b>"

def generate_stats(bank, currency):
    return f"{bank} {currency} stats"