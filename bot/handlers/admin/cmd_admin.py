import requests
from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import IDFilter, Text
# from loguru import logger
from bot import config_bot
from bot.machine import config_printer
from bot.machine.driver import home, _position
from bot.machine.serial_printer import write_port, open_port, close_port

admin_id = config_bot.ADMIN

async def connected_port_hand(message: types.Message):
    """ Подключение к порту """
    msg = open_port()
    await message.answer(msg)

async def close_port_hand(message: types.Message):
    """ Закрыть порт """
    msg = close_port()
    await message.answer(msg)


async def start_game(message: types.Message):
    """ Старт игры. Подготовка """
    await message.answer("Старт игры. Ожидайте")

    coord = home()  # Домой
    print(data)
    coord = converter(data)     # Конвертируем строку в словарь/ Не работает
    config_printer.XPOS = -20
    config_printer.YPOS = 160
    config_printer.ZPOS = 0
    await message.answer(_position())


async def home_hand(message: types.Message):
    msg = home()
    await message.answer(message.text + msg)


async def console_hand(message: types.Message):
    """ Ввод gcod """
    msg = write_port(message.text)
    await message.answer(msg)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(connected_port_hand, commands="open_port"), IDFilter(user_id=admin_id)
    dp.register_message_handler(close_port_hand, commands="close_port"), IDFilter(user_id=admin_id)

    dp.register_message_handler(start_game, IDFilter(user_id=admin_id), commands="start_game", state="*")

    dp.register_message_handler(home_hand, commands="home", state="*")
    dp.register_message_handler(home_hand, Text(equals="Домой", ignore_case=True), state="*")

    """ Консольные комманды """
    dp.register_message_handler(console_hand, IDFilter(user_id=admin_id))
