import random

def load_word():
   f = open('spaceman_words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

    # secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    # lettersGuessed: list of letters that have been guessed so far.
    # returns: string, of letters and underscores.  For letters in the word that the user has
    # guessed correctly, the string should contain the letter at the correct position.  For letters
    # in the word that the user has not yet guessed, shown an _ (underscore) instead.

def spaceman(secret_word):
    print('Welcome to Spaceman!\nThe secret word ' + secret_word + ' contains: ' + str(len(secret_word)) + ' letters.')

    letters_guessed = list()
    dashes = "_" * len(secret_word)
    sw_list = list(secret_word)

    guesses = 0
    max_guesses = 7

    while guesses < max_guesses:
        guess = input('Guess A Letter: ').lower()
        letters_guessed.append(guess)
        if guess in sw_list:
            for index, value in enumerate(sw_list):
                if value == guess:
                    #dashes = dashes[:letter_index] + guess + dashes[letter_index + 1:]
                    dashes = dashes[:index] + guess + dashes[index + 1:]
        else:
            print('{} is not in the secret word\nYou have {} guesses left'.format(guess, max_guesses - guesses))
            guesses += 1

        print(letters_guessed)
        print(dashes)

secret_word = load_word()
spaceman(load_word())
