#Sidak

CAPITAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

def genEncryptionKey(sentence: str) -> int:
    numCapitalLetters = 0
    numLowercaseLetters = 0
    numSpecialCharacters = 0
    for i in range(len(sentence)):
        if CAPITAL_LETTERS.find(sentence[i]) != -1:
            numCapitalLetters += 1
        elif LOWERCASE_LETTERS.find(sentence[i]) != -1:
            numLowercaseLetters += 1
        elif is_not_a_letter(sentence[i]):
            numSpecialCharacters += 1

    return ((numCapitalLetters * 2 + numLowercaseLetters * 3 + numSpecialCharacters * 4) ** 2) + (numCapitalLetters + numLowercaseLetters + numSpecialCharacters)

def is_not_a_letter(character: str) -> bool:
    if CAPITAL_LETTERS.find(character) != -1 or LOWERCASE_LETTERS.find(character) != -1:
        return False
    return True

def encode(letter:str, key: int)-> str:
    global CAPITAL_LETTERS, LOWERCASE_LETTERS
    if (is_not_a_letter(letter) == False):
        if CAPITAL_LETTERS.find(letter) != -1:
            index = CAPITAL_LETTERS.find(letter)
            newIndex = (index + key) % 26
            return CAPITAL_LETTERS[newIndex]
        if LOWERCASE_LETTERS.find(letter) != -1:
            index = LOWERCASE_LETTERS.find(letter)
            newIndex = (index + key) % 26
            return LOWERCASE_LETTERS[newIndex]
    return letter

def decode (letter: str, key: int)-> str:
    global CAPITAL_LETTERS, LOWERCASE_LETTERS
    if (is_not_a_letter(letter) == False):
        if CAPITAL_LETTERS.find(letter) != -1:
            index = CAPITAL_LETTERS.find(letter)
            newIndex = (index - key) % 26
            return CAPITAL_LETTERS[newIndex]
        if LOWERCASE_LETTERS.find(letter) != -1:
            index = LOWERCASE_LETTERS.find(letter)
            newIndex = (index - key) % 26
            return LOWERCASE_LETTERS[newIndex]
    return letter

def encoder(sentence: str, key: int) -> str:
    answer = ""
    for i in range(len(sentence)):
        answer += encode(sentence[i], key)
    return answer

def decoder(sentence: str, key: int) -> str:
    answer = ""
    for i in range(len(sentence)):
        answer += decode(sentence[i], key)
    return answer

if __name__ == "__main__":
    print(encode("D", -27))
    print(encode("d", -2))
    # print(decode("D", -1))
    # print(encoder("sidak", 3))
    # print(decoder(encoder("sidak", 3), 3))
