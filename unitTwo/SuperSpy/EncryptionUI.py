from tkinter import *
from Encryption import encoder, decoder, genEncryptionKey
from FileAccess import load_file, save_to_file

'''
File: EncryptionUI.py
Author: Dhenushan Ramesh and Sidak Singh
Date: Dec 9, 2024

Description:
This program provides a GUI user interface for encrypting and 
decrypting messages. It allows the users to either manually enter a key for 
encryption/decryption or automatically generate a key based on the input message. 
The program does both encrypting/decrypting files and individual messages.

Function list:
check_key(encryptKey: int) -> bool
    - Checks if the encryption key is within a the range (-2000000000 to 2000000000).
    - parameters needed: encryptKey (int) - the encryption key .
    - return: bool - sends True if the key is proper, False otherwise.

get_key(phrase: str) -> int
    - gets the encryption key from the first 11 characters of the given phrase.
    - parameters needed: phrase (str) - the input string/phrase to get the key from.
    - return: int - the encryption key or 0 in case of an error.

put_key_in_range(encryptKey: int) -> int
    - makes the encryption key between the range of -26 to 26.
    - parameters needed: encryptKey (int) - the key to change.
    - return: int - the new encryption key.

encryptFile()
    - Encrypts the file by reading its info, changing to encyrpted text for each line, and saving the result to a new file.
    - parameters needed: None.
    - return: None.

decryptFile()
    - Decrypts a file by reading its contents, applying decryption to each line, and saving the result to a new file.
    - parameters needed: None.
    - return: None.

updateMode(new_mode: str)
    - Updates the encryption/decryption mode (auto or manual) for live message entry.
    - parameters needed: new_mode (str) - the new mode to set ("auto" or "manual").
    - return: None.

messageEntryFunc(event=None)
    - Handles the encryption of the message entered by the user based on the selected mode (manual or auto).
    - parameters needed: event (optional) - event triggering the function, default is None.
    - return: None.

decryptMessageEntryFunc(event=None)
    - Handles the decryption of the message entered by the user based on the selected mode (manual or auto).
    - parameters needed: event (optional) - event triggering the function, default is None.
    - return: None.

'''

root = Tk()
root.geometry("1000x600")
root.title("Super Spy Program")
root.configure(bg="black")

def check_key(encryptKey: int) -> bool:
    try:
        if -2000000000 <= encryptKey <= 2000000000:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error in check_key: {e}")
        return False

def get_key(phrase: str) -> int:
    try:
        key = phrase[0:11]
        return int(key)
    except ValueError as e:
        print(f"ValueError in get_key: {e}. Unable to change the key to an integer.")
        return 0 
    except Exception as e2:
        print(f"Unexpected error in get_key: {e2}")
        return 0

def put_key_in_range(encryptKey: int) -> int:
    try:
        while encryptKey < -26 or encryptKey > 26:
            if encryptKey < -26:
                encryptKey += 26
            elif encryptKey > 26:
                encryptKey -= 26
        return int(encryptKey)
    except Exception as e:
        print(f"Error in put_key_in_range: {e}")
        return encryptKey 
    

if __name__ == "__main__":
    num = 500
    num2 = put_key_in_range(num)
    print(num2)
    num = 20000000000000
    checker = check_key(num)
    print(checker)
    phrase = ("10203003030Howisyourday")
    key = get_key(phrase)
    print(key)

def encryptFile():
    global fileNameEntry, outputFileNameEntry
    try:
        phrases = load_file(fileNameEntry.get())
    except Exception as e:
        print(f"Problem with loading file: {e}")
        return

    answer = []
    try:
        for i in range(len(phrases)):
            try:
                key = get_key(phrases[i])
                if check_key(key):
                    key = put_key_in_range(key)
                    answer.append(encoder(phrases[i], key))
            except ValueError as e:
                print(f"There was a ValueError during encryption for phrase {i}: {e}")
            except Exception as e2:
                print(f"Unknown error during encryption for phrase {i}: {e2}")
    except Exception as e:
        print(f"Unexpected error when processing the phrases: {e}")
        return
    try:
        save_to_file(outputFileNameEntry.get(), answer)
    except Exception as e:
        print(f"Error saving the prhaes to file file: {e}")


