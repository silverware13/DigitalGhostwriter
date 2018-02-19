# Digital Ghostwriter
# 2/12/2018

from collections import namedtuple
import tkinter as tk

Rect = namedtuple('Rect', 'x0, y0, x1, y1')

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

# PAGE ONE - Main menu.
class Page1(Page):
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
           self.pages[4].lift()
	# If the user clicks the write button go to the write menu.
       if (hit == 2):
           self.pages[1].lift()

# PAGE TWO - Write.
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid()
       self.create_widgets()

   def setup_pages(self,pg):
       self.pages = pg

   def create_widgets(self):
       self.picture = tk.PhotoImage(file='W1.gif')
	# left, top, right, bottom.
	# 0: Exit button.
       img_rects = [
              Rect(750, 0, 829, 64),
              Rect(0, 0, 64, 64),
              Rect(327, 462, 541, 526)]
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
        # If the user clicks the return button, go to main menu.
        if (hit == 1):
           self.pages[0].lift()
        # If the user clicks the done button, go to write name page.
        if (hit == 2):
           self.pages[2].lift()

# PAGE THREE - Write name.
class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid()
       self.create_widgets()

   def setup_pages(self,pg):
       self.pages = pg
   
   def create_widgets(self):
       self.picture = tk.PhotoImage(file='W2.gif')
	# left, top, right, bottom.
	# 0: Exit button.
	# 1: Return to main menu.
       img_rects = [
              Rect(750, 0, 829, 64),
              Rect(0, 0, 64, 64),
              Rect(327, 462, 541, 526)]
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
        # If the user clicks the return button, go to write menu.
        if (hit == 1):
           self.pages[1].lift()
        # If the user clicks the done button, go to finish write page.
        if (hit == 2):
           self.pages[3].lift()

# PAGE FOUR - Write done.
class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid()
       self.create_widgets()

   def setup_pages(self,pg):
       self.pages = pg
   
   def create_widgets(self):
       self.picture = tk.PhotoImage(file='W3.gif')
	# left, top, right, bottom.
	# 0: Exit button.
	# 1: Return to main menu.
       img_rects = [
              Rect(750, 0, 829, 64),
              Rect(327, 462, 541, 526)]
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
        # If the user clicks the done button, go to write menu.
        if (hit == 1):
           self.pages[0].lift()

# PAGE FIVE - Genre.
class Page5(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid()
       self.create_widgets()

   def setup_pages(self,pg):
       self.pages = pg
   
   def create_widgets(self):
       self.picture = tk.PhotoImage(file='G1.gif')
	# left, top, right, bottom.
	# 0: Exit button.
	# 1: Return to main menu.
       img_rects = [
              Rect(750, 0, 829, 64),
              Rect(0, 0, 64, 64),
              Rect(581, 97, 795, 145)]
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
        # If the user clicks the return button, go to main menu.
        if (hit == 1):
           self.pages[0].lift()
        # If the user clicks the horror button, go to horror menu.
        if (hit == 2):
           self.pages[5].lift()

# PAGE SIX - Horror.
class Page6(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid()
       self.create_widgets()

   def setup_pages(self,pg):
       self.pages = pg
   
   def create_widgets(self):
       self.picture = tk.PhotoImage(file='G2.gif')
	# left, top, right, bottom.
	# 0: Exit button.
	# 1: Return to main menu.
       img_rects = [
              Rect(750, 0, 829, 64),
              Rect(0, 0, 64, 64)]
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
        # If the user clicks the return button, go to genre menu.
        if (hit == 1):
           self.pages[4].lift()

# Main view.
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p6 = Page6(self)
        p5 = Page5(self)
        p4 = Page4(self)
        p3 = Page3(self)
        p2 = Page2(self)
        p1 = Page1(self)
        
        pg = [p1,p2,p3,p4,p5,p6]
        
        p1.setup_pages(pg)
        p2.setup_pages(pg)
        p3.setup_pages(pg)
        p4.setup_pages(pg)
        p5.setup_pages(pg)
        p6.setup_pages(pg)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

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
    root.mainloop()
