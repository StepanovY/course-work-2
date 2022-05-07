class BasicWord:
    def __init__(self, word, subword):
        self.word = word
        self.subword = subword

    def get_count_words(self):
        count_words = len(self.subword)
        return count_words

    def correct_word(self, user_word):
        if user_word in self.subword:
            return True
        else:
            print('Это слово использовать нельзя')
