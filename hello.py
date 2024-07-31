import time
import tkinter as tk
import random

class Pet():
    def __init__(self):
        self.window = tk.Tk()
        self.x = 0
        self.y = 0
        self.directiontimer = 60
        self.direction_x = 0
        self.direction_y = 0

        img = tk.PhotoImage(file="MCcloak.png")

        self.window.config(highlightbackground='black')

        self.window.overrideredirect(True) # window becomes frameless

        self.window.attributes('-topmost', True) # window is always at top

        self.window.wm_attributes('-transparentcolor', 'black') # black becomes transparent (background)

        self.label = tk.Label(self.window, bd=0, bg='black') # image container

        self.window.geometry(f"128x128+{self.x}+{self.y}") # set size and location

        self.label.configure(image=img) # add image

        self.label.pack() # doing thing thongs

        self.window.after(0, self.update) #run update every frame from very first frame (after 0)
        self.window.mainloop()
    def update(self):

        if self.directiontimer > 0:
            self.directiontimer -= 1
            if self.directiontimer == 0:
                self.direction_x = random.rand()
        self.x += 1
        self.y += 1
        self.window.geometry(f"128x128+{self.x}+{self.y}") # new pos
        self.window.after(10, self.update)

Pet()
