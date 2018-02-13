# Digital Ghostwriter
#
# Zachary Thomas
# thomasza@oregonstate.edu
# 2/12/2018
#

import sys
#from tkinter import *
import tkinter as tk

App = tk.Tk()

# Set window size and name.
App.geometry("829x556")
App.title("Digital Ghostwriter")

# Set image.
image = tk.PhotoImage(file="MM.gif")
label = tk.Label(image=image)
label.image = image
label.pack()

App.mainloop()
