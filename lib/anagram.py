# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        def sorted_letters(word):
            return sorted(word.lower())

        base_word_sorted = sorted_letters(self.word)
        return [word for word in words if sorted_letters(word) == base_word_sorted]
