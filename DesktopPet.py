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
            button = tk.Button(canvas, height=1, width=10, bg="red", command= lambda x=self.buttons_customize[i]: self.switch_page(x), text=self.buttons_customize[i], fg="white", font="Arial 18 bold")
            button.place(x=750 + i*200, y=750)
            self.buttons.append(button)
    def pet_select(self, x_distance, event):
        self.pet_frame = ttk.Frame(canvas, padding=5, borderwidth=2, style="frame.TFrame")
        self.pet_frame.place(x=x_distance-425, y=25, width=400, height=700)
        title = ttk.Label(self.pet_frame, text="Pet Selection", font="Arial 24 bold")
        title.grid(column=0, row=0)
        snake_row = ttk.Frame(self.pet_frame, padding=5, borderwidth=2, style="pet_option.TFrame")
        snake_row.grid(column=0, row=1)
        snake_image = tk.Canvas(snake_row, width=100, height=100)
        snake_image.grid(column=0, row=0)
        snake_image.create_rectangle(4,4,100,100, outline= 'black', width=4)
        snake_label = ttk.Label(snake_row, text="Snake", padding=40, font="Arial 18 bold", background="grey80")
        snake_label.grid(column=1, row=0)
        snake_button = tk.Button(snake_row, text="Choose", font="Arial 18 bold", command=event)
        snake_button.grid(column=2, row=0)
    def pet_edit(self):
        self.pet_select(450, self.edit_choose)
        self.edit_frame = ttk.Frame(canvas, padding=5, borderwidth=2, style="frame.TFrame")
        self.edit_frame.place(x=screen_width-1075, y=25, width=1050, height=700)
        title = ttk.Label(self.edit_frame, text="Pet Edit", font="Arial 24 bold")
        title.grid(column=0, row=0)
        self.properties_edit = ttk.Frame(self.edit_frame, padding=5, borderwidth=2, style="properties_edit.TFrame")
        self.properties_edit.grid(column=0, row=1)
        path_edit = tk.Button(self.properties_edit, text="Edit Path", font="Arial 18 bold", command=self.path_creation)
        path_edit.grid(column=0, row=10)
    def edit_choose(self):
        print("sdfsdf")
    def path_creation(self):
        global path
        self.edit_frame.place_forget()
        self.pet_frame.place_forget()
        path = Path()
        for b in self.buttons:
            b.place_forget()
        canvas.configure(bg="white")
        button = tk.Button(canvas, height=1, width=10, bg="red", command=self.exit_path_creation, text="Cancel", fg="white", font="Arial 18 bold")
        button.place(x=1350, y=750)
        self.buttons.append(button)
    def exit_path_creation(self):
        global path
        self.buttons[0].place_forget()
        canvas.configure(bg="grey15")
        del path
        path = ""
        self.create_buttons()
    def organisation(self):
        self.organisation_frame = ttk.Frame(canvas, padding=5, borderwidth=2, style="frame.TFrame")
        self.organisation_frame.place(x=screen_width-1075, y=25, width=1050, height=700)
    def switch_page(self, page):
        if self.current_page == "Pet Select":
            self.pet_frame.place_forget()
        elif self.current_page == "Pet Edit":
            self.edit_frame.place_forget()
            self.pet_frame.place_forget()
        elif self.current_page == "Organisation":
            self.organisation_frame.place_forget()
        if page == "Quit":
            window.destroy()
        elif page == "Pet Select":
            self.pet_select(screen_width, self.pet_create)
        elif page == "Pet Edit":
            self.pet_edit()
        elif page == "Organisation":
            self.organisation()
        self.current_page = page
    def pet_create(self):
        global pet, screen_state, path
        self.pet_frame.place_forget()
        pet = Pet()
        screen_state = True
        for b in self.buttons:
            b.place_forget()


