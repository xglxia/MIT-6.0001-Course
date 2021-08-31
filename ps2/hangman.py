#

print(""" Problem Set 2, hangman.py
        Name: Guoli
        Collaborators: Joshua
        Time spent: 3 days""")
print('--------------------------------')
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

print('------------------------------------------------')

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #secret_word = choose_word(wordlist)
    #letters_guessed = list(input("Please input your guessed letters: "))

    for char in secret_word:
        if char not in letters_guessed:
          return False
    return True
            
    
    
    
#secret_word = "eikprs"
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(is_word_guessed(secret_word, letters_guessed))
      
        



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #letters_guessed = ['_ '] * len(secret_word)
    guessed_letter = ['_ ']*len(secret_word)
    i = 0
    for char in secret_word:
        if char in letters_guessed:
            guessed_letter[i] = char
        i = i + 1
            
    return ''.join(guessed_letter)

#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_guessed_word(secret_word, letters_guessed))




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    copy = string.ascii_lowercase
    copy1 = list(copy)
    copy2 = copy1[:]
    for e in copy2: 
        if e in letters_guessed:
            copy1.remove(e)
    return ''.join(copy1)
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_available_letters(letters_guessed))
            
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #secret_word = 'appl'
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have 6 guesses left.')
    letters_guessed = ''
    i = 6
    warnings = 3
    while i > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        #letters_guessed = ['_ '] * len(secret_word)
        guess = str.lower(input('Please guess a letter: '))
        
        if guess not in 'abcdefghijklmnopqrstuvwxyz':
            warnings = warnings -1
            if warnings >= 0:
                print(f'You have {warnings} warnings left')
                print('Please enter a letter!')
                print("Remaining letters: ",get_available_letters(letters_guessed))
            else:
                i = i -1
                print('You have remaining guesses: ', i)
                print("Remaining letters: ",get_available_letters(letters_guessed))
        elif guess in letters_guessed:  
            print('You have guessed this letter!')
            warnings = warnings -1
            if warnings >= 0:
                print('You have', warnings, 'warnings left')
                print("Remaining letters: ",get_available_letters(letters_guessed))
            else:
                i = i -1
                print('You have remaining guesses: ', i)
                print("Remaining letters: ",get_available_letters(letters_guessed))
            
        elif guess in secret_word:
            print('Good guess!')
            letters_guessed = letters_guessed + guess
            print(get_guessed_word(secret_word, letters_guessed))
            
            #print(letters_guessed)
            print('You have remaining guesses: ', i)
            print("Remaining letters: ",get_available_letters(letters_guessed))
        else:
            letters_guessed = letters_guessed + guess
            if guess in 'aeiou':
                i = i -2
            else:
                i = i -1
            print('Wrong guess!')
            #print(letters_guessed)
            print('You have remaining guesses: ', i)
            print("Reaming letters: " ,get_available_letters(letters_guessed))
        print('--------------------------------------')    
        #guess = guess + input('Please guess a letter: ')
    print(f'the secret word is {secret_word}')      
    print('-------------------------------------------')   
    
    if is_word_guessed(secret_word, letters_guessed) == True:
        print('Congrulations! you won!')
        unique = ''
        for char in secret_word:
            if char not in unique:
                unique = unique + char
                
        total_score = len(unique) * i
        print(f'your total score is {total_score}')
    else:  
         print('You lost the game')

    return None
#secret_word = 'appl'   
#secret_word = choose_word(wordlist)
#hangman(secret_word)
    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    my_word_copy = my_word.replace('_', '')
    i = 0
    if len(my_word) != len(other_word):
        return False
    else:
        for char in my_word_copy:
                if char not in other_word:
                    return False
                else:
                    for i in range(len(my_word)):
                        if my_word[i] == other_word[i] or my_word[i] == '_':
                            i = i + 1
                        else:
                            return False
                    return True
        
#print(match_with_gaps("t_ _ t", "tabs"))      
    
    
    
    




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
   
    load_words()
    L = []
    for e in wordlist:
        if match_with_gaps(my_word, e) == True:
            L.append(e)
    
    if len(L) == 0:
        return "No possible matches"
    else:
        return print(f"Possible matches is in the list: {L}")

                     
#my_word = 'a_ pl_ '
#print(show_possible_matches(my_word))



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have 6 guesses left.')
    letters_guessed = ''
    i = 6
    warnings = 3
    while i > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        #letters_guessed = ['_ '] * len(secret_word)
        guess = str.lower(input('Please guess a letter: '))
        
        if guess not in 'abcdefghijklmnopqrstuvwxyz' and guess != '*':
            warnings = warnings -1
            if warnings >= 0:
                print(f'You have {warnings} warnings left')
                print('Please enter a letter!')
                print("Remaining letters: ",get_available_letters(letters_guessed))
            else:
                i = i -1
                print('You have remaining guesses: ', i)
                print("Remaining letters: ",get_available_letters(letters_guessed))
        elif guess in letters_guessed:  
            print('You have guessed this letter!')
            warnings = warnings -1
            if warnings >= 0:
                print('You have', warnings, 'warnings left')
                print("Remaining letters: ",get_available_letters(letters_guessed))
            else:
                i = i -1
                print('You have remaining guesses: ', i)
                print("Remaining letters: ",get_available_letters(letters_guessed))
            
        elif guess in secret_word:
            print('Good guess!')
            letters_guessed = letters_guessed + guess
            print(get_guessed_word(secret_word, letters_guessed))
            
            #print(letters_guessed)
            print('You have remaining guesses: ', i)
            print("Remaining letters: ",get_available_letters(letters_guessed))
        elif guess == '*' and i > 0:
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            print('You have remaining guesses: ', i)
           # print("Remaining letters: ",get_available_letters(letters_guessed))
            
        
        else:
            letters_guessed = letters_guessed + guess
            if guess in 'aeiou':
                i = i -2
            else:
                i = i -1
            print('Wrong guess!')
            #print(letters_guessed)
            print('You have remaining guesses: ', i)
            print("Reaming letters: " ,get_available_letters(letters_guessed))
        print('--------------------------------------')    
        #guess = guess + input('Please guess a letter: ')
    print(f'the secret word is {secret_word}')      
    print('-------------------------------------------')   
    
    if is_word_guessed(secret_word, letters_guessed) == True:
        print('Congrulations! you won!')
        unique = ''
        for char in secret_word:
            if char not in unique:
                unique = unique + char
                
        total_score = len(unique) * i
        print(f'your total score is {total_score}')
    else:  
         print('You lost the game')

    return  
    
    
    
    
    
    
    
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
     pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#secret_word = choose_word(wordlist)
#hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
#secret_word = 'tactt'
hangman_with_hints(secret_word)
