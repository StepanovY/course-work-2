class Player:

    def __init__(self, user_name):
        self.user_name = user_name
        self.user_subwords = []

    def get_count_user_words(self):
        """
        возвращает длину списка списка возможных слов
        :return: count_user_words
        """
        count_user_words = len(self.user_subwords)
        return count_user_words

    def get_user_subwords(self, user_word):
        """
        добавляет в список использованных слов введенное слово
        :param user_word: слово от пользователя
        :return: user_subwords
        """
        self.user_subwords.append(user_word)
        return self.user_subwords

    def correct_user_subwords(self, user_word):
        """
        проверка на повтор введенного слова
        :param user_word:
        :return:
        """
        if user_word in self.user_subwords:
            print(f'Слово {user_word.upper()} уже было')
            return False
        return True
