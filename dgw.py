# Digital Ghostwriter
# 2/12/2018

from collections import namedtuple
import tkinter as tk

Rect = namedtuple('Rect', 'x0, y0, x1, y1')

class ImageMapper(object):
    def __init__(self, image, img_rects):
        self.width, self.height = image.width(), image.height()
        self.img_rects = img_rects

    def find_rect(self, x, y):
        for i, r in enumerate(self.img_rects):
            if (r.x0 <= x <= r.x1) and (r.y0 <= y <= r.y1):
                return i
        return None

class Demo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
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
	# If the user clicks the write button go to the write menu.
        if (hit == 2):
            self.msg_text.set('Write menu.')
	# If nothing clicked we say so.
        if (hit == None):
            self.msg_text.set('Nothing selected.')

app = Demo()
app.master.title('Image Mapper')
app.mainloop()
