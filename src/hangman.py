from random import choice
board = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


class Hangman:
    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        elif letter in self.guessed_letters or letter in self.missed_letters:
            print "You already guessed that"
        else:
            return False
        return True

    def fill_word(self):
        fill = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                fill += '_ '
            else:
                fill += letter
        return fill

    def status(self):
        print board[len(self.missed_letters)]
        print 'Word: ' + self.fill_word()
        print 'Letters Missed: ',
        for letter in self.missed_letters:
            print letter,
        print
        print 'Letters Guessed: ',
        for letter in self.guessed_letters:
            print letter,
        print

    def win(self):
        if '_' not in self.fill_word():
            return True
        else:
            return False

    def game_end(self):
        return self.win() or (len(self.missed_letters) == 6)
