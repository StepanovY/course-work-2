import random
import requests


def load_random_word():
    """
    ф-ция загружает список слов с внешнего ресурса
    и рандомно возвращет одно слово
    """
    response = requests.get('https://jsonkeeper.com/b/ZGTW')
    response_json = response.json()
    return random.choice(response_json)
