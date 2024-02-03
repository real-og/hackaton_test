from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
import logging
import os


logging.basicConfig(level=logging.WARNING)
BOT_TOKEN = str(os.environ.get('BOT_TOKEN'))


# may be got from API 
AVAILABLE_BANKS = ['Национальный банк', 'Альфа банк', 'Беларусбанк']
AVAILABLE_CURRENCIES = ['USD', 'EUR', 'GBP', 'JPY']

# storage = RedisStorage2(db=2)
storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)