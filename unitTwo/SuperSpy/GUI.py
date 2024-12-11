from tkinter import *
'''
File: ExpressionLoad.py
Author: Dhenushan Ramesh
Date: Nov 30, 2024

'''


root = Tk()
root.title("Super Spy Program")
root.configure(bg="black")

Title = Label(root, text="Encrypt Message", width=20, height=1, bg="black", fg="white")
Title.grid(row=0, column=0, padx=10, pady=10)
Title.config(font=(20))

FileN = Label(root, text="Enter File Name:", width=20, height=3, bg="black", fg="white")
FileN.grid(row=1, column=0, padx=10, pady=10)

entry = Entry(root, width=40, bg="#3B3B3B", fg="white", border=0)
entry.grid(row=1, column=1, padx=10, pady=10)

FileO = Label(root, text="Enter Output File name:", width=20, height=2, bg="black", fg="white")
FileO.grid(row=2, column=0, padx=10, pady=10)

entry2 = Entry(root, width=40, bg="#3B3B3B", fg="white", border=0)
entry2.grid(row=2, column=1, padx=10, pady=10)

EncryptionK = Label(root, text="Enter Encryption Key:", width=20, height=2, bg="black", fg="white")
EncryptionK.grid(row=3, column=0, padx=10, pady=10)

entry3 = Entry(root, width=40, bg="#3B3B3B", fg="white", border=0)
entry3.grid(row=3, column=1, padx=10, pady=10)

orblock = Label(root, text="OR", width=20, height=2, bg="black", fg="black")
orblock.grid(row=2, column=2, padx=10, pady=10)

message = Label(root, text="Enter message:", width=20, height=2, bg="black", fg="white")
message.grid(row=1, column=3, padx=10, pady=10)

entry4 = Entry(root, width=40, bg="#3B3B3B", fg="white", border=0)
entry4.grid(row=1, column=4, padx=10, pady=10)

EncryptKey = Label(root, text="Encrypted Output:", width=20, height=2, bg="black", fg="white")
EncryptKey.grid(row=2, column=3, padx=10, pady=10)

entry5 = Entry(root, width=40, bg="#3B3B3B", fg="white", border=0)
entry5.grid(row=2, column=4, padx=10, pady=10)

EncryptionK = Label(root, text="Enter Encryption Key:", width=20, height=2, bg="black", fg="white")
EncryptionK.grid(row=3, column=3, padx=10, pady=10)

entry6 = Entry(root, width=40, bg="#3B3B3B", fg="white", border=0)
entry6.grid(row=3, column=4, padx=10, pady=10)

# Run the application
root.mainloop()
