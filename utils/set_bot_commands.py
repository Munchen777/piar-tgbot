from typing import Dict, List

from aiogram import Bot


from aiogram.types import (
    BotCommand,
    BotCommandScopeDefault,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeChatAdministrators,
    BotCommandScopeChat,
    BotCommandScopeAllPrivateChats,
)


async def set_commands(bot: Bot):
    await set_all_commands(bot)
    await set_private_commands(bot)


async def set_all_commands(bot: Bot):
    """Выводятся команды доступные везде"""
    COMMON_COMMANDS = {
        "ru": [
            BotCommand(command="start", description="Запуск бота"),
            BotCommand(command="help", description="Помощь"),
            BotCommand(command="report", description="Сообщить о нарушении"),
            # BotCommand(command="catalog", description="Посмотреть все товары в категории"),
        ],
        "en": [
            BotCommand(command="start", description="start bot"),
            BotCommand(command="help", description="help"),
            BotCommand(command="report", description="report about bad behaviour"),
            # BotCommand(command="catalog", description="catalog of products in definite category"),
        ],
    }
    for lang_code, commands in COMMON_COMMANDS.items():
        return await bot.set_my_commands(
            commands=commands, 
            scope=BotCommandScopeDefault(), 
            language_code=lang_code
        )


async def set_private_commands(bot: Bot):
    """Выводятся команды доступные во всех приватных чатах"""
    PRIVATE_COMMANDS = {
        "ru": [
            BotCommand(command="make_an_order", description="Оставить заявку"),
            BotCommand(command="start", description="Запустить бота"),
            BotCommand(command="catalog", description="Посмотреть все товары в категории"),
        ],
        "en": [
            BotCommand(command="make_an_order", description="leave a request"),
            BotCommand(command="start", description="start bot"),
            BotCommand(command="catalog", description="catalog of products in definite category"),
        ],
    }
    for lang_code, commands in PRIVATE_COMMANDS.items():
        return await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeAllPrivateChats(),
            language_code=lang_code,
        )


async def set_admin_commands(bot: Bot, chat_id: int):
    """Выводятся команды доступные для администраторов чата"""
    ADMIN_COMMANDS: Dict[str, List[BotCommand]] = {
        "ru": [
            BotCommand(command="start_admin", description="Команда старт для админов"),
            BotCommand(command="ro", description="Поставить пользователю режим чтения"),
            BotCommand(command="change_the_price", description="Изменить цену товаров"),
            BotCommand(command="ban", description="Выгнать и забанить нарушителя"),
            BotCommand(command="add_product", description="Добавить новый продукт"),
            BotCommand(command="delete_product", description="Удалить продукт"),
        ],
        "en": [
            BotCommand(command="ro", description="mode read for user"),
            BotCommand(command="start_admin", description="start for admins"),
            BotCommand(command="change_the_price", description="change the price"),
            BotCommand(command="ban", description="ban violator"),
            BotCommand(command="add_product", description="add new product with price or without"),
            BotCommand(command="delete_product", description="delete product from database"),
        ],
    }
    for lang_code, commands in ADMIN_COMMANDS.items():
        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeChatAdministrators(chat_id=chat_id),
            language_code=lang_code,
        )

    # return await bot.set_my_commands([
    #     BotCommand(command='ro', description='read only'),
    #     BotCommand(command="start", description='start for admin'),
    # ],
    #     scope=BotCommandScopeChatAdministrators(chat_id=chat_id)
    # )


# async def set_commands_with
