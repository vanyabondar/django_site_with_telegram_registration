from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    input_login = State()
    input_password = State()
    successful_registration = State()
