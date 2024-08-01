import time
import tkinter as tk
import random
import math

class Spine():
    def __init__(self, circle_no, radi, sizes):
        self.points_list = []
        self.radi_list = radi
        self.sizes_list = sizes
        self.rigged_list = []
        self.body_list = []
        for i in range(circle_no):
            self.points_list.append([50 + i*50, 50])
            # drawing_points = [self.points_list[i][0]-self.radi_list[i], self.points_list[i][1]-self.radi_list[i], self.points_list[i][0]+self.radi_list[i], self.points_list[i][1]+self.radi_list[i]]
            # circle = canvas.create_oval(drawing_points, outline='blue', width=2)
            # self.rigged_list.append(circle)
            drawing_points = [self.points_list[i][0]-self.sizes_list[i], self.points_list[i][1]-self.sizes_list[i], self.points_list[i][0]+self.sizes_list[i], self.points_list[i][1]+self.sizes_list[i]]
            circle = canvas.create_oval(drawing_points, outline='blue', width=2)
            self.body_list.append(circle)
    def update(self, mouse_x, mouse_y):
        for i in range(len(self.points_list)):
            if i == 0:
                self.points_list[0][0], self.points_list[0][1] = mouse_x, mouse_y
            else:
                sqrt = math.sqrt((self.points_list[i][0] - self.points_list[i-1][0])**2 + (self.points_list[i][1] - self.points_list[i-1][1])**2)
                length = (sqrt-self.radi_list[i])/sqrt
                self.points_list[i][0] += length*(self.points_list[i-1][0]-self.points_list[i][0])
                self.points_list[i][1] += length*(self.points_list[i-1][1]-self.points_list[i][1])
            # canvas.moveto(self.rigged_list[i], int(self.points_list[i][0] - self.radi_list[i]), int(self.points_list[i][1] - self.radi_list[i]))
            canvas.moveto(self.body_list[i], int(self.points_list[i][0] - self.sizes_list[i]), int(self.points_list[i][1] - self.sizes_list[i]))


class Pet():
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.x2 = width/2
        self.y2 = height/2
        self.radius = 50
        self.direction_x = 1
        self.direction_y = 1
        self.dv_x = 0
        self.dv_y = 0
        self.length = 0
        radi = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
        bodies = [50, 38, 38, 38, 37, 36, 35, 34, 33, 32, 31, 30, 28, 26, 24, 22, 20, 18, 16, 14]
        self.spine = Spine(20, radi, bodies)
    def update(self):
        self.spine.update(window.winfo_pointerx(), window.winfo_pointery())


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

