""" Общие комманды """
import logging

from aiogram import types, Dispatcher


# Приветствие при нажатии на кнопку старт
async def start(message: types.Message):
    await message.answer("Привет. Я игровой бот для управления 3D принтером. Команды: Вперёд, Назад, Влево, Вправо")
    # bot.send_message(message.chat.id, "Привет. Я игровой бот для управления 3D принтером.")
    await message.answer("Бот приостановлен. Пишите мне в телегу @teh_Ardbot , если хотите поиграть.")
    logging.info(str(message.chat.id) + " /start")

async def cmd_help_me(message: types.Message):
    """ Помощь """
    await message.answer("Чем помочь?\n"
                         "Пользовательское соглашение\n"
                         "Группа бота: @ExchangeYT")

async def other(message: types.Message):
    await message.answer("Я не знаю что это!")

def register_handlers_general(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(cmd_help_me, commands="help", state="*")

    # dp.register_message_handler(my_statistic_hand, Text(equals="Статистика канала", ignore_case=True), state="*")

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(other)