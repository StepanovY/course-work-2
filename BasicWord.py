class BasicWord:
    def __init__(self, word, subword):
        self.word = word
        self.subword = subword

    def get_count_words(self):
        # count_words = len(self.subword)
        return len(self.subword)


    def correct_word(self, user_word):
        if user_word not in self.subword:
            print('Это слово использовать нельзя')
            return False
        return True
