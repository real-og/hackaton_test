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
    return f"some data from api {bank} {currency}"

def generate_rate_by_day(day, month, year):
    return f"day{day} month {month} year {year}"