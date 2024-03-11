from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from config.config import async_session
from config.orm import User, Task
from my_logger import my_logger
from keyboards.reply_keyboard.get_actions import get_actions_keyboard
from states.state_tasks import TasksCommands
from sqlalchemy import select

task_router = Router()


@task_router.message(CommandStart())
async def start_create_task(message: types.Message, state: FSMContext):
    my_logger.info("Сработал хэндлер create_task в модуле check_subscribe.py")
    
    async with async_session() as session:
        query = select(User).filter_by(
            telegram_id = int(message.from_user.id)
        )
        result = await session.execute(query)
        user = result.one_or_none()
        if not user:
            my_logger.info(f"Пользователь {message.from_user.username} пока что не в базе данных.")
            user = User(telegram_id=int(message.from_user.id))
            session.add(user)
            
        await session.commit()
        
        
            
    keyboard = get_actions_keyboard()
    await state.set_state(TasksCommands.select_action)
    await message.answer("Привет! Список доступных команд",
                         reply_markup=keyboard)
    
    
@task_router.message(TasksCommands.select_action)
async def create_task(message: types.Message, state: FSMContext):
    my_logger.info("Сработал хэндлер create_task в модуле check_subscribe.py")
    await state.update_data(telegram_id=message.from_user.id)
    if message.text == "Создать":
        async with async_session() as session:
            query_user = select(User).filter_by(
                telegram_id = int(message.from_user.id)
            )
            # query_old_tasks = select(Task).filter_by(
            #     is_active = True
            # )
            # result = await session.execute(query_old_tasks)
            # old_tasks = result.scalars().fetchmany()
            # print(old_tasks)
            
    
    
    
    