from hangman import Hangman
from random import choice


def get_word():
    words = ["Friends", "Parents", "Patients",
             "Python", "Database",
             "Bigdata", "Development"]
    secret = choice(words).lower()
    return secret
replay = True
while replay:
    def play_game():
        play = Hangman(get_word())
        while not play.game_end():
            play.status()
            user_input = input('\nEnter a letter: ').lower()
            if len(user_input) != 1:
                print("Please, enter just a letter")
            elif user_input not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter an alphabet")
            else:
                play.guess(user_input)

        if play.win():
            print()
            print("Great! You got the word right. It was {}".format(play.word))
        else:
            play.status()
            print("\nOoops! You Lost!")
            print("The word was {}".format(play.word))

    def play_again():
        replay = input("\nDo you want to play again? yes or no ").lower()
        if replay == "yes":
            replay = True
        elif replay == "no":
            exit()
        else:
            print("\nPlease enter YES or NO")
            play_again()
        return replay

    if __name__ == "__main__":
        play_game()
        play_again()
