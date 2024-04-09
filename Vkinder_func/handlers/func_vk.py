import asyncio
from asyncio import sleep
from datetime import datetime
from vkbottle import API
from typing import Union


#  Функция поиска людей по заданным параметрам
async def search_people(user_api: API, age_from=None, age_to=None, city_id=None, city_title=None, sex_id=0, status=4):

    response = await user_api.users.search(  
        sort=0,  
        city=city_id,
        hometown=city_title,
        sex=sex_id,  
        status=status, 
        age_from=age_from,
        age_to=age_to,
        has_photo=True, 
        count=20, 
        fields=["can_write_private_message", 
                "city", 
                "domain", 
                "home_town"] 
    )
    return response

# Функция вычесления возраста
def get_old(birthday: str) -> Union[int | None]:
    if birthday is None:
        return None
    b_day = birthday.split('.')
    now_day = datetime.now()
    year_today = now_day.date().year
    month_today = now_day.date().month
    day_today = now_day.date().day
    years = year_today - int(b_day[2])
    months = month_today - int(b_day[1])
    if months < 0:
        years -= 1
    if months == 0:
        days = day_today - int(b_day[0])
        if days < 0:
            years -= 1
    return years

# Функция инверсии пола
def get_sex(sex: int) -> int:
    if sex == 2:
        return 1
    elif sex == 1:
        return 2
    else:
        return 0



async def get_user_info(api_user: API, user_id: int) -> object:

    data = {'user_ids': user_id,
              'fields': ['city', 'sex', 'bdate']}
    
    request = await api_user.request('users.get', data=data)
    user = 'имя таблицы в бд'(
        first_name=request.get('response')[0].get('first_name'),
        last_name=request.get('response')[0].get('last_name'),
        vk_id=request.get('response')[0].get('id'),
        city=request.get('response')[0].get('city').get('title'),
        city_id=request.get('response')[0].get('city').get('id'),
        sex_id=request.get('response')[0].get('sex', None),
        age=get_old(request.get('response')[0].get('bdate'))
    )
    return user


async def get_photos(api_user: API, user_id: int) -> list:
    
    data = {'owner_id': user_id, 
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 0,}
    request_photo = await api_user.request('photos.get', data=data)

    photos = sorted(request_photo.get('response').get('items'),
                    key=lambda x: x.get('likes').get('count'),
                    reverse=True)[:3]

    three_photos = ['photo{}_{}'.format(photo.get('owner_id'), photo.get('id')) for photo in photos]
    return three_photos
