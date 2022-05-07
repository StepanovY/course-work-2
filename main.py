import utils
import BasicWord
import Player

user_name = input('Привет! Давай поиграем в "Угадайку". Как тебя зовут?\n')
flag = True

while flag:
    basic_word = utils.load_random_word()
    words = BasicWord.BasicWord(basic_word['word'], basic_word['subwords'])
    print(f'{user_name} составь  {words.get_count_words()} слов из слова {words.word.upper()}')
    print('Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop" или "стоп"')
    play = Player.Player(user_name)

    for i in range(words.get_count_words()):
        print(f'Напиши {i+1} слово?')
        user_word = input().lower()
        if user_word in ['stop', 'стоп']:
            break
        else:
            if play.correct_user_subwords(user_word):
                if words.correct_word(user_word):
                    print('Такое слово есть, молодец!')
                    play.get_user_subwords(user_word)

    resume = input('Желаете продолжить? (д\н)\n')
    if resume == 'д':
        flag = True
    else:
        flag = False

count_words = play.get_count_user_words()

if 5 <= count_words <= 20 or count_words == 0:
    text = 'слов'
if count_words == 1:
    text = 'слово'
if 2 <= count_words <= 4:
    text = 'слова'

print('Слова закончились, игра завершена!')
print(f'Вы угадали {count_words} {text}!')
