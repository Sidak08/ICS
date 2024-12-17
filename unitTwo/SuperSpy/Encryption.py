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
    except ValueError as ve:
        print(f"An invalid value was provided for automatic encryption key generation: {ve}")
        #prints if an invalid value is provided
        return None
    except Exception as e:
        print(f"An invalid type (non string) was given or a general error occured: {e}")
        #prints if there is an error in the function
        return None

def is_not_a_letter(character: str) -> bool:
    '''
    Checks if a character is a letter
    Parameters:
        character(str) - input character to check
    Returns:
        bool - True if the character is a letter, False otherwise
    '''
    try:
        if len(character) != 1:
            raise ValueError("Input string must be a single character")

        if CAPITAL_LETTERS.find(character) != -1 or LOWERCASE_LETTERS.find(character) != -1:
            return False #returns False if the character is a letter
        return True #returns True if the character is not a letter
    except Exception as e:
        print(f"Error in is_not_a_letter: {e}")
        #prints a generic error

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
        if len(letter) > 1:
            raise ValueError("Input string must be a single character")

        key = int(key) #checks if the key is an integer
        global CAPITAL_LETTERS, LOWERCASE_LETTERS
        if is_not_a_letter(letter) == False:
            if CAPITAL_LETTERS.find(letter) != -1:
                #checks letter for capital letter
                index = CAPITAL_LETTERS.find(letter)
                newIndex = (index + key) % 26 #calculates the new index
                if newIndex < 0:
                    newIndex += 26 #makes the index positive if negative
                return CAPITAL_LETTERS[newIndex] #returns the new letter
            if LOWERCASE_LETTERS.find(letter) != -1:
                #checks letter for lowercase letter
                index = LOWERCASE_LETTERS.find(letter)
                newIndex = (index + key) % 26 #calculates the new index
                if newIndex < 0:
                    newIndex += 26 #makes the index positive if negative
                return LOWERCASE_LETTERS[newIndex]
        return letter
    except ValueError as ve:
        if str(ve) == "Input string must be a single character":
            print(ve)
        else:
            print("Key must be an integer") #prints if a invalid key is provided
        return letter
    except Exception as e:
        print(f"Error in encode: {e}") #prints a generic error
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
        if len(letter) != 1:
            raise ValueError("Input string must be a single character")

        key = int(key)  #checks if the key is an integer
        global CAPITAL_LETTERS, LOWERCASE_LETTERS
        if is_not_a_letter(letter) == False:
            if CAPITAL_LETTERS.find(letter) != -1:
                #checks letter for capital letter
                index = CAPITAL_LETTERS.find(letter)
                newIndex = (index - key) % 26 #calculates the new index
                if newIndex < 0:
                    newIndex += 26 #makes the index positive if negative
                return CAPITAL_LETTERS[newIndex] #returns the new letter
            if LOWERCASE_LETTERS.find(letter) != -1:
                #checks letter for lowercase letter
                index = LOWERCASE_LETTERS.find(letter)
                newIndex = (index - key) % 26 #calculates the new index
                if newIndex < 0:
                    newIndex += 26  #makes the index positive
                return LOWERCASE_LETTERS[newIndex] #returns the new letter
        return letter
    except ValueError as ve:
        if str(ve) == "Input string must be a single character":
            print(ve)
        else:
            print("Key must be an integer") #prints if a invalid key is provided
        return letter
    except Exception as e:
        print(f"Error in decode: {e}") #prints a generic error
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
        key = int(key)  #checks if the key is an integer
        answer = ""
        for i in range(len(sentence)): #loops through the sentence
            answer += encode(sentence[i], key)
            #encodes the character and adds it to the answer
        return answer #returns the encoded string
    except ValueError:
        print("Key must be an integer")
        #prints an error if the key is not an integer
        return ""
    except Exception as e:
        print(f"Error in encoder: {e}")
        #prints an generic error
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
        key = int(key) #checks if the key is an integer
        answer = ""
        for i in range(len(sentence)): #loops through the sentence
            answer += decode(sentence[i], key)
            #encodes the character and adds it to the answer
        return answer
    except ValueError:
        print("Key must be an integer")
        #prints an error if the key is not an integer
        return ""
    except Exception as e:
        print(f"Error in decoder: {e}")
        #prints an generic error
        return ""


if __name__ == "__main__":
    # genEncryptionKey
    print(genEncryptionKey("Hello, World!")) #output: 794
    print(genEncryptionKey("Python3.8")) #output: 295
    print(genEncryptionKey("1234567890")) #output: 0
    print(genEncryptionKey("!@#$%^&*()")) #output: 0
    print(genEncryptionKey("A quick brown fox jumps over the lazy dog."))
    #output: 9637

    # encode
    print(encode("A", 1)) #output: B
    print(encode("z", 1)) #output: a
    print(encode("Z", 1)) #output: A
    print(encode("a", -1)) #output: z
    print(encode("!", 5)) #output: !

    # decode
    print(decode("B", 1)) # output: A
    print(decode("a", 1)) # output: z
    print(decode("A", 1)) # output: Z
    print(decode("z", -1)) # output: a
    print(decode("!", 5)) # output: !

    # encoder
    print(encoder("Hello, World!", 3)) # output: Khoor, Zruog!
    print(encoder("Python3.8", 5)) # output: Udymts3.8
    print(encoder("1234567890", 2)) # output: 1234567890
    print(encoder("!@#$%^&*()", 4)) # output: !@#$%^&*()
    print(encoder("Well, all 2567 spies liked the encrypting program.", 3256))
    # output: Ckrr, grr 2567 yvoky roqkj znk ktixevzotm vxumxgs.

    # decoder
    print(decoder("Khoor, Zruog!", 3)) #output: Hello, World!
    print(decoder("Udymts3.8", 5)) #output: Python3.8
    print(decoder("1234567890", 2)) #output: 1234567890
    print(decoder("!@#$%^&*()", 4)) #output: !@#$%^&*()
    print(decoder("Ckrr, grr 2567 yvoky roqkj znk ktixevzotm vxumxgs.", 3256))
    # output: Well, all 2567 spies liked the encrypting program.

    # is_not_a_letter
    print(is_not_a_letter("a")) # output: False
    print(is_not_a_letter("Z")) # output: False
    print(is_not_a_letter("1")) # output: True
    print(is_not_a_letter("!")) # output: True
    print(is_not_a_letter(" ")) # output: True
