import random           # Import 'random' module from Python

word_list = ["apple", "kiwi", "orange", "guava", "plum"] # Variable with list of items to randamise from
word = (random.choice(word_list)) # 'choice' method applied on variable to randomise

def check_guess(guess):
  guess.lower()
  if guess in word:
    print(f"Good guess! {guess} is in the word")
  else:
    print(f"Sorry, {guess} is not in the word")

def ask_for_input():
  guess = input("Guess a letter: ")
  check_guess(guess)
  while(True):
    if (guess.isalpha() == True) and (len(guess) == 1):
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
    return ask_for_input()

ask_for_input()