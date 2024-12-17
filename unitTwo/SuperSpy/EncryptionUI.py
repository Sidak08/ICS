from tkinter import *
from Encryption import encoder, decoder, genEncryptionKey
from FileAccess import load_file, save_to_file

'''
File: EncryptionUI.py
Author: Dhenushan Ramesh and Sidak Singh
Date: Dec 9, 2024

Work Contributions:
    Dhenushan Ramesh: Gui Elements, check_key(encryptKey: int), get_key(phrase: str)
    put_key_in_range(encryptKey: int), Commenting

    Sidak Singh: encryptFile(), decryptFile(), updateMode(newMode: str),
    messageEntryFunc(event=None), decryptMessageEntryFunc(event=None),
    radio buttons, integration of all systems, design GUI design


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

updateMode(newMode: str)
    - Updates the encryption/decryption mode (auto or manual)
    for live message entry.
    - parameters needed: newMode (str) - the new mode to set
    "auto" or "manual".
    - return: None.

messageEntryFunc(event=None)
    - Handles the encryption of the message entered by the user based on the
    selected mode (manual or auto).
    - parameters needed: event: default = None.
    - return: None.

decryptMessageEntryFunc(event=None)
    - Handles the decryption of the message entered by the user based on
    the selected mode (manual or auto).
    - parameters needed: event: default = None.
    - return: None.

'''

root = Tk() # create the root window
root.geometry("1000x600") # makes the size of the window
root.title("Super Spy Program") # Makes the title of the window
root.configure(bg="black") # Makes the background color of the window

def check_key(encryptKey: int) -> bool:
    try:
        if -2000000000 <= encryptKey <= 2000000000: # checks if the key is in the range
            return True # returns True if the key is in the range
        else:
            return False # returns False if the key is not in the range
    except Exception as e:
        print(f"Error in check_key: {e}") # prints the error message
        return False # returns False if there is an error

def get_key(phrase: str) -> int:
    try:
        key = phrase[0:11] # gets the first 11 characters of the phrase
        return int(key) # returns the 11 characters as a key as an integer
    except ValueError as e:
        print(f"ValueError in get_key: {e}. Unable to change the key to an integer.")
        # prints the error message
        return 0
    except Exception as e2:
        print(f"Unexpected error in get_key: {e2}") # prints the error message
        return 0

def put_key_in_range(encryptKey: int) -> int:
    try:
        # while encryptKey < -26 or encryptKey > 26: # checks if the key is in the range
        #     if encryptKey < -26: # checks if the key is less than -26
        #         encryptKey += 26 # adds 26 to the key
        #     elif encryptKey > 26: # checks if the key is greater than 26
        #         encryptKey -= 26 # subtracts 26 from the key
        # return int(encryptKey) # returns the key as an integer
        if encryptKey < -26: # checks if the key is less than -26
            return -((encryptKey * -1) % 26) # adds 26 to the key
        return encryptKey % 26
    except Exception as e:
        print(f"Error in put_key_in_range: {e}") # prints the error message
        return encryptKey




def encryptFile(fileName, outputFileName):
    try:
        phrases = load_file(fileName) # gets the phrases from the file
    except Exception as e:
        print(f"Problem with loading file: {e}") # prints the error while loading file
        return

    answer = [] # creates an empty list to store the new encrypted phrases
    try:
        for i in range(len(phrases)):
            try:
                key = get_key(phrases[i]) # gets the key from the phrase
                if check_key(key):
                    key = put_key_in_range(key) # puts the key in the range
                    answer.append(encoder(phrases[i], key))
                    # encrypts the phrase and adds it to the list
            except ValueError as e:
                print(f"There was a ValueError during encryption for phrase {i}: {e}")
                # prints the error message and line (incorrect value type)
            except Exception as e2:
                print(f"Unknown error during encryption for phrase {i}: {e2}")
                # prints the line and a general error message
    except Exception as e:
        print(f"Unexpected error when processing the phrases: {e}")
        # prints error when looping through the phrases
        return
    try:
        save_to_file(outputFileName, answer)
        # saves the encrypted phrases to a new file
    except Exception as e:
        print(f"Error saving the prhaes to file file: {e}")
        # prints an error message if there is a problem saving the file


