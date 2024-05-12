from aiogram import Bot, types

default_commands = [
    types.BotCommand(command='/start', description='начало работы'),
    types.BotCommand(command='/about', description='о проекте'),
    types.BotCommand(command='/how_it_works', description='как это работает'),
    types.BotCommand(command='/form', description='заполнить форму'),
    types.BotCommand(command='/contacts', description='контакты'),
    types.BotCommand(command='/feedback', description='оставить обратную связь'),
    types.BotCommand(command='/donate', description='поддержать проект'),
]


async def set_bot_commands(bot: Bot) -> None:
    await bot.set_my_commands(default_commands)
