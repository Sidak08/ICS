from tkinter import *
from Encryption import encoder, decoder, is_not_a_letter, genEncryptionKey
from FileAccess import load_file, save_to_file
import time
'''

File: ExpressionLoad.py
Author: Dhenushan Ramesh
Date: Nov 30, 2024

'''

def check_key(encryptKey: int) -> bool:
    if -2000000000 <= encryptKey <= 2000000000:
        return True
    else:
        return False

def get_key(phrase: str) -> int:
    key = phrase[0:11]
    return int(key)

def put_key_in_range(encryptKey: int) -> int:
    while encryptKey < -26 or encryptKey > 26:
        if encryptKey < -26:
            encryptKey += 26
        elif encryptKey > 26:
            encryptKey -= 26
    return int(encryptKey)

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

root = Tk()
root.geometry("1200x600")
root.title("Super Spy Program")
root.configure(bg="black")
phrases = []

titleLabel = Label(root, text="Encrypt Message", width=20, height=1, bg="black", fg="white")
titleLabel.grid(row=0, column=0, padx=10, pady=10)
# titleLabel.config(font=25)–

fileNameLabel = Label(root, text="Enter File Name:", width=20, height=3, bg="black", fg="white")
fileNameLabel.grid(row=1, column=0, padx=10, pady=10)

fileNameEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
fileNameEntry.grid(row=1, column=1, padx=10, pady=10)

def fileNameEntryFunc(event):
    global fileNameEntry, phrases
    fileName = fileNameEntry.get()
    phrases = load_file(fileName)
    answer = []

    for i in range(len(phrases)):
        key = getKey(phrases[i])
        answer.append(encoder(phrases[i], key))
    save_to_file("test", answer)

fileNameEntry.bind("<KeyRelease>", fileNameEntryFunc)

outputFileNameLabel = Label(root, text="Enter Output File Name:", width=20, height=2, bg="black", fg="white")
outputFileNameLabel.grid(row=2, column=0, padx=10, pady=10)

outputFileNameEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
outputFileNameEntry.grid(row=2, column=1, padx=10, pady=10)

encryptionKeyLabel = Label(root, text="Enter Encryption Key:", width=20, height=2, bg="black", fg="white")
encryptionKeyLabel.grid(row=3, column=0, padx=10, pady=10)

encryptionKeyEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
encryptionKeyEntry.grid(row=3, column=1, padx=10, pady=10)

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

decryptEncryptionKeyLabel = Label(root, text="Enter Encryption Key:", width=20, height=2, bg="black", fg="white")
decryptEncryptionKeyLabel.grid(row=8, column=0, padx=10, pady=10)

decryptEncryptionKeyEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
decryptEncryptionKeyEntry.grid(row=8, column=1, padx=10, pady=10)

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

encryption_mode = "auto"

def update_encryption_mode(mode):
    global encryption_mode
    encryption_mode = mode
    messageEntryFunc()

def messageEntryFunc(event=None):
    global messageEntry, encryptedOutputEntry, additionalEncryptionKeyEntry
    key = 0

    if encryption_mode == "manual":
        additionalEncryptionKeyEntry.config(state=NORMAL)
        if additionalEncryptionKeyEntry.get() != "" and check_key(int(additionalEncryptionKeyEntry.get())):
            key = int(additionalEncryptionKeyEntry.get())
            additionalEncryptionKeyEntry.delete(0, END)
            additionalEncryptionKeyEntry.insert(0, str(key))
    elif encryption_mode == "auto":
        key = genEncryptionKey(messageEntry.get())
        additionalEncryptionKeyEntry.config(state=NORMAL)
        additionalEncryptionKeyEntry.delete(0, END)
        additionalEncryptionKeyEntry.insert(0, str(key))
        additionalEncryptionKeyEntry.config(state=DISABLED)

    encryptedOutputEntry.config(state=NORMAL)
    encryptedOutputEntry.delete(0, END)
    encryptedOutputEntry.insert(0, encoder(messageEntry.get(), key))
    encryptedOutputEntry.config(state=DISABLED)

autoGenRadio = Radiobutton(
    root, text="Auto Generate Key", value="auto", bg="black", fg="white",
    command=lambda: update_encryption_mode("auto")
)
autoGenRadio.grid(row=4, column=1, padx=10, pady=10)

manualKeyRadio = Radiobutton(
    root, text="Manual Key Entry", value="manual", bg="black", fg="white",
    command=lambda: update_encryption_mode("manual")
)
manualKeyRadio.grid(row=4, column=2, padx=10, pady=10)

autoGenRadio.select()
encryptedOutputEntry.config(state=DISABLED)
additionalEncryptionKeyEntry.config(state=DISABLED)

messageEntry.bind("<KeyRelease>", messageEntryFunc)
additionalEncryptionKeyEntry.bind("<KeyRelease>", messageEntryFunc)

def decryptMessageEntryFunc(e):
    global decryptMessageEntry, decryptEncryptedOutputEntry, decryptAdditionalEncryptionKeyEntry
    key = 0
    if decryptAdditionalEncryptionKeyEntry.get() != "" and check_key(int(decryptAdditionalEncryptionKeyEntry.get())):
        key = int(decryptAdditionalEncryptionKeyEntry.get())
    decryptEncryptedOutputEntry.config(state=NORMAL)
    decryptEncryptedOutputEntry.delete(0, END)
    decryptEncryptedOutputEntry.insert(0, decoder(decryptMessageEntry.get(), key))
    decryptEncryptedOutputEntry.config(state=DISABLED)

decryptEncryptedOutputEntry.config(state=DISABLED)
decryptMessageEntry.bind("<KeyRelease>", decryptMessageEntryFunc)
decryptAdditionalEncryptionKeyEntry.bind("<KeyRelease>", decryptMessageEntryFunc)


# Run the application
root.mainloop()
