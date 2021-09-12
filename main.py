# В config.py будет храниться Токен и ID администартора
# В Handlers - будут наши обработчики
# В Main.py - будет запускаться сам бот

# Библиотека aiogram - она Асинхронная, пишем в начале: await для сообщений и async def func() для функций
import aiogram
import asyncio  # Для работы с асинхронными функциями

# Импортируем: Класс Bot, Dispatcher - это обработчик и доставщик наших Update(сообщений),
# executor - будет запускать нашего бота
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

# Создаепм поток, где будут обрабатываться все события - обязательно для работы с аснхронной библиотекой
loop = asyncio.get_event_loop()  # Получаем поток.  get_event_loop = получить событий цикл

# Создаем нашего бота, Bot - это класс бота, который мы импортировали
bot = Bot(BOT_TOKEN, parse_mode='HTML')  # parse_mode для форматирования. parse = разбирать
# parse_mode: то есть делать текст: <b> bold </p> - жирным, курсивом и тд

# Создаем наш Dispatcher dp - обработчк и доставщик
# Засовываем в него нашего бота bot и полученный Поток loop
dp = Dispatcher(bot, loop = loop)

if __name__ == '__main__':  # Если запускаем с main.py то выполнять
    from handlers import dp, send_to_admin  # Импортируем Dispatcher из папки handlers.py
                                            # Импортируем функицию send_to_admin из папки handlers.py
    # Теперь запускаем нашего бота:
    executor.start_polling(dp, on_startup=send_to_admin)
    # executor - для запуска. start polling = начать опрос.
    # start_polling - это встроенная функция в aiogram, которая делает запросы get_updates к телеграмм
    # start_polling запоминает ОФСЕТ, она делает все за нас и просто доставляет нам сообщения
    # start_polling сразу засовывает сообщения в Dispatcher
    # dp мы создаем в handlers.py/
    # on_startup = при запуске. При запуске бота, запускать функицю send_to_admin