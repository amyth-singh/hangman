# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# milestone_2.py
This .py file begins with importing the python module 'random' to surface a random word from the user defined variable 'word_list', the random module is actioned as 'word' using the 'random.choice' feature. 
Next, the user is prompted to provide an alphabetical input which is stored under the user defined variable 'guess'.
Finally, the variable 'input' uses the 'if statement' to accept only a single alphabet as an input

# milestone_3.py
milestone_3.py consolidates all the code from milestone_2.py, wraps all the variables, statements into functions, two functions were defined. check_guess and ask_for_input.
check_guess takes all alphabetical arguments and lowers its case, later checks if the argument exists within the word_list.
ask_for_input has a while loop created which if True creates an input variable to get user alphabet input, calls check_guess variable to check if the user input exists within word_list, opens an if statment that checks if the input is alphbetical and has one charecter, else prints the exit loop message and reloops to the top prompting the user for an input. 