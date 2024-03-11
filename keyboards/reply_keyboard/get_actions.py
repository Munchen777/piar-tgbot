from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import KeyboardBuilder
from aiogram.types.keyboard_button import KeyboardButton



def get_actions_keyboard() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    commands = {
        "Создать":"create_task",
        "Добавить":"add_task",
        "Удалить":"delete_task",
        "Посмотреть":"view_task",
    }
    for task, cmd in commands.items():
        builder.add(KeyboardButton(text=task, callback_data=cmd))
        builder.adjust(2)
    
  
    return builder.as_markup()
    
    