def decryptFile(fileName, outputFileName):
    try:
        phrases = load_file(fileName)
        # gets the phrases from the file
    except Exception as e:
        print(f"Problem with loading file: {e}")
        # prints the error message while loading the file
        return

    answer = [] # creates an empty list to store the new decrypted phrases
    try:
        for i in range(len(phrases)):
            try:
                key = get_key(phrases[i]) # gets the key from the phrase
                if check_key(key):
                    key = put_key_in_range(key) # puts the key in the range
                    answer.append(decoder(phrases[i], key)) 
            except ValueError as e:
                print(f"There was a ValueError during decryption for phrase {i}: {e}")
                # prints the error message
            except Exception as e2:
                print(f"Unexpected error during decryption for phrase {i}: {e2}")
                # prints the error messsage
    except Exception as e:
        print(f"Unexpected error processing phrases: {e}") # prints the error message
        return
    try:
        save_to_file(outputFileName, answer) # saves the decrypted phrases to a new file
    except Exception as e:
        print(f"Error saving phrases to file: {e}") # prints error message


titleLabel = Label(root, text="Encrypt Message", width=20, height=1,
                    bg="black", fg="white") # creates a label for the title
titleLabel.grid(row=0, column=0, padx=10, pady=10) # places the label in the window
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
    border=0, command=lambda:
        encryptFile(fileNameEntry.get(), outputFileNameEntry.get()))
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
    fg="#FFFFFF", border=0, command=lambda:
        decryptFile(decryptFileNameEntry.get(), decryptOutputFileNameEntry.get()))
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

# Set initial mode for the radio button calculation to "auto"
mode = "auto"

# Update mode for the radio button and refresh encryption and decryption entries
def updateMode(newMode):
    global mode
    mode = newMode
    messageEntryFunc()
    decryptMessageEntryFunc()

# Handle entry for encryption
def messageEntryFunc(event=None):
    global messageEntry, encryptedOutputEntry, additionalEncryptionKeyEntry
    key = 0

    # Handles manual mode: user enters a key
    try:
        if mode == "manual":
            additionalEncryptionKeyEntry.config(state=NORMAL)
            if additionalEncryptionKeyEntry.get() != "" and check_key(
                int(additionalEncryptionKeyEntry.get())):
                # Check if the key is valid
                key = int(additionalEncryptionKeyEntry.get())
                additionalEncryptionKeyEntry.delete(0, END)
                additionalEncryptionKeyEntry.insert(0, str(key))
                # Displays the key

        # Handles Auto mode: generate key automatically
        elif mode == "auto":
            key = genEncryptionKey(messageEntry.get())
            # Generates a key based on the message
            additionalEncryptionKeyEntry.config(state=NORMAL)
            additionalEncryptionKeyEntry.delete(0, END)
            additionalEncryptionKeyEntry.insert(0, str(key))
            additionalEncryptionKeyEntry.config(state=DISABLED)
            # Displays the key
    except Exception as e:
        print("Your key value might have letter within it")
        print(e)

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

    # Handles Manual mode: user enters decryption key
    try:
        if mode == "manual":
            decryptAdditionalEncryptionKeyEntry.config(state=NORMAL)
            if decryptAdditionalEncryptionKeyEntry.get() != "" and check_key(
                int(decryptAdditionalEncryptionKeyEntry.get())):
                # Check if the key is valid
                key = int(decryptAdditionalEncryptionKeyEntry.get())
                decryptAdditionalEncryptionKeyEntry.delete(0, END)
                decryptAdditionalEncryptionKeyEntry.insert(0, str(key))
                # Displays the key

        # Handles Auto mode: generate key automatically
        elif mode == "auto":
            if decryptMessageEntry.get():
                key = genEncryptionKey(decryptMessageEntry.get())
                # Generates a key based on the message
                decryptAdditionalEncryptionKeyEntry.config(state=NORMAL)
                decryptAdditionalEncryptionKeyEntry.delete(0, END)
                decryptAdditionalEncryptionKeyEntry.insert(0, str(key))
                decryptAdditionalEncryptionKeyEntry.config(state=DISABLED)
                # Displays the key
    except Exception as e:
        print("Your key value might have letter within it")
        print(e)

    # Display decrypted output
    decryptEncryptedOutputEntry.config(state=NORMAL)
    decryptEncryptedOutputEntry.delete(0, END)
    decryptEncryptedOutputEntry.insert(0, decoder(decryptMessageEntry.get(), key))
    decryptEncryptedOutputEntry.config(state=DISABLED)

