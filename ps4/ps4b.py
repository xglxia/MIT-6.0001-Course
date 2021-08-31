# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

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

word_list = load_words('words.txt')
print('fumily:', is_word(word_list, 'fumily'))
def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.text = text
        self.valid_words =[]
        
        #pass #delete this line and replace with your code here

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        
        return self.text
        #pass #delete this line and replace with your code here

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        word_list = load_words('words.txt')
        context = self.get_message_text()
        list_context = context.split()
        list_update = []
        for word in list_context:
            #print(word)
            if is_word(word_list, word) == True:
                list_update.append(word)
        
        self.valid_words = list_update
        
        return self.valid_words
    
        
         #delete this line and replace with your code here


    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
                 
        '''
        dict1 = {}
        dict2 = {}
        table1 = 'abcdefghijklmnopqrstuvwxyz'
        table2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(26):
            dict1[table1[i]] = table1[(i + shift)%26]
            dict2[table2[i]] = table2[(i+shift)%26]
         
            
        return {**dict1, **dict2}
        
        
        #pass #delete this line and replace with your code here

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        tet = self.get_message_text()
        shifted_dict = self.build_shift_dict(shift)
        table = 'abcdefghijklmnopqrstuvwxyz'
        encryed_text = ''
        for letter in tet:
            if letter.lower() in table:
                encryed_letter = shifted_dict[letter]
            else:
                encryed_letter = letter
            encryed_text = encryed_text + encryed_letter
        return encryed_text
            
    
        
        #pass #delete this line and replace with your code here

my_instance_1 = Message('How are you?')
print(my_instance_1.get_message_text())
print(my_instance_1.get_valid_words())
print(my_instance_1.build_shift_dict(4))
print(my_instance_1.apply_shift(4))

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
        
        #pass #delete this line and replace with your code here

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift
        #pass #delete this line and replace with your code here

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        
        return self.encryption_dict
        #pass #delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted
        
        #pass #delete this line and replace with your code here

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        
        '''
        self.shift = shift
        
        
        
        #pass #delete this line and replace with your code here


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        
        
       # pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        table1 = 'abcdefghijklmnopqrstuvwxyz'
        table2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
       # decrypted_list = []
        text_message = self.get_message_text()
        for shift in range(26):
            shifted_dict = self.build_shift_dict(shift)
            decrypted_text = []
            for world in text_message.split():
                
                decrypted_world =''
                for letter in world:
                    if letter.lower() not in table1:
                         decrypted_letter = letter
                    elif letter == letter.lower():
                         for i in range(26):
                             if table1[i]==letter:
                                 letter_index = i
                         decrypted_letter =shifted_dict[table1[letter_index]]
                    elif letter == letter.upper():
                         for i in range(26):
                             if table2[i]==letter:
                                 letter_index = i
                         decrypted_letter = shifted_dict[table2[letter_index]]
                    decrypted_world =decrypted_world + decrypted_letter
                if Message(decrypted_world).apply_shift(26-shift) == world and is_word(word_list,decrypted_world)==True:
                    decrypted_text.append(decrypted_world)
                    print('decrypted text is:', decrypted_text)
            if decrypted_text != []:
                #decrypted_list.append((shift, decrypted_text))
                return (shift, ' '.join(decrypted_text))
            
        return  
                    

        #pass #delete this line and replace with your code here

if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('Lipps')
    print('Expected Output:', (22, 'Hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    
    ciphertext1 = CiphertextMessage('Lipps Asvph!')
    
    print('Actual Output:', ciphertext1.decrypt_message())

    #TODO: best shift value and unencrypted story 
    
    ciphertext2 = CiphertextMessage('Lsa evi csy?')
    print('Actual output:', ciphertext2.decrypt_message() )
    
    pass #delete this line and replace with your code here
