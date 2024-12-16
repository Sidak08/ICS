'''
File: EncryptionK.py
Author: Sidak Singh
Date: Dec 14, 2024

Description:
This program receives a sentence and based off the sentence it can dynamically
generate a key, encode a sentence based off a key, decode a sentence based off a key,
'''
#================ Functions ===================
CAPITAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

def genEncryptionKey(sentence: str) -> int:
    '''
    Takes a sentence and returns a key based off the number of capital letters,
    lowercase letters, and special characters in the sentence using this formula
    ((numCapitalLetters * 2 + numLowercaseLetters * 3 + numSpecialCharacters * 4) ** 2)
    + (numCapitalLetters + numLowercaseLetters + numSpecialCharacters)

    Parameters:
        sentence(str) - input string containing the sentence to base the key off of

    Returns:
        key(int) - a dynamically generated key based off the sentence
    '''
    try:
        numCapitalLetters = 0
        numLowercaseLetters = 0
        numSpecialCharacters = 0
        for i in range(len(sentence)):
            if CAPITAL_LETTERS.find(sentence[i]) != -1:
                #checks if the character is a capital letter
                numCapitalLetters += 1
            elif LOWERCASE_LETTERS.find(sentence[i]) != -1:
                #checks if the character is a lowercase letter
                numLowercaseLetters += 1
            elif not is_not_a_letter(sentence[i]):
                #checks if the character is a special letter
                numSpecialCharacters += 1

        return ((numCapitalLetters * 2 + numLowercaseLetters * 3 +
            numSpecialCharacters * 4) ** 2) + (numCapitalLetters +
                numLowercaseLetters + numSpecialCharacters)
            # usses a formula to generate a key based off the number
            # of capital letters, lowercase letters, and special characters
    except Exception as e:
        print(f"Error in genEncryptionKey: {e}")
        #prints if there is a error in the function
        return None

def is_not_a_letter(character: str) -> bool:
    '''
    Checks if a character is a letter
    Parameters:
        character(str) - input character to check
    Returns:
        bool - True if the character is a letter, False otherwise
    '''
    if CAPITAL_LETTERS.find(character) != -1 or LOWERCASE_LETTERS.find(character) != -1:
        return True
    return False #checks if the character is a letter

def encode(letter: str, key: int) -> str:
    '''
    Encodes one character by using Caesar cipher to move the character by key
    Parameters:
        letter(str) - input character to encode
        key(int) - input key to encode the character by
    Returns:
        str - encoded character
    '''
    try:
        global CAPITAL_LETTERS, LOWERCASE_LETTERS
        if is_not_a_letter(letter):
            if CAPITAL_LETTERS.find(letter) != -1:
                #checks letter for capital letter
                index = CAPITAL_LETTERS.find(letter)#finds the index of the letter
                newIndex = (index + key) % 26#calculates the new index
                if newIndex < 0: #check if the index is negative
                    newIndex += 26 #makes the index positive
                return CAPITAL_LETTERS[newIndex] #returns the new letter
            if LOWERCASE_LETTERS.find(letter) != -1:
                #checks letter for lowercase letter
                index = LOWERCASE_LETTERS.find(letter)#finds the index of the letter
                newIndex = (index + key) % 26 #calculates the new index
                if newIndex < 0: #check if the index is negative
                    newIndex += 26 #makes the index positive
                return LOWERCASE_LETTERS[newIndex] #returns the new letter
        return letter
    except Exception as e:
        print(f"Error in encode: {e}") #prints if there is a error in the function
        return letter

def decode(letter: str, key: int) -> str:
    '''
    Decodes one character by using Caesar cipher to move the character by the negative key
    Parameters:
        letter(str) - input character to decode
        key(int) - input key to decode the character by
    Returns:
        str - decoded character
    '''
    try:
        global CAPITAL_LETTERS, LOWERCASE_LETTERS
        if is_not_a_letter(letter):
            if CAPITAL_LETTERS.find(letter) != -1:
                #checks letter for capital letter
                index = CAPITAL_LETTERS.find(letter) #finds the index of the letter
                newIndex = (index - key) % 26 #calculates the new index
                if newIndex < 0: #check if the index is negative
                    newIndex += 26 #makes the index positive
                return CAPITAL_LETTERS[newIndex] #returns the new letter
            if LOWERCASE_LETTERS.find(letter) != -1:
                #checks letter for lowercase letter
                index = LOWERCASE_LETTERS.find(letter) #finds the index of the letter
                newIndex = (index - key) % 26 #calculates the new index
                if newIndex < 0: #check if the index is negative
                    newIndex += 26  #makes the index positive
                return LOWERCASE_LETTERS[newIndex] #returns the new letter
        return letter
    except Exception as e:
        print(f"Error in decode: {e}")
        return letter

def encoder(sentence: str, key: int) -> str:
    '''
    Encodes a string by using Caesar cipher to move the character by the key
    Parameters:
        sentence(str) - input string to encode
        key(int) - input key to encode the string by
    Returns:
        str - encoded string
    '''
    try:
        answer = "" #initialize the answer
        for i in range(len(sentence)): #loops through the sentence
            answer += encode(sentence[i], key)
            #encodes the character and adds it to the answer
        return answer #returns the encoded string
    except Exception as e:
        print(f"Error in encoder: {e}")
        #prints an a error in the function if present
        return ""

def decoder(sentence: str, key: int) -> str:
    '''
    Decodes a string by using Caesar cipher to move the character by the negative key
    Parameters:
        sentence(str) - input string to decode
        key(int) - input key to decode the string by
    Returns:
        str - decoded string
    '''
    try:
        answer = "" #initialize the answer
        for i in range(len(sentence)): #loops through the sentence
            answer += decode(sentence[i], key)
            #encodes the character and adds it to the answer
        return answer
    except Exception as e:
        print(f"Error in decoder: {e}")
        #prints an a error in the function if present
        return ""

if __name__ == "__main__":
    print(genEncryptionKey("test")) #148
    print(encode("D", -27)) # C
    print(encode("d", -2)) # b
    print(decode("D", -1)) # E
    print(encoder("sidak", 3)) # vlgdn
    print(decoder("vlgdn", 3)) # sidak
    print(is_not_a_letter("a")) # True
