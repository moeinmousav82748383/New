from aiogram.fsm.state import State, StatesGroup

class MinesStates(StatesGroup):
    waiting_for_diamonds = State()