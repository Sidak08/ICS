#Sidak

capitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"

def is_not_a_letter(character: str) -> bool:
    if capitalLetters.find(character) != -1 or lowercaseLetters.find(character) != -1:
        return True
    return False

def encode(letter:str, key: int)-> str:
    global capitalLetters, lowercaseLetters
    if (is_not_a_letter == False):
        if capitalLetters.find(letter) != -1:
            index = capitalLetters.find(letter)
            newIndex = (index + key) % 26
            return capitalLetters[newIndex]
        if lowercaseLetters.find(letter) != -1:
            index = lowercaseLetters.find(letter)
            newIndex = (index + key) % 26
            return lowercaseLetters[newIndex]
    return letter

def decode (letter: str, key: int)-> str:
    global capitalLetters, lowercaseLetters
    if (is_not_a_letter == False):
        if capitalLetters.find(letter) != -1:
            index = capitalLetters.find(letter)
            newIndex = (index - key) % 26
            return capitalLetters[newIndex]
        if lowercaseLetters.find(letter) != -1:
            index = lowercaseLetters.find(letter)
            newIndex = (index - key) % 26
            return lowercaseLetters[newIndex]
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
    print(encode("!", 27))
    print(decode("D", 3))
    print(encoder("sidak", 3))
    print(decoder(encoder("sidak", 3), 3))
