import time
import tkinter as tk
import random
import math
class Pet():
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.x2 = width/2
        self.y2 = height/2
        self.radius = 50
        self.direction_x = 1
        self.direction_y = 1
        self.head = canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius, outline='blue', width=2)
        self.neck = canvas.create_oval(self.x2-self.radius, self.y2-self.radius, self.x2+self.radius, self.y2+self.radius, outline='blue', width=2)
        self.dv_x = 0
        self.dv_y = 0
    def update(self):
        # self.x += self.direction_x
        # self.y += self.direction_y
        # if self.x >= width:
        #     self.direction_x = -10
        mouse_x, mouse_y = window.winfo_pointerx(), window.winfo_pointery()
        self.direction_x, self.direction_y = mouse_x - self.x, mouse_y - self.y
        canvas.move(self.head, self.direction_x, self.direction_y)
        self.x, self.y = mouse_x, mouse_y
        self.dv_x, self.dv_y= (50/math.sqrt(self.x**2 + self.y**2))*(self.x2 - self.x), (50/math.sqrt(self.x**2 + self.y**2))*(self.y2 - self.y)
        canvas.move(self.neck, self.x+self.dv_x-self.x2, self.y+self.dv_y-self.y2)



def programloop(): # main loop
    pet.update()
    window.after(10, programloop)

def check_key(event): # check what key was pressed
    if event.keysym == "p":
        window.destroy() # close program

# creating window / fullscreen / top overlay
window = tk.Tk()
window.attributes('-fullscreen', True)
window.attributes('-topmost', True)
# set height and width variables
height = window.winfo_screenheight()
width = window.winfo_screenwidth()

#set up black canvas
canvas = tk.Canvas(window, bg='black', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)
window.wm_attributes('-transparentcolor', 'black') # make black transparent
pet = Pet()

# event bindings
window.bind("<KeyPress>", check_key)

window.after(100, programloop) # start main program loop
window.mainloop() # checks events

