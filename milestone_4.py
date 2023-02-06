import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = (random.choice(word_list))
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(list(set(self.word)))
        self.list_of_guesses = []
    
    def check_guess(guess):
      guess.lower()
      if guess in word:
        print(f"Good guess! {guess} in in the word.")

    def ask_for_input():
      while True:
        guess = input("Guess the letter: ")
        if (guess.isalpha() == False) and (len(guess) > 1):
          print("Invalid letter. Please, enter a single alphabetical character.")
        elif (guess in self.list_of_guesses):
          print("You already tried that letter!.")
        else:
          (guess.isaplha() == True) and (guess not in self.list_of_guesses)
          check_guess()
        ask_for_input()

