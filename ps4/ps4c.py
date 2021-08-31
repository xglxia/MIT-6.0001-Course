# Problem Set 4C
# Name: Guoli
# Collaborators:
# Time Spent: x:xx
import random
import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
word_list = load_words('words.txt')
class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = []
        
        #pass #delete this line and replace with your code here
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
        
        #pass #delete this line and replace with your code here

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words
        
        #pass #delete this line and replace with your code here
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #vowels_permutation = input('Permutation: ')
        vowels_permutation = 'eaiuo'
        dict_lower = {}
        dict_upper = {}
        VOWELS_LOWER = 'aeiou'
        VOWELS_UPPER = 'AEIOU'
        CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
        CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
        for i in range(len(CONSONANTS_LOWER)):
            dict_lower[CONSONANTS_LOWER[i]] = CONSONANTS_LOWER[i]
            dict_upper[CONSONANTS_UPPER[i]] = CONSONANTS_UPPER[i]
        
        for j in range(len(vowels_permutation)):
            dict_lower[VOWELS_LOWER[j]] = vowels_permutation[j].lower()
            dict_upper[VOWELS_UPPER[j]] = vowels_permutation[j].upper()
            
        
        return {**dict_lower, **dict_upper}
        #pass #delete this line and replace with your code here
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        vowelsshifted_dict = self.build_transpose_dict(transpose_dict)
        text = self.message_text
        encrp_lst = []
        for word in text.split():
            #print(word)
            encrp_word = ''
            for letter in word:
                #print('letter is:', letter)
                if letter in VOWELS_LOWER or letter in VOWELS_UPPER:
                    letter = vowelsshifted_dict[letter]
                    encrp_word = encrp_word + letter
                else:
                    encrp_word = encrp_word + letter
            encrp_lst.append(encrp_word)
        
        return ' '.join(encrp_lst)
                
                
                
        #pass #delete this line and replace with your code here
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = []
        
        #pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        table = 'abcdefghijklmnopqrstuvwxyz'
        #VOWELS_LOWER = 'aeiou'
        #VOWELS_UPPER = 'AEIOU'
        #CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
        #CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
        permutation_lst = get_permutations('aeiou')
        decrypted_txt = []
        for perm in permutation_lst:
            #print('perm is:', perm)
            perm_dict = self.build_transpose_dict(perm)
            #print(perm_dict)
            perm_decrypted = []
            for word in self.message_text.split():
                #print('Word is:', word)
                decrp_word = ''
                #decrp_letter = []
                for letter in word:
                    #print('letter is:', letter)
                    if letter.lower()  not in table:
                        decrp_letter = letter
                    elif letter in VOWELS_LOWER:
                        for i in range(5):
                             if letter == VOWELS_LOWER[i]:
                                vowel_index = i       
                        decrp_letter = perm_dict[VOWELS_LOWER[vowel_index]]
                    elif letter in VOWELS_UPPER:
                        for i in range(5):
                             if letter == VOWELS_LOWER[i]:
                                vowel_index = i       
                        decrp_letter = perm_dict[VOWELS_UPPER[vowel_index]]
                    else:
                        decrp_letter = letter 
                    #print('decrp letter is:', decrp_letter)
                    decrp_word = decrp_word + ''.join(decrp_letter)
                    #print('decrp word is:', decrp_word)
                    #print()
                if SubMessage(decrp_word).apply_transpose(perm) == word and is_word(word_list,decrp_word)==True:     
                       perm_decrypted.append(decrp_word)
            decrypted_txt.append((perm, ' '.join(perm_decrypted)))
        return random.choice(decrypted_txt)
        
       # pass #delete this line and replace with your code here
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    vowels_permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(vowels_permutation)
    print("Original message:", message.get_message_text(), "Permutation:", vowels_permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
