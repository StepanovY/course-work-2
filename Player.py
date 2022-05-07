class Player:

    def __init__(self, user_name):
        self.user_name = user_name
        self.user_subwords = []

    def get_count_user_words(self):
        count_user_words = len(self.user_subwords)
        return count_user_words

    def get_user_subwords(self, user_word):
        self.user_subwords.append(user_word)
        return self.user_subwords

    def correct_user_subwords(self, user_word):
        if user_word in self.user_subwords:
            print(f'Слово {user_word.upper()} уже было')
            return False
        if len(user_word) < 3:
            print('Слишком короткое слово')
            return False
        else:
            return True
