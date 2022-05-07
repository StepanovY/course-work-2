import json
from random import choice
import requests


def load_random_word():
    """
    ф-ция загружает список слов с внешнего ресурса
    и рандомно возвращет одно слово
    """
    response = requests.get('https://jsonkeeper.com/b/ZGTW')
    response_json = response.json()
    return choice(response_json)


def end_word(count_words):
    if 5 <= count_words <= 20 or count_words == 0:
        return 'слов'
    if count_words == 1:
        return 'слово'
    if 2 <= count_words <= 4:
        return 'слова'


def get_len_word(user_word):
    """
    проверка длины введенного слова
    :param user_word:
    :return:
    """
    if len(user_word) < 3:
        print('Слишком короткое слово')
        return False
    return True
