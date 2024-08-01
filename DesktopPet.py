import time
import tkinter as tk
import random

class Pet():
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.radius = 50
        self.directiontimer = 60
        self.direction_x = 1
        self.direction_y = 1
        canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius, fill='red', outline='blue')
    def update(self):
        self.x += self.direction_x
        # self.y += self.direction_y
        if self.x >= width:
            self.direction_x = -1

window = tk.Tk()
window.attributes('-fullscreen', True)
window.attributes('-topmost', True)
height = window.winfo_screenheight()
width = window.winfo_screenwidth()
print(height, width)
canvas = tk.Canvas(window, bg='black', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)
window.wm_attributes('-transparentcolor', 'black')
pet = Pet()
window.after_idle(pet.update())
window.mainloop()

