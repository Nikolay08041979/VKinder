import configparser

from vkbottle import API
from vkbottle.bot import BotLabeler, Message
from keyboards.keyborad import KEYBOARD_START_MENU, KEYBOARD_NEXT_MENU, KEYBOARD_MY_LIST


from .func_vk import get_user_info, search_people, get_sex, get_person_info


labler = BotLabeler()
labler.vbml_ignore_case = True

# Вытакскиваем токены
vk_config = configparser.ConfigParser()
vk_config.read('config.ini')
vk_token = vk_config['vk']['token']
vk_group_id = vk_config['vk']['group_id']
vk_user_token = vk_config['vk']['user_token']


api = API(vk_token)
api_user = API(token=vk_user_token)

#  Функции реакции на чат

@labler.message(text=['start', 'начать', 'привет', 'главное меню',]) # Декоратор, ожидания сообщений из списка
async def bye_handler(message: Message):
    info = await message.get_user() # Узнаем информацию о пользователе

    await message.answer(f'Привет {info.first_name}!', keyboard=KEYBOARD_START_MENU) # Отвечаем пользователю

    pass
    


@labler.message(text=['начать поиск', 'следующий', 'next',]) # Декоратор, ожидания сообщений из списка
async def start_handler(message: Message):
    await message.answer("Сейчас посмотрим, кто у нас есть", keyboard=KEYBOARD_NEXT_MENU) 
    pass


@labler.message(text=['добавить в избранное',])
async def bye_handler(message: Message):
    pass

@labler.message(text=['игнорировать', 'в черный список',])
async def bye_handler(message: Message):
    pass


@labler.message(text=['мой список', 'список избранного',])
async def bye_handler(message: Message):
    pass


@labler.message(text=['пока', 'достаточно',])
async def bye_handler(message: Message):
    pass
