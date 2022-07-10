from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import dotenv_values

from states import RegistrationStates
from requests_to_api import registration_user, is_user_exist

config = dotenv_values('.env')
bot = Bot(token=config['BOT_TOKEN'])
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.reply('For registration send /registration')


@dp.message_handler(commands=['registration'], state='*')
async def process_registration_command(message: types.Message):
    chat_id = message.chat.id
    resp = await is_user_exist(chat_id)
    if resp['is_exist']:
        await RegistrationStates.successful_registration.set()
        await message.reply("Your account is already registered")
        return
    await RegistrationStates.input_login.set()
    await message.reply('Enter your login:')


@dp.message_handler(state=RegistrationStates.input_login)
async def input_login(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text
    await RegistrationStates.input_password.set()
    await message.reply('Enter your password')


@dp.message_handler(state=RegistrationStates.input_password)
async def input_password(message: types.Message, state: FSMContext):
    # CHECK CORRECT PASSWORD
    async with state.proxy() as data:
        login = data['login']
    password = message.text
    # TRY TO SAVE IN DB

    registration_data = {
        'username': login,
        'password': password,
        'chat_id': message.chat.id,
        'first_name': message.chat.first_name,
        'last_name': message.chat.last_name,
        'tg_username': message.chat.username,
    }
    is_created, errors = await registration_user(registration_data)
    if is_created:
        await RegistrationStates.successful_registration.set()
        await message.reply('Registration is successful')
    else:
        await message.reply('Registration isn\'t successful')
        await bot.send_message(message.chat.id, text=errors)

if __name__ == '__main__':
    executor.start_polling(dp)
