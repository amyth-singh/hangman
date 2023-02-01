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