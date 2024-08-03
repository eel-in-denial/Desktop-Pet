import time
import tkinter as tk
import random
import math

pi = math.pi

class Spine():
    def __init__(self, circle_no, radi, sizes):
        self.points_list = []
        self.radi_list = radi
        self.sizes_list = sizes
        self.rigged_canvas = []
        self.body_canvas = []
        self.body_points_left = []
        self.body_points_right = []
        self.side_canvas = []
        self.direction = []
        self.body = ""
        self.head = []
        self.eyes = []
        self.eyes_canvas = []
        for i in range(circle_no):
            # body and rigging
            self.points_list.append([50 + i*self.radi_list[i], 50])
            drawing_points = [self.points_list[i][0]-self.radi_list[i], self.points_list[i][1]-self.radi_list[i], self.points_list[i][0]+self.radi_list[i], self.points_list[i][1]+self.radi_list[i]]
            circle = canvas.create_oval(drawing_points, outline='blue', width=2)
            self.rigged_canvas.append(circle)
            drawing_points = [self.points_list[i][0]-self.sizes_list[i], self.points_list[i][1]-self.sizes_list[i], self.points_list[i][0]+self.sizes_list[i], self.points_list[i][1]+self.sizes_list[i]]
            circle = canvas.create_oval(drawing_points, outline='blue', width=2)
            self.body_canvas.append(circle)
            # side circles
            self.direction.append(pi)
            if i == 0:
                self.head.append([self.points_list[i][0] + math.cos(self.direction[i]-pi/3)*self.sizes_list[i], self.points_list[i][1] + math.sin(self.direction[i]-pi/3)*self.sizes_list[i]])
                self.head.append([self.points_list[i][0] + math.cos(self.direction[i]+pi/3)*self.sizes_list[i], self.points_list[i][1] + math.sin(self.direction[i]+pi/3)*self.sizes_list[i]])
                self.eyes.append([self.points_list[i][0] + math.cos(self.direction[i]-pi/3)*self.sizes_list[i], self.points_list[i][1] + math.sin(self.direction[i]-pi/3)*self.sizes_list[i]])
                self.eyes.append([self.points_list[i][0] + math.cos(self.direction[i]+pi/3)*self.sizes_list[i], self.points_list[i][1] + math.sin(self.direction[i]+pi/3)*self.sizes_list[i]])

            self.body_points_left.append([self.points_list[i][0] + math.cos(self.direction[i]-pi/2)*self.sizes_list[i], self.points_list[i][1] + math.sin(self.direction[i]-pi/2)*self.sizes_list[i]])
            self.body_points_right.append([self.points_list[i][0] + math.cos(self.direction[i]+pi/2)*self.sizes_list[i], self.points_list[i][1] + math.sin(self.direction[i]+pi/2)*self.sizes_list[i]])
            #side circles drawn
            drawing_points = [self.body_points_left[i][0]-5, self.body_points_left[i][1]-5, self.body_points_left[i][0]+5, self.body_points_left[i][1]+5]
            circle = canvas.create_oval(drawing_points, outline='red', width=2)
            self.side_canvas.append(circle)
            drawing_points = [self.body_points_right[i][0]-5, self.body_points_right[i][1]-5, self.body_points_right[i][0]+5, self.body_points_right[i][1]+5]
            circle = canvas.create_oval(drawing_points, outline='orange', width=2)
            self.side_canvas.append(circle)
        # polygon
        self.body_points_right.reverse()
        self.body = canvas.create_polygon(self.body_points_left + self.body_points_right, outline="white", width=2, smooth=1, fill="yellow")
        self.body_points_right.reverse()
        drawing_points = [self.eyes[0][0]-5, self.eyes[0][1]-5, self.eyes[0][0]+5, self.eyes[0][1]+5]
        eye = canvas.create_oval(drawing_points, outline='black', width=2, fill="black")
        self.eyes_canvas.append(eye)
        drawing_points = [self.eyes[1][0]-5, self.eyes[1][1]-5, self.eyes[1][0]+5, self.eyes[1][1]+5]
        eye = canvas.create_oval(drawing_points, outline='black', width=2, fill="black")
        self.eyes_canvas.append(eye)
    def update(self, mouse_x, mouse_y):
        for i in range(len(self.points_list)):
            sqrt = math.sqrt((self.points_list[i][0] - self.points_list[i-1][0])**2 + (self.points_list[i][1] - self.points_list[i-1][1])**2)
            if i == 0:
                direction_x, direction_y = mouse_x - self.points_list[0][0], mouse_y - self.points_list[0][1]
                self.points_list[0][0], self.points_list[0][1] = mouse_x, mouse_y
                length = self.sizes_list[i]/sqrt
                self.head[0] = [self.points_list[i][0] + math.cos(self.direction[i]+pi/6)*60, self.points_list[i][1] + math.sin(self.direction[i]+pi/6)*60]
                self.head[1] = [self.points_list[i][0] + math.cos(self.direction[i]-pi/6)*60, self.points_list[i][1] + math.sin(self.direction[i]-pi/6)*60]
                self.eyes[0] = [self.points_list[i][0] + math.cos(self.direction[i]+4*pi/3)*30, self.points_list[i][1] + math.sin(self.direction[i]+4*pi/3)*30]
                self.eyes[1] = [self.points_list[i][0] + math.cos(self.direction[i]-4*pi/3)*30, self.points_list[i][1] + math.sin(self.direction[i]-4*pi/3)*30]
            else:
                length = 1-(self.radi_list[i]/sqrt)
                direction_x, direction_y = self.points_list[i-1][0] - self.points_list[i][0], self.points_list[i-1][1] - self.points_list[i][1]
                self.points_list[i][0] += length*(direction_x)
                self.points_list[i][1] += length*(direction_y)
            # calculates position of points
            self.direction[i] = math.atan2(direction_y, direction_x)
            self.body_points_left[i] = [self.points_list[i][0] + math.cos(self.direction[i]-pi/2)*self.sizes_list[i], self.points_list[i][1] + math.sin(self.direction[i]-pi/2)*self.sizes_list[i]]
            self.body_points_right[i] = [self.points_list[i][0] + math.cos(self.direction[i]+pi/2)*self.sizes_list[i], self.points_list[i][1] + math.sin(self.direction[i]+pi/2)*self.sizes_list[i]]
            # moves the side circles
            drawing_points = [self.body_points_left[i][0]-5, self.body_points_left[i][1]-5]
            canvas.moveto(self.side_canvas[i*2], *drawing_points)
            drawing_points = [self.body_points_right[i][0]-5, self.body_points_right[i][1]-5]
            canvas.moveto(self.side_canvas[i*2+1], *drawing_points)

            # moves rigging circles
            canvas.moveto(self.rigged_canvas[i], int(self.points_list[i][0] - self.radi_list[i]), int(self.points_list[i][1] - self.radi_list[i]))
            # moves body circles
            canvas.moveto(self.body_canvas[i], int(self.points_list[i][0] - self.sizes_list[i]), int(self.points_list[i][1] - self.sizes_list[i]))

        # moves polygon body shape
        self.body_points_right.reverse()
        canvas.coords(self.body, self.head + self.body_points_left + self.body_points_right)
        self.body_points_right.reverse()
        canvas.moveto(self.eyes_canvas[0], self.eyes[0][0] - 5, self.eyes[0][1] - 5)
        canvas.moveto(self.eyes_canvas[1], self.eyes[1][0] - 5, self.eyes[1][1] - 5)

 # detect perpendicular and then create polygon
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
        radi = [40, 40, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
        bodies = [40, 50, 40, 30, 30, 29, 29, 28, 28, 27, 27, 26, 26, 25, 25, 24, 24, 23, 23, 22, 22, 21, 21, 20, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
        self.spine = Spine(40, radi, bodies)
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
canvas = tk.Canvas(window, bg='aqua', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)
window.wm_attributes('-transparentcolor', 'aqua') # make black transparent
pet = Pet()
print("heello")

# event bindings
window.bind("<KeyPress>", check_key)

window.after(100, programloop) # start main program loop
window.mainloop() # checks events

