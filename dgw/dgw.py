# Digital Ghostwriter
# 2/12/2018

from collections import namedtuple
import tkinter as tk
from tkinter.font import Font
from tkinter import *
from tkinter import messagebox
import os
import re
import time
import math

Rect = namedtuple('Rect', 'x0, y0, x1, y1')

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

# Main menu.
class MainMenu(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid()
       self.create_widgets()
   
   def setup_pages(self,pg):
       self.pages = pg
   
   def create_widgets(self):
       self.picture = tk.PhotoImage(file='MM.gif')
	# left, top, right, bottom.
	# 0: Exit button.
	# 1: Genre button.
	# 2: Write button.
       img_rects = [
              Rect(750, 0, 829, 64),
              Rect(0, 65, 413, 556),
              Rect(414, 65, 829, 556)]
       self.imagemapper = ImageMapper(self.picture, img_rects)
        # use Label widget to display image
       self.image = tk.Label(self, image=self.picture, borderwidth=0)
       self.image.bind('<Button-1>', self.image_click)
       self.image.grid(row=1, column=0)
       
   def image_click(self, event):
       hit = self.imagemapper.find_rect(event.x, event.y)
	# If the user clicks the exit button, quit.
       if (hit == 0):
          quit()
	# If the user clicks the genre button go to the genre menu.
       if (hit == 1):
           self.pages[3].lift()
	# If the user clicks the write button go to the write menu.
       if (hit == 2):
           self.pages[1].lift()

# Write specifications.
class WriteSpecs(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.configure(bg='#74A84F') # Set our background to a green color.

   def create_widgets(self):
       frame = Frame(self)
       frame.configure(bg='#74A84F') # Set our background to a green color.
       frame.grid(row=2, column=0, padx=10, pady=10) # This frame holds all buttons.
       frameDone = Frame(self)
       frameDone.configure(bg='#74A84F') # Set our background to a green color.
       frameDone.grid(row=3, column=0, padx=10, pady=10) # This frame holds the text fields and the done button.
       btnFont = Font(family='Helvetica', size=15, weight='bold') # This is the font we use for our buttons.
       self.cntLabel = Label(frameDone, text="Story Word Count", font=btnFont, bg='#74A84F')
       self.cntLabel.grid(row=1, column=0, padx=10, pady=10) # Label for word count.
       self.wrdCnt = Entry(frameDone, font=btnFont)
       self.wrdCnt.grid(row=2, column=0, padx=10, pady=10) # Text field for word count.
       self.fileLabel = Label(frameDone, text="Story Name", font=btnFont, bg='#74A84F')
       self.fileLabel.grid(row=3, column=0, padx=10, pady=10) # Label for story name.
       self.fileName = Entry(frameDone, font=btnFont)
       self.fileName.grid(row=4, column=0, padx=10, pady=10) # Text field for file name.
       self.done = tk.Button(frameDone, text="Done", bg='#FFD966', bd=0, height=3, width=10, font=btnFont, command= self.verify_fields) # Done button.
       self.done.grid(row=5, column=0, padx=10, pady=30)
       self.btns = []
       i = 0
       ii = 1
       self.current_genre = ""
       for x in os.listdir("./genre"):       
           self.btns.append(tk.Button(frame, text=x, bg='#B6D7A8', bd=0, height=3, width=15, font=btnFont, command= lambda y=x: self.genre_pressed(y))) # Genre buttons.
       for b in self.btns:
           b.grid(row=ii, column=i, padx=10, pady=10)
           i += 1
           if i > 2:
              i = 0
              ii += 1

   def genre_pressed(self, text):
       for b in self.btns:
           b.configure(bg='#B6D7A8')           
           if b['text'] in text:
               b.configure(bg='#FFD966')
               self.current_genre = text
   
   def verify_fields(self):
       try:
           if self.current_genre == "":
               messagebox.showerror("Genre Selection Error", "Please select a genre.")
               return
       	   self.string_wrdCnt = self.wrdCnt.get() # Get the word count from the word count field.
           wc = int(self.string_wrdCnt)
           if wc <= 0 or wc > 10000:
               messagebox.showerror("Word Count Error", "Word count must be a positive number no greater than ten thousand.")
               return
           self.string_wrdCnt = str(wc - 1)
           self.string_name = self.fileName.get() # Get the file name from the file name field.
           if len(self.string_name) == 0 or len(self.string_name) >= 256:
               messagebox.showerror("Invalid File Name", "File name must be between 1 and 255 characters long (inclusive).")
               return
           if re.fullmatch("[a-zA-Z0-9_-]*", self.string_name) is None:
               messagebox.showerror("Invalid File Name", "File name may contain only alphanumeric characters, '_', and '-'.")
               return
           self.write_story()
       except ValueError:
           messagebox.showerror("Word Count Error", "Please enter a number.")

   def write_story(self):
       self.picturepop = tk.PhotoImage(file='WW.gif')
       self.imagepop = tk.Label(self, image=self.picturepop, borderwidth=0)
       self.imagepop.grid(row=0, column=0) # Display an image saying 'Writing story to file... please wait'.
       self.update() # Updates our image before running next command.
       cmd = "python sample.py -n " + self.string_wrdCnt + " --quiet --save_dir save/" + self.current_genre + " > ./stories/" + self.string_name  + ".txt 2> /dev/null" # Save our command with vars.
       self.wrdCnt.delete(0, END) # Clear word count entry.
       self.fileName.delete(0, END) # Clear file name entry.
       exstat = os.system(cmd) # Next write our file.
       self.imagepop.destroy()
       if exstat != 0:
           messagebox.showerror("Write Error", "Failed to write story.")
       else:
           self.pages[2].lift() # When done writing story go to finished page.
       
   def setup_pages(self, pg):
       self.pages = pg
       self.setup_header()
       self.create_widgets()   

   def setup_header(self):
       self.picture = tk.PhotoImage(file='HG.gif')
       # 0: Back button.
       # 1: Exit button.
       img_rects = [
              Rect(0, 0, 64, 64),
              Rect(750, 0, 829, 64)]
       self.imagemapper = ImageMapper(self.picture, img_rects)
       self.image = tk.Label(self, image=self.picture, borderwidth=0)
       self.image.bind('<Button-1>', self.image_click)
       self.image.grid(row=1, column=0)

   def image_click(self, event):
       hit = self.imagemapper.find_rect(event.x, event.y)
       # If the user clicks the back button go back a page.
       if (hit == 0):
           self.pages[0].lift()
       # If the user clicks the exit button, quit.
       if (hit == 1):
          quit()

# PAGE THREE - <REMOVE ME>
class Useless(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid()
       self.configure(bg='#74A84F') # Set our background to a green color.

   def setup_pages(self,pg):
       self.pages = pg

# Write was successful.
class WriteSuccess(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid()
       self.create_widgets()
       self.configure(bg='#74A84F') # Set our background to a green color.

   def setup_pages(self,pg):
       self.pages = pg
   
   def create_widgets(self):
       btnFont = Font(family='Helvetica', size=30, weight='bold') # This is the font we use for our buttons.
       self.picture = tk.PhotoImage(file='HD.gif')
	# left, top, right, bottom.
	# 0: Exit button.
       img_rects = [
              Rect(750, 0, 829, 64)]
       self.imagemapper = ImageMapper(self.picture, img_rects)
        # use Label widget to display image
       self.image = tk.Label(self, image=self.picture, borderwidth=0)
       self.image.bind('<Button-1>', self.image_click)
       self.image.grid(row=1, column=0) # This is our header.
       self.scrTxt = Label(self, text="The story has been\nwritten and saved", font=btnFont, bg='#74A84F')
       self.scrTxt.grid(row=2, column=0, padx=10, pady=10) # Label for word count.
       self.picture2 = tk.PhotoImage(file='CM.gif')
       self.check = tk.Label(self, image=self.picture2, borderwidth=0)
       self.check.grid(row=3, column=0) # This is a check mark.
       btnFont = Font(family='Helvetica', size=15, weight='bold') # This is the font we use for our buttons.
       self.done = tk.Button(self, text="Done", bg='#FFD966', bd=0, height=3, width=10, font=btnFont, command=self.done_return) # Done button.
       self.done.grid(row=4, column=0, padx=10, pady=10)

   def done_return(self):
        self.pages[0].lift()

   def image_click(self, event):
        hit = self.imagemapper.find_rect(event.x, event.y)
        # If the user clicks the exit button, quit.
        if (hit == 0):
            quit()

# View genres.
class GenreView(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.configure(bg='#6D9EEB') # Set our background to a blue color.

   def create_widgets(self):
       frame = Frame(self)
       frame.configure(bg='#6D9EEB') # Set our background to a blue color.
       frame.grid(row=2, column=0) # This frame holds all buttons.
       btnFont = Font(family='Helvetica', size=20, weight='bold') # This is the font we use for our buttons.
       self.btns = []
       i = 0
       ii = 1
       for x in os.listdir("./genre"):       
           self.btns.append(tk.Button(frame, text=x, bg='#CFE2F3', bd=0, height=3, width=15, font=btnFont, command= lambda y=x: self.make_page(y)))
       for b in self.btns:
           b.grid(row=ii, column=i, padx=10, pady=10)
           i += 1
           if i > 2:
              i = 0
              ii += 1

   def make_page(self, name):
       pg = PageGenre(self)
       pg.setup_pages(self.pages)
       pg.create_widgets(name)
       pg.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
       pg.lift()
   
   def setup_pages(self, pg):
       self.pages = pg
       self.setup_header()
       self.create_widgets()
       
   def setup_header(self):
       self.picture = tk.PhotoImage(file='HB.gif')
       # 0: Back button.
       # 1: Exit button.
       img_rects = [
              Rect(0, 0, 64, 64),
              Rect(750, 0, 829, 64)]
       self.imagemapper = ImageMapper(self.picture, img_rects)
       self.image = tk.Label(self, image=self.picture, borderwidth=0)
       self.image.bind('<Button-1>', self.image_click)
       self.image.grid(row=1, column=0)
 
   def image_click(self, event):
       hit = self.imagemapper.find_rect(event.x, event.y)
       # If the user clicks the back button go back a page.
       if (hit == 0):
           self.pages[0].lift()
       # If the user clicks the exit button, quit.
       if (hit == 1):
          quit()

# SPECIFIC GENRE PAGE.
class PageGenre(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.configure(bg='#6D9EEB') # Set our background to a blue color.
   
   def create_widgets(self, name):
      frame = Frame(self)
      frame.configure(bg='#6D9EEB') # Set our background to a blue color.
      frame.grid(row=2, column=0, padx=10, pady=10) # This frame holds all buttons.
      btnFont = Font(family='Helvetica', size=15, weight='bold') # This is the font we use for our buttons.
      self.btns = []
      i = 0
      ii = 1
      for x in os.listdir("./genre/" + name): 
          self.btns.append(tk.Button(frame, text=x, bg='#CFE2F3', bd=0, height=3, width=15, font=btnFont))
      for b in self.btns:
          b.grid(row=ii, column=i, padx=10, pady=10)
          i += 1
          if i > 2:
             i = 0
             ii += 1

   def setup_pages(self, pg):
       self.pages = pg
       self.setup_header()

   def setup_header(self):
       self.picture = tk.PhotoImage(file='HB.gif')
       # 0: Back button.
       # 1: Exit button.
       img_rects = [
              Rect(0, 0, 64, 64),
              Rect(750, 0, 829, 64)]
       self.imagemapper = ImageMapper(self.picture, img_rects)
       self.image = tk.Label(self, image=self.picture, borderwidth=0)
       self.image.bind('<Button-1>', self.image_click)
       self.image.grid(row=1, column=0)
   
   def image_click(self, event):
       hit = self.imagemapper.find_rect(event.x, event.y)
       # If the user clicks the back button go back a page.
       if (hit == 0):
          self.destroy()
       # If the user clicks the exit button, quit.
       if (hit == 1):
          quit()

# Main view.
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = MainMenu(self)
        p2 = WriteSpecs(self)
        p3 = WriteSuccess(self)
        p4 = GenreView(self)
        
        pg = [p1,p2,p3,p4]
        
        p1.setup_pages(pg)
        p2.setup_pages(pg)
        p3.setup_pages(pg)
        p4.setup_pages(pg)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        p1.show()

class ImageMapper(object):
    def __init__(self, image, img_rects):
        self.width, self.height = image.width(), image.height()
        self.img_rects = img_rects

    def find_rect(self, x, y):
        for i, r in enumerate(self.img_rects):
            if (r.x0 <= x <= r.x1) and (r.y0 <= y <= r.y1):
                return i
        return None

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Digital Ghostwriter")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("829x556")
    root.resizable(False,False) # Make window unresizeable.
    root.mainloop()
