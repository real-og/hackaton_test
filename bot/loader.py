from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
import logging
import os


logging.basicConfig(level=logging.WARNING)
BOT_TOKEN = str(os.environ.get('BOT_TOKEN'))
BASE_URL = str(os.environ.get('BASE_URL'))

CURRENCY_CODE ={"USD": 840,
                "EUR": 978,
                'GBP': 826,
                'JPY': 392}

BANK_CODE ={"Национальный банк": 'nbrb',
                "Альфа банк": 'alfabank',
                'Беларусбанк': 'belarusbank',
              }

NUM_BY_MONTH_NAME = {"January": 1,
                     "February": 2,
                     "March": 3,
                     "April": 4,
                     "May": 5,
                     "June": 6,
                     "July": 7,
                     "August": 8,
                     "September": 9,
                     "October": 10,
                     "November": 11,
                     "December": 12,}



NAME_BY_MONTH_NUM = {1: "January",
                     2: "February",
                     3: "March",
                     4: "April",
                     5: "May",
                     6: "June",
                     7: "July",
                     8: "August",
                     9: "September",
                     10: "October",
                     11: "November",
                     12: "December",}
# may be got from API 
AVAILABLE_BANKS = ['Национальный банк', 'Альфа банк', 'Беларусбанк']
AVAILABLE_CURRENCIES = ['USD', 'EUR', 'GBP', 'JPY']

# storage = RedisStorage2(db=2)
storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)