# Label for mode selection
modeLabel = Label(root, text="Encryption | Decryption mode for live entry",
                  height=2, bg="black", fg="white")
modeLabel.grid(row=9, column=0, padx=10, pady=10)

# Auto radio buttons for mode selection
autoGenRadio = Radiobutton(
    root, text="Auto Generate Key", value="auto", bg="black", fg="white",
    command=lambda: updateMode("auto")
)
autoGenRadio.grid(row=9, column=1, padx=10, pady=10)

# Manual radio buttons for mode selection
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

# Binds entery boxes to key release; so the values are calculated live
messageEntry.bind("<KeyRelease>", messageEntryFunc)
additionalEncryptionKeyEntry.bind("<KeyRelease>", messageEntryFunc)
decryptMessageEntry.bind("<KeyRelease>", decryptMessageEntryFunc)
decryptAdditionalEncryptionKeyEntry.bind("<KeyRelease>", decryptMessageEntryFunc)


#testing the functions
if __name__ == "__main__":
    #check_key
    print(check_key(0))  #output: True
    print(check_key(2000000000))  #output: True
    print(check_key(-2000000000))  #output: True
    print(check_key(2000000001))  #output: False
    print(check_key(-2000000001))  #output: False
    print(check_key(123456789))  #output: True
    print(check_key(-123456789))  #output: True

    #get_key
    print(get_key("12345678901Hello"))  # output: 12345678901
    print(get_key("00000000000World"))  # output: 0
    print(get_key("+9876543210Test"))  # output: 9876543210
    print(get_key("InvalidKey"))  # output: 0  # ValueError in get_key:
    print(get_key("12345abcde6Test"))  # output: 0  # ValueError in get_key:

    print("hi")

    #put_key_in_range
    print(put_key_in_range(0))  # output: 0
    print(put_key_in_range(26))  # output: 0
    print(put_key_in_range(-26))  # output: 0 FAILS
    print(put_key_in_range(27))  # output: 1
    print(put_key_in_range(-27))  # output: -1
    print(put_key_in_range(52))  # output: 0 FAILS
    print(put_key_in_range(-52))  # output: 0 FAILS
    print(put_key_in_range(53))  # output: 1
    print(put_key_in_range(-53)) # output: -1

    #encryptFile
    encryptFile("TestToEncrypt.txt", "Encrypted.txt")
    #Should not throw any errors
    #Encrypted.txt should display
    # 9
    # +1234567890 Dro aesmu lbygx pyh tewzc yfob dro vkji nyq.
    # +1122334455 Cjr hpxc rjjy rjpgy v rjjyxcpxf xcpxf da v rjjyxcpxf xjpgy xcpxf rjjy?
    # -1566778899 Wr eh ru qrw wr eh, wkdw lv wkh txhvwlrq.
    # +1677889900 Y hmsplcw md y rfmsqylb kgjcq zceglq ugrf y qglejc qrcn.
    # -1344556677 Rcc kyrk xczkkvij zj efk xfcu.
    # +1988776655 Ocz zvmgt wdmy xvoxczn ocz rjmh.
    # -1766554433 Tvmbhgl lixtd ehnwxk matg phkwl.
    # +2000000000 Ctcpw ajmsb fyq y qgjtcp jglgle.
    # -2000000000 Yjgp kp Tqog, fq cu vjg Tqocpu fq.


    #decryptFile
    decryptFile("Encrypted.txt", "Decrypted.txt")
    #Should not throw any errors
    #Decrypted.txt should display
    # 9
    # +1234567890 The quick brown fox jumps over the lazy dog.
    # +1122334455 How much wood would a woodchuck chuck if a woodchuck could chuck wood?
    # -1566778899 To be or not to be, that is the question.
    # +1677889900 A journey of a thousand miles begins with a single step.
    # -1344556677 All that glitters is not gold.
    # +1988776655 The early bird catches the worm.
    # -1766554433 Actions speak louder than words.
    # +2000000000 Every cloud has a silver lining.
    # -2000000000 When in Rome, do as the Romans do.

# Start the GUI event loop
root.mainloop()
