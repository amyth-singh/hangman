import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = (random.choice(word_list))
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(list(set(self.word_guessed)))
        self.list_of_guesses = []
        print(self.word, self.word_guessed)

a = Hangman(["apple", "kiwi"])