class Path:
    def __init__(self):
        self.points = []
        self.point_counter = 0
        self.colour = ["red", "green", "blue"]
        for i in range(3):
            point = Node(100 + i*100, 100 + i*100, self.colour[i])
            self.points.append(point)
        # self.direction = [[50, 50], [50, 50], [50, 50]]
        # self.distance = [2, 2, 2]
        # self.colour = [colour_1, colour_2, colour_3, colour_4, colour_5, colour_6, colour_7, colour_8, colour_9]
        # self.bezier_points = []
        # for i in range(3):
        #     # drawing_points = [self.points[i][0], self.points[i][1], self.tweenpoints[i][0], self.tweenpoints[i][1]]
        #     # line = canvas.create_line(drawing_points, fill=self.colour[i], width=2)
        #     # self.direction_canvas.append(line)
        #     node = Node(random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT), self.colour[i], self.colour[i+6], self.colour[i+3])
        #     self.points.append(node)

        # for i in range(101):
        #     t = i/100
        #     p1 = (1-t)**3
        #     p2 = 3*t*(1-t)**2
        #     p3 = 3*(t**2)*(1-t)
        #     p4 = t**3
        #     point = [self.points[0].x*p1 + self.points[0].post_x*p2 + self.points[1].pre_x*p3 + self.points[1].x*p4, self.points[0].y*p1 + self.points[0].post_y*p2 + self.points[1].pre_y*p3 + self.points[1].y*p4]
        #     self.bezier_points.append(point)
        #     point = [self.points[1].x*p1 + self.points[1].post_x*p2 + self.points[2].pre_x*p3 + self.points[2].x*p4, self.points[1].y*p1 + self.points[1].post_y*p2 + self.points[2].pre_y*p3 + self.points[2].y*p4]
        #     self.bezier_points.append(point)
        # for p in self.bezier_points:
        #     draw.circle(screen, WHITE, [p[0], p[1]], 2)
    def create_node(self, m_x, m_y):
        point = Node(m_x, m_y, self.colour[self.point_counter])
        self.points.append(point)
        del self.points[0]
        self.point_counter += 1
        if self.point_counter == 3:
            self.point_counter = 0
    def __del__(self):
        for i in self.points:
            del i
        
    # def update(self):
    #     for p in self.points:
    #         p.drag(mouse_x, mouse_y)
    #     self.bezier_points = []
    #     for i in range(101):
    #         t = i/100
    #         p1 = (1-t)**3
    #         p2 = 3*t*(1-t)**2
    #         p3 = 3*(t**2)*(1-t)
    #         p4 = t**3
    #         point = [self.points[0].x*p1 + self.points[0].post_x*p2 + self.points[1].pre_x*p3 + self.points[1].x*p4, self.points[0].y*p1 + self.points[0].post_y*p2 + self.points[1].pre_y*p3 + self.points[1].y*p4]
    #         self.bezier_points.append(point)
    #         point = [self.points[1].x*p1 + self.points[1].post_x*p2 + self.points[2].pre_x*p3 + self.points[2].x*p4, self.points[1].y*p1 + self.points[1].post_y*p2 + self.points[2].pre_y*p3 + self.points[2].y*p4]
    #         self.bezier_points.append(point)
    # def randomize(self):
    #     for i in self.points:
    #         i.x, i.y = random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT)
    #         i.pre_x, i.pre_y = i.x + math.cos(i.pre_angle)*i.pre_length, i.y + math.sin(i.pre_angle)*i.pre_length
    #         i.post_x, i.post_y = i.x + math.cos(i.post_angle)*i.post_length, i.y + math.sin(i.post_angle)*i.pre_length
    #     self.update()

    # def draw(self, screen):
    #     for p in self.points:
    #         p.draw(screen)
    #     for p in self.bezier_points:
    #         draw.circle(screen, WHITE, [p[0], p[1]], 2)

class Node:
    def __init__(self, pos_x, pos_y, colour):
        self.radius = 10
        self.clickstate = [False, False, False]
        self.canvas = []

        self.length = [50, 0, 50]
        self.angle = [pi, 0, 0]
        if colour == "red":
            self.colour = ["red4", "red", "tomato"]
        if colour == "green":
            self.colour = ["dark green", "lime green", "lawn green"]
        if colour == "blue":
            self.colour = ["navy", "blue", "deep sky blue"]
        self.x, self.y = [pos_x + math.cos(self.angle[0])*self.length[0], pos_x, pos_x + math.cos(self.angle[2])*self.length[2]], [pos_y + math.sin(self.angle[0])*self.length[0], pos_y, pos_y + math.sin(self.angle[2])*self.length[2]]

        for i in range(3):
            drawing_points = [self.x[i]-self.radius, self.y[i]-self.radius, self.x[i]+self.radius, self.y[i]+self.radius]
            self.canvas.append(canvas.create_oval(drawing_points, outline=self.colour[i], width=5))
        
        
    def click(self, m_x, m_y):
        if math.sqrt((m_x-self.x[1])**2+(m_y-self.y[1])**2) < self.radius:
            self.clickstate[1] = True
            return True
        elif math.sqrt((m_x-self.x[0])**2+(m_y-self.y[0])**2) < self.radius:
            self.clickstate[0] = True
            return True
        elif math.sqrt((m_x-self.x[2])**2+(m_y-self.y[2])**2) < self.radius:
            self.clickstate[2] = True
            return True

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
    def __del__(self):
        for i in self.canvas:
            canvas.delete(i)

def programloop(): # main loop
    global pet
    if pet != 0:
        pet.update()
    window.after(10, programloop)

def check_key(event): # check what key was pressed
    global screen_state
    if event.keysym == "p" and screen_state == True:
        ui.create_buttons()
        screen_state = False

def check_mouse(event): # check what key was pressed
    global path
    clicked_state = False
    print(event.widget)
    x, y = event.x, event.y
    if path != "":
        for p in path.points:
            if p.click(x, y) == True:
                clicked_state = True
                break
        if event.widget == canvas and clicked_state == False:
            path.create_node(x, y)

# creating window / fullscreen / top overlay
window = tk.Tk()
window.attributes('-fullscreen', True)
window.attributes('-topmost', True)
s = ttk.Style()
s.configure("frame.TFrame", background="white")
s.configure("pet_option.TFrame", background="grey80")
s.configure("properties_edit.TFrame", background="grey80")

#global
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
path = ""
pet = 0
screen_state = False

#set up black canvas
canvas = tk.Canvas(window, bg='grey15', highlightthickness=0)
canvas.pack(fill="both", expand=True)
window.wm_attributes('-transparentcolor', 'grey15') # make black transparent

#classes
ui = UI()

# event bindings
window.bind("<KeyPress>", check_key)
window.bind("<ButtonPress-1>", check_mouse)

window.mainloop() # checks events

