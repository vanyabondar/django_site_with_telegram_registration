import aiohttp


REGISTRATION_API_URL = 'http://127.0.0.1:8000/users/api/create/'
CHECK_CHAT_ID_API_URL = 'http://127.0.0.1:8000/users/api/is_exist/'


async def registration_user(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            REGISTRATION_API_URL, data=data
        ) as response:
            if response.status == 201:
                return (True, None)
            else:
                return False, await response.json()


async def is_user_exist(chat_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            CHECK_CHAT_ID_API_URL + str(chat_id)
        ) as response:
            if response.status == 200:
                return await response.json()
            return None
