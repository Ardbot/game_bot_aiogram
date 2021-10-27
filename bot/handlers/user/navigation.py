from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from bot.machine.driver import forward, back, right, left, up

""" Вызов функций из телеграм """
async def forward_hand(message: types.Message):
    msg = forward()
    await message.answer(message.text + msg)

async def back_hand(message: types.Message):
    msg = back()
    await message.answer(message.text + msg)

async def right_hand(message: types.Message):
    msg = right()
    await message.answer(message.text + msg)

async def left_hand(message: types.Message):
    msg = left()
    await message.answer(message.text + msg)

async def up_hand(message: types.Message):
    msg = up()
    await message.answer(message.text + msg)

    # else:
    #     await message.answer("Команда не распознана! " + position())


def register_handlers_motion(dp: Dispatcher):
    dp.register_message_handler(forward_hand, commands="forward", state="*")
    dp.register_message_handler(forward_hand, Text(equals="Вперед", ignore_case=True), state="*")
    dp.register_message_handler(forward_hand, Text(equals="Вперёд", ignore_case=True), state="*")

    dp.register_message_handler(back_hand, commands="back", state="*")
    dp.register_message_handler(back_hand, Text(equals="Назад", ignore_case=True), state="*")

    dp.register_message_handler(left_hand, commands="left", state="*")
    dp.register_message_handler(left_hand, Text(equals="Влево", ignore_case=True), state="*")

    dp.register_message_handler(right_hand, commands="right", state="*")
    dp.register_message_handler(right_hand, Text(equals="Вправо", ignore_case=True), state="*")

    dp.register_message_handler(up_hand, commands="up", state="*")
    dp.register_message_handler(up_hand, Text(equals="Вверх", ignore_case=True), state="*")


