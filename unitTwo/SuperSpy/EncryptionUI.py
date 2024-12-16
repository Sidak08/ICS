from tkinter import *
from Encryption import encoder, decoder, genEncryptionKey
from FileAccess import load_file, save_to_file

'''
File: EncryptionUI.py
Author: Dhenushan Ramesh and Sidak Singh
Date: Dec 9, 2024

Work Contributions:
    Dhenushan Ramesh: Gui Elements, check_key(encryptKey: int), get_key(phrase: str)
    put_key_in_range(encryptKey: int), Commenting, error handling

    Sidak Singh: encryptFile(), decryptFile(), updateMode(newMode: str),
    messageEntryFunc(event=None), decryptMessageEntryFunc(event=None),
    radio buttons, integration of all systems, Program GUI design


Description:
This program provides a GUI user interface for encrypting and
decrypting messages. It allows the users to either manually enter a key for
encryption/decryption or automatically generate a key based on the input message.
The program does both encrypting/decrypting files and individual messages.

Function list:
check_key(encryptKey: int) -> bool
    - Checks if the encryption key is within a the range (-2000000000 to
    2000000000).
    - parameters needed: encryptKey (int) - the encryption key .
    - return: bool - sends True if the key is proper, False otherwise.

get_key(phrase: str) -> int
    - gets the encryption key from the first 11 characters of the given phrase.
    - parameters needed: phrase (str) - the input string/phrase to get the
    key from.
    - return: int - the encryption key or 0 in case of an error.

put_key_in_range(encryptKey: int) -> int
    - makes the encryption key between the range of -26 to 26.
    - parameters needed: encryptKey (int) - the key to change.
    - return: int - the new encryption key.

encryptFile()
    - Encrypts the file by reading its info, changing to encyrpted text for
    each line, and saving the result to a new file. Called by the done button
    - parameters needed: None.
    - return: None.

decryptFile()
    - Decrypts a file by reading its contents, applying decryption to each line,
    and saving the result to a new file. Called by the done button
    - parameters needed: None.
    - return: None.

updateMode(new_mode: str)
    - Updates the encryption/decryption mode (auto or manual)
    for live message entry.
    - parameters needed: newMode (str) - the new mode to set
    "auto" or "manual".
    - return: None.

messageEntryFunc()
    - Handles the encryption of the message entered by the user based on the
    selected mode (manual or auto).
    - parameters needed: None
    - return: None.

decryptMessageEntryFunc()
    - Handles the decryption of the message entered by the user based on
    the selected mode (manual or auto).
    - parameters needed: None.
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


def encryptFile():
    global fileNameEntry, outputFileNameEntry
    try:
        phrases = load_file(fileNameEntry.get())
        #loads the prahe from the file
    except Exception as e:
        print(f"Problem with loading file: {e}")
        #checks if there was error loading the file
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


# Label for Encryption section title
titleLabel = Label(root, text="Encrypt Message", width=20, height=1,
                    bg="black", fg="white")
titleLabel.grid(row=0, column=0, padx=10, pady=10)
# Positioning title in grid layout
titleLabel.config(font=25)  # Setting font size for the title

# Label for file name input
fileNameLabel = Label(root, text="Enter File Name:", width=20, height=3,
                       bg="black", fg="white")
fileNameLabel.grid(row=1, column=0, padx=10, pady=10)
# Positioning label for file name

# Entry widget for the file name
fileNameEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
fileNameEntry.grid(row=1, column=1, padx=10, pady=10)
# Positioning entry box for file name

# Label for output file name input
outputFileNameLabel = Label(root, text="Enter Output File Name:",
                            width=20, height=2, bg="black", fg="white")
outputFileNameLabel.grid(row=2, column=0, padx=10, pady=10)
# Positioning label for output file name

# Entry widget for the output file name
outputFileNameEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
outputFileNameEntry.grid(row=2, column=1, padx=10, pady=10)
# Positioning entry box for output file name

# Description for the button to encrypt the file
enterButtonDescript = Label(root, text="When done typing click this ->",
                            width=30, height=2, bg="black", fg="white")
enterButtonDescript.grid(row=3, column=0, padx=10, pady=10)
# Positioning description label for button

# Button to trigger the encryption process
enterButton = Button(root, text="Done", width=20, bg="#3B3B3B", fg="white",
                      border=0, command=encryptFile)
enterButton.grid(row=3, column=1, padx=10, pady=10)
# Positioning the Done button for encryption

# Label to display "OR" (alternative method for encryption)
orLabel = Label(root, text="OR", width=20, height=2, bg="black", fg="white")
orLabel.grid(row=2, column=2, padx=10, pady=10)
# Positioning OR label in grid layout

# Label for message input in the encryption section
messageLabel = Label(root, text="Enter Message:", width=20, height=2,
                      bg="black", fg="white")
messageLabel.grid(row=1, column=3, padx=10, pady=10)
# Positioning message label for encryption

# Entry widget for the message input in the encryption section
messageEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
messageEntry.grid(row=1, column=4, padx=10, pady=10)
# Positioning entry box for message input

# Label for displaying encrypted output in the encryption section
encryptedOutputLabel = Label(root, text="Encrypted Output:", width=20,
                              height=2, bg="black", fg="white")
encryptedOutputLabel.grid(row=2, column=3, padx=10, pady=10)
# Positioning encrypted output label

# Entry widget for displaying the encrypted output
encryptedOutputEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
encryptedOutputEntry.grid(row=2, column=4, padx=10, pady=10)
# Positioning encrypted output entry

# Label for encryption key input in the encryption section
additionalEncryptionKeyLabel = Label(root, text="Enter Encryption Key:",
                                      width=20, height=2, bg="black", fg="white")
additionalEncryptionKeyLabel.grid(row=3, column=3, padx=10, pady=10)
# Positioning encryption key label

# Entry widget for encryption key input
additionalEncryptionKeyEntry = Entry(root, width=25, bg="#3B3B3B", fg="white",
                                      border=0)
additionalEncryptionKeyEntry.grid(row=3, column=4, padx=10, pady=10)
# Positioning encryption key entry

# Title for the Decryption section
decryptTitleLabel = Label(root, text="Decrypt Message", width=20, height=1,
                           bg="black", fg="white")
decryptTitleLabel.grid(row=5, column=0, padx=10, pady=10)
# Positioning decryption title label
decryptTitleLabel.config(font=(25))  # Setting font for decryption title

# Label for file name input in the decryption section
decryptFileNameLabel = Label(root, text="Enter File Name:", width=20, height=3,
                              bg="black", fg="white")
decryptFileNameLabel.grid(row=6, column=0, padx=10, pady=10)
# Positioning decryption file name label

# Entry widget for the file name input in the decryption section
decryptFileNameEntry = Entry(root, width=25, bg="#3B3B3B", fg="white",
                              border=0)
decryptFileNameEntry.grid(row=6, column=1, padx=10, pady=10)
# Positioning decryption file name entry

# Label for output file name input in the decryption section
decryptOutputFileNameLabel = Label(root, text="Enter Output File Name:",
                                    width=20, height=2, bg="black", fg="white")
decryptOutputFileNameLabel.grid(row=7, column=0, padx=10, pady=10)
# Positioning decryption output file name label

# Entry widget for output file name in the decryption section
decryptOutputFileNameEntry = Entry(root, width=25, bg="#3B3B3B", fg="white",
                                    border=0)
decryptOutputFileNameEntry.grid(row=7, column=1, padx=10, pady=10)
# Positioning decryption output file name entry

# Description for the button to decrypt the file
decryptEnterButtonDescript = Label(root, text="When done typing click this ->",
                                    width=30, height=2, bg="black", fg="white")
decryptEnterButtonDescript.grid(row=8, column=0, padx=10, pady=10)
# Positioning description label for decryption button

# Button to trigger the decryption process
decryptEnterButton = Button(root, text="Done", width=20, bg="#3B3B3B",
                             fg="#FFFFFF", border=0, command=decryptFile)
decryptEnterButton.grid(row=8, column=1, padx=10, pady=10)
# Positioning the Done button for decryption

# Label to display "OR" (alternative method for decryption)
decryptOrLabel = Label(root, text="OR", width=20, height=2, bg="black", fg="white")
decryptOrLabel.grid(row=7, column=2, padx=10, pady=10)
# Positioning OR label for decryption

# Label for message input in the decryption section
decryptMessageLabel = Label(root, text="Enter Message:", width=20, height=2,
                             bg="black", fg="white")
decryptMessageLabel.grid(row=6, column=3, padx=10, pady=10)
# Positioning message label for decryption

# Entry widget for message input in the decryption section
decryptMessageEntry = Entry(root, width=25, bg="#3B3B3B", fg="white", border=0)
decryptMessageEntry.grid(row=6, column=4, padx=10, pady=10)
# Positioning message entry for decryption

# Label for displaying decrypted output
decryptEncryptedOutputLabel = Label(root, text="Decrypted Output:", width=20,
                                     height=2, bg="black", fg="white")
decryptEncryptedOutputLabel.grid(row=7, column=3, padx=10, pady=10)
# Positioning decrypted output label

# Entry widget for displaying decrypted output
decryptEncryptedOutputEntry = Entry(root, width=25, bg="#3B3B3B", fg="white",
                                     border=0)
decryptEncryptedOutputEntry.grid(row=7, column=4, padx=10, pady=10)
# Positioning decrypted output entry

# Label for decryption key input
decryptAdditionalEncryptionKeyLabel = Label(root, text="Enter Decryption Key:",
                                             width=20, height=2, bg="black", fg="white")
decryptAdditionalEncryptionKeyLabel.grid(row=8, column=3, padx=10, pady=10)
# Positioning decryption key label

# Entry widget for the decryption key input
decryptAdditionalEncryptionKeyEntry = Entry(root, width=25, bg="#3B3B3B",
                                             fg="white", border=0)
decryptAdditionalEncryptionKeyEntry.grid(row=8, column=4, padx=10, pady=10)
# Positioning decryption key entry

# Set initial mode to "auto"
mode = "auto"

# Update mode and refresh message and decryption entry functions
def updateMode(new_mode):
    global mode
    mode = new_mode
    messageEntryFunc()
    decryptMessageEntryFunc()

# Handle message entry for encryption
def messageEntryFunc():
    global messageEntry, encryptedOutputEntry, additionalEncryptionKeyEntry
    key = 0

    # Manual mode: user enters a key
    if mode == "manual":
        additionalEncryptionKeyEntry.config(state=NORMAL)
        if additionalEncryptionKeyEntry.get() != "" and check_key(
            int(additionalEncryptionKeyEntry.get())):
            key = int(additionalEncryptionKeyEntry.get())
            additionalEncryptionKeyEntry.delete(0, END)
            additionalEncryptionKeyEntry.insert(0, str(key))

    # Auto mode: generate key automatically
    elif mode == "auto":
        key = genEncryptionKey(messageEntry.get())
        additionalEncryptionKeyEntry.config(state=NORMAL)
        additionalEncryptionKeyEntry.delete(0, END)
        additionalEncryptionKeyEntry.insert(0, str(key))
        additionalEncryptionKeyEntry.config(state=DISABLED)

    # Display encrypted output
    encryptedOutputEntry.config(state=NORMAL)
    encryptedOutputEntry.delete(0, END)
    encryptedOutputEntry.insert(0, encoder(messageEntry.get(), key))
    encryptedOutputEntry.config(state=DISABLED)

# Handle message entry for decryption
def decryptMessageEntryFunc(event=None):
    global decryptMessageEntry, decryptEncryptedOutputEntry
    global decryptAdditionalEncryptionKeyEntry
    key = 0

    # Manual mode: user enters decryption key
    if mode == "manual":
        decryptAdditionalEncryptionKeyEntry.config(state=NORMAL)
        if decryptAdditionalEncryptionKeyEntry.get() != "" and check_key(
            int(decryptAdditionalEncryptionKeyEntry.get())):
            key = int(decryptAdditionalEncryptionKeyEntry.get())
            decryptAdditionalEncryptionKeyEntry.delete(0, END)
            decryptAdditionalEncryptionKeyEntry.insert(0, str(key))

    # Auto mode: generate key automatically
    elif mode == "auto":
        if decryptMessageEntry.get():
            key = genEncryptionKey(decryptMessageEntry.get())
            decryptAdditionalEncryptionKeyEntry.config(state=NORMAL)
            decryptAdditionalEncryptionKeyEntry.delete(0, END)
            decryptAdditionalEncryptionKeyEntry.insert(0, str(key))
            decryptAdditionalEncryptionKeyEntry.config(state=DISABLED)

    # Display decrypted output
    decryptEncryptedOutputEntry.config(state=NORMAL)
    decryptEncryptedOutputEntry.delete(0, END)
    decryptEncryptedOutputEntry.insert(0, decoder(decryptMessageEntry.get(),
                                                  key))
    decryptEncryptedOutputEntry.config(state=DISABLED)

# Label for mode selection
modeLabel = Label(root, text="Encryption | Decryption mode for live entry",
                  height=2, bg="black", fg="white")
modeLabel.grid(row=9, column=0, padx=10, pady=10)

# Radio buttons for mode selection
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

# Default to "auto" mode
if mode == "auto":
    autoGenRadio.select()

# Disable output and key entry fields by default
encryptedOutputEntry.config(state=DISABLED)
additionalEncryptionKeyEntry.config(state=DISABLED)
decryptEncryptedOutputEntry.config(state=DISABLED)
decryptAdditionalEncryptionKeyEntry.config(state=DISABLED)

# Bind functions to entry fields for live updates
messageEntry.bind("<KeyRelease>", messageEntryFunc)
additionalEncryptionKeyEntry.bind("<KeyRelease>", messageEntryFunc)
decryptMessageEntry.bind("<KeyRelease>", decryptMessageEntryFunc)
decryptAdditionalEncryptionKeyEntry.bind("<KeyRelease>", decryptMessageEntryFunc)

# Start the GUI event loop
root.mainloop()

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
