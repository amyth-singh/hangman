from milestone_4 import Hangman

def play_game(word_list, num_lives=5):
    num_lives=5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 or game.num_letters > 0:
            print("Congratulations. You won the game!")
            break

play_game(["apple", "plum"])