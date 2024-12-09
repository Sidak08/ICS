'''
File: ExpressionLoad.py
Author: Dhenushan Ramesh
Date: Nov 30, 2024

'''



root = Tk()
root.geometry("800x800")
root.title("Super Spy")
textOutput = Text(root, height=40, width=40)
textOutput.grid(column=0, row=0, padx=50, pady=20)
textOutput.insert(END, text)
textOutput.config(state=DISABLED)
root.mainloop()