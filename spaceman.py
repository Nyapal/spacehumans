import random

letters_guessed = list()

def load_word():
   f = open('spaceman_words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word


def start_game():
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Spaceman in the command line.

    * At the start of the game, let the user know how many
    letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
    partially guessed word so far, as well as letters that the
    user has not yet guessed.
    '''
    print('Welcome to Spaceman!\n The secret word ' +secret_word+ ' contains: ' + str(len(secret_word)) + ' letters.\n ')


def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

def dashes (secret_word, letters_guessed):
    dashes = list("_" * len(secret_word))


def spaceman(secret_word):
    #start_game()

    wrong_guess = 0
    while wrong_guess < 7:
        guess = input('Guess A Letter: ')
        letters_guessed.append(guess)
        print({}.)
        print(guess)
        wrong_guess += 1
        #
        # #is_word_guessed(secret_word, letters_guessed)
        #
        # if guess in secret_word:
        #     print ('character is in str')
        # else:
        #     print ('character is not in str')
        #     wrong_guess += 1

secret_word = load_word()
spaceman(load_word())
