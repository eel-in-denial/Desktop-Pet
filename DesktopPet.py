import time
import tkinter as tk
from tkinter import ttk
import random
import math

pi = math.pi
        
class Spine:
    def __init__(self, circle_no, radi, sizes, mouse_x, mouse_y):
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
            self.points_list.append([mouse_x + i*self.radi_list[i], mouse_y])
            # body and rigging
            # drawing_points = [self.points_list[i][0]-self.radi_list[i], self.points_list[i][1]-self.radi_list[i], self.points_list[i][0]+self.radi_list[i], self.points_list[i][1]+self.radi_list[i]]
            # circle = canvas.create_oval(drawing_points, outline='blue', width=2)
            # self.rigged_canvas.append(circle)
            # drawing_points = [self.points_list[i][0]-self.sizes_list[i], self.points_list[i][1]-self.sizes_list[i], self.points_list[i][0]+self.sizes_list[i], self.points_list[i][1]+self.sizes_list[i]]
            # circle = canvas.create_oval(drawing_points, outline='blue', width=2)
            # self.body_canvas.append(circle)
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
            # drawing_points = [self.body_points_left[i][0]-5, self.body_points_left[i][1]-5, self.body_points_left[i][0]+5, self.body_points_left[i][1]+5]
            # circle = canvas.create_oval(drawing_points, outline='red', width=2)
            # self.side_canvas.append(circle)
            # drawing_points = [self.body_points_right[i][0]-5, self.body_points_right[i][1]-5, self.body_points_right[i][0]+5, self.body_points_right[i][1]+5]
            # circle = canvas.create_oval(drawing_points, outline='orange', width=2)
            # self.side_canvas.append(circle)
        # polygon
        self.body_points_right.reverse()
        self.body = canvas.create_polygon(self.body_points_left + self.body_points_right, outline="white", width=2, smooth=1, fill="yellow")
        self.body_points_right.reverse()
        drawing_points = [self.eyes[0][0]-10, self.eyes[0][1]-10, self.eyes[0][0]+10, self.eyes[0][1]+10]
        eye = canvas.create_oval(drawing_points, outline='black', width=2, fill="black")
        self.eyes_canvas.append(eye)
        drawing_points = [self.eyes[1][0]-10, self.eyes[1][1]-10, self.eyes[1][0]+10, self.eyes[1][1]+10]
        eye = canvas.create_oval(drawing_points, outline='black', width=2, fill="black")
        self.eyes_canvas.append(eye)
    def update(self, mouse_x, mouse_y):
        for i in range(len(self.points_list)):
            sqrt = math.sqrt((self.points_list[i][0] - self.points_list[i-1][0])**2 + (self.points_list[i][1] - self.points_list[i-1][1])**2)
            if i == 0:
                direction_x, direction_y = mouse_x - self.points_list[0][0], mouse_y - self.points_list[0][1]
                self.direction[i] = math.atan2(direction_y, direction_x)
                print(self.direction[i])
                self.points_list[0][0], self.points_list[0][1] = mouse_x, mouse_y
                self.head[0] = [self.points_list[i][0] + math.cos(self.direction[i]+pi/6)*60, self.points_list[i][1] + math.sin(self.direction[i]+pi/6)*60]
                self.head[1] = [self.points_list[i][0] + math.cos(self.direction[i]-pi/6)*60, self.points_list[i][1] + math.sin(self.direction[i]-pi/6)*60]
                self.eyes[0] = [self.points_list[i][0] + math.cos(self.direction[i]+4*pi/3)*30, self.points_list[i][1] + math.sin(self.direction[i]+4*pi/3)*30]
                self.eyes[1] = [self.points_list[i][0] + math.cos(self.direction[i]-4*pi/3)*30, self.points_list[i][1] + math.sin(self.direction[i]-4*pi/3)*30]
            else:
                length = 1-(self.radi_list[i]/sqrt)
                direction_x, direction_y = self.points_list[i-1][0] - self.points_list[i][0], self.points_list[i-1][1] - self.points_list[i][1]
                self.direction[i] = math.atan2(direction_y, direction_x)
                self.points_list[i][0] += length*(direction_x)
                self.points_list[i][1] += length*(direction_y)
            # calculates position of points
            self.body_points_left[i] = [self.points_list[i][0] + math.cos(self.direction[i]-pi/2)*self.sizes_list[i], self.points_list[i][1] + math.sin(self.direction[i]-pi/2)*self.sizes_list[i]]
            self.body_points_right[i] = [self.points_list[i][0] + math.cos(self.direction[i]+pi/2)*self.sizes_list[i], self.points_list[i][1] + math.sin(self.direction[i]+pi/2)*self.sizes_list[i]]
            # moves the side circles
            # drawing_points = [self.body_points_left[i][0]-5, self.body_points_left[i][1]-5]
            # canvas.moveto(self.side_canvas[i*2], *drawing_points)
            # drawing_points = [self.body_points_right[i][0]-5, self.body_points_right[i][1]-5]
            # canvas.moveto(self.side_canvas[i*2+1], *drawing_points)
            # if i == 0:
            #     print(self.direction[i])
            #     print(self.direction[i]-pi/2)
            #     print(self.direction[i]+pi/2)

            # moves rigging circles
            # canvas.moveto(self.rigged_canvas[i], int(self.points_list[i][0] - self.radi_list[i]), int(self.points_list[i][1] - self.radi_list[i]))
            # moves body circles
            # canvas.moveto(self.body_canvas[i], int(self.points_list[i][0] - self.sizes_list[i]), int(self.points_list[i][1] - self.sizes_list[i]))

        # moves polygon body shape
        self.body_points_right.reverse()
        canvas.coords(self.body, self.head + self.body_points_left + self.body_points_right)
        self.body_points_right.reverse()
        canvas.moveto(self.eyes_canvas[0], self.eyes[0][0] - 10, self.eyes[0][1] - 10)
        canvas.moveto(self.eyes_canvas[1], self.eyes[1][0] - 10, self.eyes[1][1] - 10)
    def __del__(self):
        canvas.delete(self.body)
        canvas.delete(self.eyes_canvas[0])
        canvas.delete(self.eyes_canvas[1])

 # detect perpendicular and then create polygon
