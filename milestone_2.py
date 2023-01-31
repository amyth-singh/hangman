import random

word_list = ["apple", "kiwi", "orange", "guava", "plum"]
word = (random.choice(word_list))
print(word)

guess = input("Enter a single letter: ")

if (len(guess) > 1) or (guess.isnumeric()):
    print("Oops! That is not a valid input")
else:
    print("Good guess!")