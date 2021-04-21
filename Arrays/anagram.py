def anagram(word, test):
    '''
    given two strings, check if they are anagrams, an anagrams is when two
    strings can be written using the exact same letters.
    
    eg. "running is an anagram of unnring",
        "donald trump is an anagram of dodnumptrnla"
    so the ideal is to write a script to check if the two words are anagrams
    '''
    word = word.lower().replace(' ', '')
    test = test.lower().replace(' ', '')
    
    #CASE CHECK
    if len(word) != len(test):
        return False
    for letter in test:
        if letter in word:
            word = word.replace(letter,'', 1)
    if len(word) == 0:
        return True
    return False

    
# there are other ways to solving this, like sorting the two string and checking if they are equal