class Pet:
    def __init__(self):
        radi = [40, 40, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
        bodies = [35, 45, 35, 30, 30, 29, 29, 28, 28, 27, 27, 26, 26, 25, 25, 24, 24, 23, 23, 22, 22, 21, 21, 20, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
        self.spine = Spine(40, radi, bodies, window.winfo_pointerx(), window.winfo_pointery())
        window.after(100, programloop)
    def update(self):
        self.spine.update(window.winfo_pointerx(), window.winfo_pointery())
    def __del__(self):
        del self.spine


class UI:
    def __init__(self):
        self.current_page = ""
        self.pet_frame = ""
        self.edit_frame = ""
        self.organisation_frame = ""
        self.buttons = []
        self.buttons_customize = ["Pet Select", "Pet Edit", "Organisation", "Quit"]
        self.create_buttons()
    def create_buttons(self):
        global pet
        if pet != 0:
            del pet
        pet = 0
        for i in range(4):
            button = tk.Button(canvas, height=1, width=10, bg="red", command= lambda: self.switch_page(self.buttons_customize[i]), text=self.buttons_customize[i], fg="white", font="Arial 18 bold")
            print(button.cget)
            button.place(x=750 + i*200, y=750)
            self.buttons.append(button)
        # for i in self.buttons:
        #     print(i.command)
    def pet_select(self):
        self.pet_frame = ttk.Frame(canvas, padding=5, borderwidth=2, style="frame.TFrame")
        self.pet_frame.place(x=screen_width-425, y=25, width=400, height=700)
        title = ttk.Label(self.pet_frame, text="Pet Selection", font="Arial 24 bold")
        title.grid(column=0, row=0)
        snake_row = ttk.Frame(self.pet_frame, padding=5, borderwidth=2, style="pet_option.TFrame")
        snake_row.grid(column=0, row=1)
        snake_image = tk.Canvas(snake_row, width=100, height=100)
        snake_image.grid(column=0, row=0)
        snake_image.create_rectangle(4,4,100,100, outline= 'black', width=4)
        snake_label = ttk.Label(snake_row, text="Snake", padding=50, font="Arial 18 bold", background="grey80")
        snake_label.grid(column=1, row=0)
        snake_button = tk.Button(snake_row, text="Snake", font="Arial 18 bold", command= lambda: self.choose_pet())
        snake_button.grid(column=2, row=0)
    def pet_edit(self):
        self.edit_frame = ttk.Frame(canvas, padding=5, borderwidth=2, style="frame.TFrame")
        self.edit_frame.place(x=screen_width-1225, y=25, width=1200, height=700)
        title = ttk.Label(self.edit_frame, text="Pet Selection", font="Arial 24 bold")
        title.grid(column=0, row=0)
    def organisation(self):
        print("sdf")
    def switch_page(self, page):
        print(page)
        if page == "Quit":
            window.destroy()
        elif page == "Pet Select":
            self.pet_select()
        elif page == "Pet Edit":
            self.pet_edit()
        elif page == "Organisation":
            self.organisation()
        if self.current_page == "Pet Select" and self.pet_frame != "":
            self.pet_frame.place_forget()
        elif self.current_page == "Pet Edit" and self.edit_frame != "":
            self.edit_frame.place_forget()
        elif self.current_page == "Organisation" and self.organisation_frame != "":
            self.organisation_frame.place_forget
        self.current_page = page

    def choose_pet(self):
        global pet
        pet = Pet()
        self.pet_frame.place_forget()
        for b in self.buttons:
            b.place_forget()

# class Path():
#     def __init__(self):
#         self.points = []
#         self.direction = [[50, 50], [50, 50], [50, 50]]
#         self.distance = [2, 2, 2]
#         self.colour = [colour_1, colour_2, colour_3, colour_4, colour_5, colour_6, colour_7, colour_8, colour_9]
#         self.bezier_points = []
#         for i in range(3):
#             # drawing_points = [self.points[i][0], self.points[i][1], self.tweenpoints[i][0], self.tweenpoints[i][1]]
#             # line = canvas.create_line(drawing_points, fill=self.colour[i], width=2)
#             # self.direction_canvas.append(line)
#             node = Node(random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT), self.colour[i], self.colour[i+6], self.colour[i+3])
#             self.points.append(node)

#         for i in range(101):
#             t = i/100
#             p1 = (1-t)**3
#             p2 = 3*t*(1-t)**2
#             p3 = 3*(t**2)*(1-t)
#             p4 = t**3
#             point = [self.points[0].x*p1 + self.points[0].post_x*p2 + self.points[1].pre_x*p3 + self.points[1].x*p4, self.points[0].y*p1 + self.points[0].post_y*p2 + self.points[1].pre_y*p3 + self.points[1].y*p4]
#             self.bezier_points.append(point)
#             point = [self.points[1].x*p1 + self.points[1].post_x*p2 + self.points[2].pre_x*p3 + self.points[2].x*p4, self.points[1].y*p1 + self.points[1].post_y*p2 + self.points[2].pre_y*p3 + self.points[2].y*p4]
#             self.bezier_points.append(point)
#         for p in self.bezier_points:
#             draw.circle(screen, WHITE, [p[0], p[1]], 2)
#     def update(self):
#         for p in self.points:
#             p.drag(mouse_x, mouse_y)
#         self.bezier_points = []
#         for i in range(101):
#             t = i/100
#             p1 = (1-t)**3
#             p2 = 3*t*(1-t)**2
#             p3 = 3*(t**2)*(1-t)
#             p4 = t**3
#             point = [self.points[0].x*p1 + self.points[0].post_x*p2 + self.points[1].pre_x*p3 + self.points[1].x*p4, self.points[0].y*p1 + self.points[0].post_y*p2 + self.points[1].pre_y*p3 + self.points[1].y*p4]
#             self.bezier_points.append(point)
#             point = [self.points[1].x*p1 + self.points[1].post_x*p2 + self.points[2].pre_x*p3 + self.points[2].x*p4, self.points[1].y*p1 + self.points[1].post_y*p2 + self.points[2].pre_y*p3 + self.points[2].y*p4]
#             self.bezier_points.append(point)
#     def randomize(self):
#         for i in self.points:
#             i.x, i.y = random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)
#             i.pre_x, i.pre_y = i.x + math.cos(i.pre_angle)*i.pre_length, i.y + math.sin(i.pre_angle)*i.pre_length
#             i.post_x, i.post_y = i.x + math.cos(i.post_angle)*i.post_length, i.y + math.sin(i.post_angle)*i.pre_length
#         self.update()

#     def draw(self, screen):
#         for p in self.points:
#             p.draw(screen)
#         for p in self.bezier_points:
#             draw.circle(screen, WHITE, [p[0], p[1]], 2)

# class Node:
#     def __init__(self, pos_x, pos_y, colour, pre_colour, post_colour):
#         self.x, self.y = pos_x, pos_y
#         self.radius = 10
#         self.clickstate = False
#         self.pre_clickstate = False
#         self.post_clickstate = False
#         self.colour = colour
#         self.pre_colour = pre_colour
#         self.post_colour = post_colour
#         self.pre_length = 50
#         self.post_length = 50
#         self.pre_angle = pi
#         self.post_angle = 0
#         self.pre_x, self.pre_y = self.x + math.cos(self.pre_angle)*self.pre_length, self.y + math.sin(self.pre_angle)*self.pre_length
#         self.post_x, self.post_y = self.x + math.cos(self.post_angle)*self.post_length, self.y + math.sin(self.post_angle)*self.pre_length
        
#     def click(self, m_x, m_y):
#         if math.sqrt((m_x-self.x)**2+(m_y-self.y)**2) < self.radius:
#             self.clickstate = True
#         elif math.sqrt((m_x-self.pre_x)**2+(m_y-self.pre_y)**2) < self.radius:
#             self.pre_clickstate = True
#         elif math.sqrt((m_x-self.post_x)**2+(m_y-self.post_y)**2) < self.radius:
#             self.post_clickstate = True
#     def unclick(self):
#         self.clickstate = False
#         self.pre_clickstate = False
#         self.post_clickstate = False
#     def drag(self, m_x, m_y):
#         if self.clickstate == True:
#             self.x, self.y = m_x, m_y
#             self.pre_x, self.pre_y = self.x + math.cos(self.pre_angle)*self.pre_length, self.y + math.sin(self.pre_angle)*self.pre_length
#             self.post_x, self.post_y = self.x + math.cos(self.post_angle)*self.post_length, self.y + math.sin(self.post_angle)*self.pre_length
#         elif self.pre_clickstate == True:
#             self.pre_x, self.pre_y = m_x, m_y
#             self.pre_length = math.sqrt((self.pre_x-self.x)**2+(self.pre_y-self.y)**2)
#             self.pre_angle = math.atan2((self.pre_y-self.y), (self.pre_x-self.x))
#             self.post_angle = self.pre_angle - pi
#             self.post_x, self.post_y = self.x + math.cos(self.post_angle)*self.post_length, self.y + math.sin(self.post_angle)*self.pre_length
#         elif self.post_clickstate == True:
#             self.post_x, self.post_y = m_x, m_y
#             self.post_length = math.sqrt((self.post_x-self.x)**2+(self.post_y-self.y)**2)
#             self.post_angle = math.atan2((self.post_y-self.y), (self.post_x-self.x))
#             self.pre_angle = self.post_angle - pi
#             self.pre_x, self.pre_y = self.x + math.cos(self.pre_angle)*self.pre_length, self.y + math.sin(self.pre_angle)*self.pre_length

    # def draw(self, screen):
    #     draw.circle(screen, self.colour, [self.x, self.y], self.radius, 4)
    #     draw.circle(screen, self.pre_colour, [self.pre_x, self.pre_y], self.radius, 4)
    #     draw.circle(screen, self.post_colour, [self.post_x, self.post_y], self.radius, 4)

def programloop(): # main loop
    if pet != 0:
        pet.update()
    window.after(1000, programloop)

def check_key(event): # check what key was pressed
    if event.keysym == "p":
        ui.create_buttons()

# creating window / fullscreen / top overlay
window = tk.Tk()
window.attributes('-fullscreen', True)
window.attributes('-topmost', True)
s = ttk.Style()
s.configure("frame.TFrame", background="white")
s.configure("pet_option.TFrame", background="grey80")
# set height and width variables
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

#set up black canvas
canvas = tk.Canvas(window, bg='grey15', highlightthickness=0)
canvas.pack(fill="both", expand=True)
window.wm_attributes('-transparentcolor', 'grey15') # make black transparent

#global
pet = 0
ui = UI()
# event bindings
window.bind("<KeyPress>", check_key)

window.mainloop() # checks events

