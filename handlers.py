from main import bot, dp  # Импортируем bot и Dispatcher из Main.py

from aiogram.types import Message  # Импортируем из aiogram ТИПЫ: Massage

from config import admin_id # Импортируем из config - admin_id
# То есть мы будем себе отправлять сообщения

# Для того, что бы при старте бота, мне приходило сообщение, что бот запущен:
async def send_to_admin(dp):  # send_to_admin = отправить админу. Передаем в функицю Dispatcher
    # bot - бот имеет методы, те которые были в API , в том числе send_message
    await bot.send_message(chat_id=admin_id, text='Бот запущен')  # send_message = Отправить сообщение
    # Мы через адрусную строку вводили запрос к телеграмм боту:
    # https://api.telegram.org/bot1952558821:AAF-KrzKcCD87VmUofafrZkzGHaw7fp2ZpY/sendMessage?chat_id=109422760&text=HelloWorld
    # Теперь запустим эту функицю в Main

# Создадим функицю, которая будет реагировать на наши сообщения
# Создадим декоратор, который будет нам отправлять сообщения
# Наш декоратор @dp.message_handler() изменяет функицию echo() и передает параметры: message
@dp.message_handler()  # Она будет нам в нижнюю функцию доставлять сообщения
async def echo(message: Message):  # Message импортировали из aiogram.types
    # Текст, который мы хотим отправить:
    text = f'Привет, ты написал: {message.text}'
    # Отвечаем сообщением нашему пользователю:
 #    await bot.send_message(chat_id=message.from_user.id,
  #                          text=text)
    await message.answer(text=text)  # Это тоже самое, что и выше. answer = отвечать.
    # Бот ответит на наше сообщение

    from pars import poisk
    poisk(message.text)

    from pars import news
    for x in news:
        await message.answer(text=x)