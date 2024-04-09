from urllib.parse import urlencode
from configuration import app_id


def getting_a_token(app_id):
    """
    Функция получения токена VK
    """
    oauth_base_url = 'https://oauth.vk.com/authorize'
    params = {
        'client_id': app_id,
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'display': 'page',
        'scope': 'status, photos',
        'response_type': 'token',
    }
    oauth_url = f'{oauth_base_url}?{urlencode(params)}'
    print(oauth_url)

if __name__ == '__main__':
    getting_a_token(app_id)