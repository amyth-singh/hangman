import random

word_list = ["apple", "plum", "banana", "kiwi", "pineapple"]

class Hangman:

  def __init__(self, word_list, num_lives=5):

    self.word_list = word_list
    self.num_lives = num_lives
    self.word = random.choice(word_list)
    self.word_guessed = ["_"]*len(self.word)
    self.num_letters = len(list(set(self.word)))
    self.list_of_guesses = []

  def check_guess(self, guess):
    guess.lower()
    if guess in self.word:
      print(f"Good guess! {guess} is in the word.")
      for i in range(len(self.word)):
        if self.word[i] == guess:
          self.word_guessed[i]=guess
        self.num_letters -= 1
      print(self.word_guessed)
    self.list_of_guesses.append(guess)    

  def ask_for_input(self):
    while True:
      guess = input("Guess a letter :")
      if guess.isalpha() == False or len(guess) != 1:
        print("Invalid letter. Please enter a single alphabetical character.")
      elif guess in self.list_of_guesses:
        print("You already tried that letter!")
      else:
        self.check_guess(guess)
        break

hangman_game = Hangman(["apple", "plum"])
print(hangman_game.ask_for_input())