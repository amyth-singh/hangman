import random

word_list = ["apple", "kiwi", "orange", "guava", "plum"]
word = (random.choice(word_list))

def check_guess(guess):
  guess.lower()
  if guess in word:
    print(f"Good guess! {guess} is in the word")
  else:
    print(f"Sorry, {guess} is not in the word")

def ask_for_input():
  while True:
    guess = input("Guess a letter: ")
    check_guess(guess)
    if (guess.isalpha() == True) and (len(guess) == 1):
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        break
  return ask_for_input()

ask_for_input()

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.list_of_guesses = list_of_guesses