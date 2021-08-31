# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    L = []
    if len(sequence) == 1:
        L.append(sequence)
        return L
    elif len(sequence) > 1:
        equence = sequence[1:]
       # print(equence)
        for e in get_permutations(equence):
            #print(e)
            for i in range(len(e)+1):
                if i == 0:
                    copy = sequence[0] + e
                else:    
                    copy = e[:i] + sequence[0] + e[i:]
                L.append(copy)
   
        return L
                
                #e0 = sequence[0] + e
                #e1 = e[0] + sequence[0] + e[1:]
                #e2 = e[0] + e[1] + sequence[0] + e[2:]
            
        
#print(get_permutations('aeiou')) 
#print(len(get_permutations('family')))   
    
    
    
   # pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
    
   example2_input = 'bc'
   print('Input:', example2_input)
   print('Excepted output:', ['bc', 'cb'])
   print('Actual output:', get_permutations(example2_input))
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

  #  pass #delete this line and replace with your code here