def decryptFile():
    global decryptFileNameEntry, decryptOutputFileNameEntry
    try:
        phrases = load_file(decryptFileNameEntry.get())
    except Exception as e:
        print(f"Problem with loading file: {e}")
        return 

    answer = []
    try:
        for i in range(len(phrases)):
            try:
                key = get_key(phrases[i])
                if check_key(key):
                    key = put_key_in_range(key)
                    answer.append(decoder(phrases[i], key))
            except ValueError as e:
                print(f"There was a ValueError during decryption for phrase {i}: {e}")
            except Exception as e2:
                print(f"Unexpected error during decryption for phrase {i}: {e2}")
    except Exception as e:
        print(f"Unexpected error processing phrases: {e}")
        return

    try:
        save_to_file(decryptOutputFileNameEntry.get(), answer)
    except Exception as e:
        print(f"Error saving phrases to file: {e}")


titleLabel = Label(root, text="Encrypt Message", width=20, height=1, bg="black", fg="white")
titleLabel.grid(row=0, column=0, padx=10, pady=10)
titleLabel.config(font=25)

fileNameLabel = Label(root, text="Enter File Name:", width=20, height=3, bg="black", fg="white")
fileNameLabel.grid(row=1, column=0, padx=10, pady=10)

fileNameEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
fileNameEntry.grid(row=1, column=1, padx=10, pady=10)

outputFileNameLabel = Label(root, text="Enter Output File Name:", width=20, height=2, bg="black", fg="white")
outputFileNameLabel.grid(row=2, column=0, padx=10, pady=10)

outputFileNameEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
outputFileNameEntry.grid(row=2, column=1, padx=10, pady=10)

enterButtonDescript = Label(root, text="When done typing click this ->", width=30, height=2, bg="black", fg="white")
enterButtonDescript.grid(row=3, column=0, padx=10, pady=10)

enterButton = Button(root, text="Done", width=20, bg="#3B3B3B", fg="white", border=0, command=encryptFile)
enterButton.grid(row=3, column=1, padx=10, pady=10)

orLabel = Label(root, text="OR", width=20, height=2, bg="black", fg="white")
orLabel.grid(row=2, column=2, padx=10, pady=10)

messageLabel = Label(root, text="Enter Message:", width=20, height=2, bg="black", fg="white")
messageLabel.grid(row=1, column=3, padx=10, pady=10)

messageEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
messageEntry.grid(row=1, column=4, padx=10, pady=10)

encryptedOutputLabel = Label(root, text="Encrypted Output:", width=20, height=2, bg="black", fg="white")
encryptedOutputLabel.grid(row=2, column=3, padx=10, pady=10)

encryptedOutputEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
encryptedOutputEntry.grid(row=2, column=4, padx=10, pady=10)

additionalEncryptionKeyLabel = Label(root, text="Enter Encryption Key:", width=20, height=2, bg="black", fg="white")
additionalEncryptionKeyLabel.grid(row=3, column=3, padx=10, pady=10)

additionalEncryptionKeyEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
additionalEncryptionKeyEntry.grid(row=3, column=4, padx=10, pady=10)

decryptTitleLabel = Label(root, text="Decrypt Message", width=20, height=1, bg="black", fg="white")
decryptTitleLabel.grid(row=5, column=0, padx=10, pady=10)
decryptTitleLabel.config(font=(25))

decryptFileNameLabel = Label(root, text="Enter File Name:", width=20, height=3, bg="black", fg="white")
decryptFileNameLabel.grid(row=6, column=0, padx=10, pady=10)

decryptFileNameEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
decryptFileNameEntry.grid(row=6, column=1, padx=10, pady=10)

decryptOutputFileNameLabel = Label(root, text="Enter Output File Name:", width=20, height=2, bg="black", fg="white")
decryptOutputFileNameLabel.grid(row=7, column=0, padx=10, pady=10)

decryptOutputFileNameEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
decryptOutputFileNameEntry.grid(row=7, column=1, padx=10, pady=10)

decryptEnterButtonDescript = Label(root, text="When done typing click this ->", width=30, height=2, bg="black", fg="white")
decryptEnterButtonDescript.grid(row=8, column=0, padx=10, pady=10)

decryptEnterButton = Button(root, text="Done", width=20, bg="#3B3B3B", fg="#FFFFFF", border=0, command=decryptFile)
decryptEnterButton.grid(row=8, column=1, padx=10, pady=10)

decryptOrLabel = Label(root, text="OR", width=20, height=2, bg="black", fg="white")
decryptOrLabel.grid(row=7, column=2, padx=10, pady=10)

decryptMessageLabel = Label(root, text="Enter Message:", width=20, height=2, bg="black", fg="white")
decryptMessageLabel.grid(row=6, column=3, padx=10, pady=10)

decryptMessageEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
decryptMessageEntry.grid(row=6, column=4, padx=10, pady=10)

decryptEncryptedOutputLabel = Label(root, text="Decrypted Output:", width=20, height=2, bg="black", fg="white")
decryptEncryptedOutputLabel.grid(row=7, column=3, padx=10, pady=10)

decryptEncryptedOutputEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
decryptEncryptedOutputEntry.grid(row=7, column=4, padx=10, pady=10)

decryptAdditionalEncryptionKeyLabel = Label(root, text="Enter Decryption Key:", width=20, height=2, bg="black", fg="white")
decryptAdditionalEncryptionKeyLabel.grid(row=8, column=3, padx=10, pady=10)

decryptAdditionalEncryptionKeyEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
decryptAdditionalEncryptionKeyEntry.grid(row=8, column=4, padx=10, pady=10)

mode = "auto"

def updateMode(new_mode):
    global mode
    mode = new_mode
    messageEntryFunc()
    decryptMessageEntryFunc()

def messageEntryFunc(event=None):
    global messageEntry, encryptedOutputEntry, additionalEncryptionKeyEntry
    key = 0
    if mode == "manual":
        additionalEncryptionKeyEntry.config(state=NORMAL)
        if additionalEncryptionKeyEntry.get() != "" and check_key(int(additionalEncryptionKeyEntry.get())):
            key = int(additionalEncryptionKeyEntry.get())
            additionalEncryptionKeyEntry.delete(0, END)
            additionalEncryptionKeyEntry.insert(0, str(key))
    elif mode == "auto":
        key = genEncryptionKey(messageEntry.get())
        additionalEncryptionKeyEntry.config(state=NORMAL)
        additionalEncryptionKeyEntry.delete(0, END)
        additionalEncryptionKeyEntry.insert(0, str(key))
        additionalEncryptionKeyEntry.config(state=DISABLED)

    encryptedOutputEntry.config(state=NORMAL)
    encryptedOutputEntry.delete(0, END)
    encryptedOutputEntry.insert(0, encoder(messageEntry.get(), key))
    encryptedOutputEntry.config(state=DISABLED)



def decryptMessageEntryFunc(event=None):
    global decryptMessageEntry, decryptEncryptedOutputEntry, decryptAdditionalEncryptionKeyEntry
    key = 0
    if mode == "manual":
        decryptAdditionalEncryptionKeyEntry.config(state=NORMAL)
        if decryptAdditionalEncryptionKeyEntry.get() != "" and check_key(int(decryptAdditionalEncryptionKeyEntry.get())):
            key = int(decryptAdditionalEncryptionKeyEntry.get())
            decryptAdditionalEncryptionKeyEntry.delete(0, END)
            decryptAdditionalEncryptionKeyEntry.insert(0, str(key))
    elif mode == "auto":
        if decryptMessageEntry.get():
            key = genEncryptionKey(decryptMessageEntry.get())
            decryptAdditionalEncryptionKeyEntry.config(state=NORMAL)
            decryptAdditionalEncryptionKeyEntry.delete(0, END)
            decryptAdditionalEncryptionKeyEntry.insert(0, str(key))
            decryptAdditionalEncryptionKeyEntry.config(state=DISABLED)

    decryptEncryptedOutputEntry.config(state=NORMAL)
    decryptEncryptedOutputEntry.delete(0, END)
    decryptEncryptedOutputEntry.insert(0, decoder(decryptMessageEntry.get(), key))
    decryptEncryptedOutputEntry.config(state=DISABLED)

modeLabel = Label(root, text="Encryption | Decryption mode for live entry",  height=2, bg="black", fg="white")
modeLabel.grid(row=9, column=0, padx=10, pady=10)

autoGenRadio = Radiobutton(
    root, text="Auto Generate Key", value="auto", bg="black", fg="white",
    command=lambda: updateMode("auto")
)
autoGenRadio.grid(row=9, column=1, padx=10, pady=10)

manualKeyRadio = Radiobutton(
    root, text="Manual Key Entry", value="manual", bg="black", fg="white",
    command=lambda: updateMode("manual")
)
manualKeyRadio.grid(row=9, column=2, padx=10, pady=10)

if mode == "auto":
    autoGenRadio.select()
encryptedOutputEntry.config(state=DISABLED)
additionalEncryptionKeyEntry.config(state=DISABLED)
decryptEncryptedOutputEntry.config(state=DISABLED)
decryptAdditionalEncryptionKeyEntry.config(state=DISABLED)

messageEntry.bind("<KeyRelease>", messageEntryFunc)
additionalEncryptionKeyEntry.bind("<KeyRelease>", messageEntryFunc)
decryptMessageEntry.bind("<KeyRelease>", decryptMessageEntryFunc)
decryptAdditionalEncryptionKeyEntry.bind("<KeyRelease>", decryptMessageEntryFunc)

root.mainloop()
