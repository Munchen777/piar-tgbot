from aiogram.fsm.state import State, StatesGroup


class TasksCommands(StatesGroup):
    select_action = State()


