import asyncio

import logging  # Сохраняем логи в файл
from multiprocessing import Process

import requests

import config_bot
from bot.handlers.admin.cmd_admin import register_handlers_admin

from bot.handlers.user.general import register_handlers_general, register_handlers_other
from bot.handlers.user.navigation import register_handlers_motion

logger = logging.getLogger(__name__)

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher, types


async def set_commands(bot: Bot):
    """ Регистрация команд, отображаемых в интерфейсе Telegram """
    commands = [
        BotCommand(command="/forward", description="Вперёд"),
        BotCommand(command="/back", description="Назад"),
        BotCommand(command="/right", description="Вправо"),
        BotCommand(command="/left", description="Влево")
    ]
    await bot.set_my_commands(commands)


async def main():
    """ Настройка логирования в stdout """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    logger.error("Starting bot")

    # # Парсинг файла конфигурации
    # config = load_config("config/bot.ini")

    """ Объявление и инициализация объектов бота и диспетчера """
    bot = Bot(token=config_bot.TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    """ Регистрация хэндлеров """
    register_handlers_general(dp)
    register_handlers_motion(dp)
    register_handlers_admin(dp)

    register_handlers_other(dp)

    """ Установка команд бота """
    await set_commands(bot)

    """ Запуск поллинга """
    # await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    await dp.start_polling()


if __name__ == '__main__':
    Process(target=asyncio.run(main())).start()
