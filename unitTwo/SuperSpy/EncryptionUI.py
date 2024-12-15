from tkinter import *
from Encryption import encoder, decoder, genEncryptionKey
from FileAccess import load_file, save_to_file
#h
root = Tk()
root.geometry("1200x600")
root.title("Super Spy Program")
root.configure(bg="black")

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

def encryptFile():
    global fileNameEntry, outputFileNameEntry
    phrases = load_file(fileNameEntry.get())
    answer = []
    for i in range(len(phrases)):
        key = get_key(phrases[i])
        if (check_key(key)):
            key = put_key_in_range(key)
            answer.append(encoder(phrases[i], key))
    save_to_file(outputFileNameEntry.get(), answer)

def decryptFile():
    global decryptFileNameEntry, decryptOutputFileNameEntry
    phrases = load_file(decryptFileNameEntry.get())
    answer = []
    for i in range(len(phrases)):
        key = get_key(phrases[i])
        if (check_key(key)):
            key = put_key_in_range(key)
            answer.append(decoder(phrases[i], key))
    save_to_file(decryptOutputFileNameEntry.get(), answer)


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
