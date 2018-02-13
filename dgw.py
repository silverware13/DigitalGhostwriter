# Digital Ghostwriter
#
# Zachary Thomas
# thomasza@oregonstate.edu
# 2/12/2018
#

import sys
#from tkinter import *
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# Set window size and name.
root.geometry("829x556")
root.title("Digital Ghostwriter")

# Set image.
image = tk.PhotoImage(file="MM.gif")
label = tk.Label(image=image)
label.image = image
label.pack()

# Exit button.
button = tk.Button(frame, text="QUIT", fg="red", command=quit)
button.pack(side=tk.LEFT)

root.mainloop()
