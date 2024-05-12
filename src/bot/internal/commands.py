from aiogram import Bot, types

default_commands = [
    types.BotCommand(command='/start', description='начало работы'),
    types.BotCommand(command='/form', description='заполнить анкету'),
    types.BotCommand(command='/about', description='о проекте'),
    types.BotCommand(command='/donate', description='поддержать проект'),
    types.BotCommand(command='/contacts', description='связаться с нами'),
    types.BotCommand(command='/feedback', description='дать фидбэк'),
]


async def set_bot_commands(bot: Bot) -> None:
    await bot.set_my_commands(default_commands)
