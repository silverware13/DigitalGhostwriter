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

   def create_widgets(self):
       self.msg_text = tk.StringVar()
       self.msg = tk.Message(self, textvariable=self.msg_text, width=100)
       self.msg.grid(row=0, column=0)
	
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
            self.msg_text.set('Genre menu.')
            Page2.lift           
            # Go to page2.
	# If the user clicks the write button go to the write menu.
        if (hit == 2):
            self.msg_text.set('Write menu.')
            Page3.lift
	# If nothing clicked we say nothing was selected.
        if (hit == None):
            Screen=0
            self.msg_text.set('Nothing selected.')

# PAGE TWO - Genre.
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid()
       self.create_widgets()

   def create_widgets(self):
       self.msg_text = tk.StringVar()
       self.msg = tk.Message(self, textvariable=self.msg_text, width=100)
       self.msg.grid(row=0, column=0)
	
       self.picture = tk.PhotoImage(file='G1.gif')
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
        # If the user clicks the return button, go to main menu.
        if (hit == 1):
            self.msg_text.set('Return to main.')
	# If nothing clicked we say nothing was selected.
        if (hit == None):
            Screen=0
            self.msg_text.set('Nothing selected.')

# PAGE THREE - Write.
class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.grid()
       self.create_widgets()

   def create_widgets(self):
       self.msg_text = tk.StringVar()
       self.msg = tk.Message(self, textvariable=self.msg_text, width=100)
       self.msg.grid(row=0, column=0)
	
       self.picture = tk.PhotoImage(file='W1.gif')
	# left, top, right, bottom.
	# 0: Exit button.
       img_rects = [
              Rect(750, 0, 829, 64)]
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
	# If nothing clicked we say nothing was selected.
        if (hit == None):
            Screen=0
            self.msg_text.set('Nothing selected.')

# Main view.
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

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
