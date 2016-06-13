from hangman import Hangman
from random import choice

def get_word():
    words = ["Friends", "Parents", "Patients",
            "Python", "Database",
             "Bigdata", "Development"]
    secret=choice(words).lower()
    return secret

def play_game():
  play = Hangman(get_word())
  while not play.game_end():
    play.status()
    user_input = raw_input('\nEnter a letter: ').lower()
    if len(user_input)!=1:
      print "Please, enter just a letter"
    elif user_input not in "abcdefghijklmnopqrstuvwxyz":
      print "Please enter an alphabet"
    else:
      play.guess(user_input)

  play.status()
  if play.win():
    print "Awesome! You got the word right, It was '%s'" %(play.word)
  else:
    print "Ooops! You Lost!"
    print "The word was '%s'" %(play.word)

if __name__ == "__main__":
  play_game()

