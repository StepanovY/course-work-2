import utils
from BasicWord import BasicWord
from Player import Player


def main():
    user_name = input('Привет! Давай поиграем в "Угадайку". Как тебя зовут?\n')
    flag = True
    play = Player(user_name)

    while flag:
        basic_word = utils.load_random_word()
        words = BasicWord(basic_word['word'], basic_word['subwords'])
        print(f'{user_name} составь  {words.get_count_words()} слов из слова {words.word.upper()}')
        print('Слова должны быть не короче 3 букв')
        print('Чтобы закончить игру, угадайте все слова или напишите "stop" или "стоп"')

        for i in range(words.get_count_words()):
            print(f'Напиши {i + 1} слово?')
            user_word = input().lower()
            if user_word in ['stop', 'стоп']:
                break
            else:
                if play.correct_user_subwords(user_word) \
                        and utils.get_len_word(user_word) \
                        and words.correct_word(user_word):
                    print('Такое слово есть, молодец!')
                    play.get_user_subwords(user_word)

        resume = input('Желаете продолжить? (д\н)\n')
        if resume == 'д':
            flag = True
        else:
            flag = False

    count_words = play.get_count_user_words()

    print('Слова закончились, игра завершена!')
    print(f'Вы угадали {count_words} {utils.end_word(count_words)}!')


if __name__ == "__main__":
    main()
