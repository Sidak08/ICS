from tkinter import *
'''
File: ExpressionLoad.py
Author: Dhenushan Ramesh
Date: Nov 30, 2024

'''

import tkinter as tk

root = tk.Tk()
root.title("File Name Input")

FileN = tk.Label(root, text="Enter File Name:", width=20, height=2)
FileN.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.grid(row=0, column=1, padx=10, pady=10)

FileO = tk.Label(root, text="Enter Output File name:", width=20, height=2)
FileO.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root, width=40)
entry2.grid(row=1, column=1, padx=10, pady=10)

EncryptionK = tk.Label(root, text="Enter Encryption Key:", width=20, height=2)
EncryptionK.grid(row=2, column=0, padx=10, pady=10)

entry3 = tk.Entry(root, width=40)
entry3.grid(row=2, column=1, padx=10, pady=10)

orblock = tk.Label(root, text="OR", width=20, height=2)
orblock.grid(row=1, column=2, padx=10, pady=10)

FileN = tk.Label(root, text="Enter File Name:", width=20, height=2)
FileN.grid(row=0, column=3, padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.grid(row=0, column=4, padx=10, pady=10)

# Run the application
root.mainloop()