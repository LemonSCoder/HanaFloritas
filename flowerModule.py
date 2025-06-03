import random
import turtle
import math
global flower_turtle
global screen
class flower:
    def __init__(self, message, petal_num, flower_num, flower_type):
        self.message = message
        self.petal_num = petal_num
        self.flower_num = flower_num
        self.flower_type = flower_type
    def get_flower(self):
        flower_names = {
        "Rose" : ["lov", "royal", "beau", "secre"], "Daffodil" : ["birth", "new", "hope", "joy", "luck"], "Carnation" : ["devot", "lov", "fascina"], "Lily" : ["lov", "pur", "fertil", "birth"], "Daisy" : ["pur", "birth", "new", "cheer"], "Tulip" : ["birth", "perfect", "lov"], "Random" : [],
        }
        screen = turtle.Screen()
        flower_turtle = turtle.Turtle()
        screen.clear()
        screen.bgcolor("skyblue")
        for flower in flower_names.keys():
            if self.flower_type == flower.lower():
                if self.flower_type == "rose":
                    flower_numbers = 0
                    while flower_numbers < int(self.flower_num[2]):
                        location_x = random.randint(-250, 250)
                        location_y = random.randint(-250, 250)
                        #Used ChatGPT to generate a portion of the flowers I created
                        rose_colors = [["red", "crimson"], ["orange", "chocolate"], ["yellow", "goldenrod"], ["lavender", "orchid"], ["hot pink", "deep pink"], ["white", "lavender"], ["black", "dim gray"]]
                        flower_turtle.speed(20)
                        flower_turtle.color("green")    
                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y-20)
                        flower_turtle.right(90)
                        flower_turtle.pendown()
                        flower_turtle.pensize(15)
                        flower_turtle.forward(300)
                        rose_color_choice = random.choice(rose_colors)
                        flower_turtle.pensize(5)
                        flower_turtle.color(rose_color_choice[1])
                        flower_turtle.left(90)
                        def draw_petals():
                            for i in range(int(self.petal_num[2])):
                                flower_turtle.penup()
                                flower_turtle.goto(location_x, (location_y-20))
                                flower_turtle.pendown()
                                flower_turtle.fillcolor(rose_color_choice[0])
                                flower_turtle.begin_fill()
                                flower_turtle.circle(150, 60)
                                flower_turtle.left(120)
                                flower_turtle.circle(150, 60)
                                flower_turtle.left(120)
                                flower_turtle.end_fill()
                                flower_turtle.left(180 / int(self.petal_num[2]))

                        def draw_bud():
                            flower_turtle.penup()
                            flower_turtle.goto(location_x, location_y-20)
                            flower_turtle.pendown()
                            flower_turtle.fillcolor(rose_color_choice[0])
                            flower_turtle.begin_fill()
                            flower_turtle.circle(85)
                            flower_turtle.end_fill()
                            flower_turtle.right(270)
                            flower_turtle.penup()
                            flower_turtle.goto(location_x-60, location_y+125)
                            flower_turtle.pendown()
                            flower_turtle.right(180)
                            flower_turtle.begin_fill()
                            flower_turtle.circle(60, 180)
                            flower_turtle.end_fill()
                            flower_turtle.penup()
                            flower_turtle.goto(location_x+50, location_y+100)
                            flower_turtle.pendown()
                            flower_turtle.begin_fill()
                            flower_turtle.circle(50, 180)
                            flower_turtle.end_fill()
                            flower_turtle.left(90)
                        draw_bud()
                        draw_petals()
                        flower_turtle.left(180)
                        flower_numbers += 1
                elif self.flower_type == "daffodil":
                    flower_numbers = 0
                    while flower_numbers < int(self.flower_num[2]):
                        location_x = random.randint(-500, 500)
                        location_y = random.randint(-500, 500)
                        flower_turtle = turtle.Turtle()
                        flower_turtle.speed(20)
                        flower_turtle.color("green")    
                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y-20)
                        flower_turtle.right(90)
                        flower_turtle.pendown()
                        flower_turtle.pensize(15)
                        flower_turtle.forward(600)
                        flower_turtle.color("yellow")
                        flower_turtle.left(90)
                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y)
                        flower_turtle.pendown()

                        def draw_petal():
                            flower_turtle.begin_fill()
                            flower_turtle.circle(150, 60)
                            flower_turtle.left(120)
                            flower_turtle.circle(150, 60)
                            flower_turtle.left(120)
                            flower_turtle.end_fill()

                        def draw_petal_3():
                            flower_turtle.begin_fill()
                            flower_turtle.circle(20)
                            flower_turtle.left(90)
                            flower_turtle.circle(20)
                            flower_turtle.left(90)
                            flower_turtle.end_fill()

                        for i in range(int(self.petal_num[2])):
                            degree_turns = 360 / (int(self.petal_num[2]))
                            draw_petal()
                            flower_turtle.right(degree_turns)

                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y)
                        flower_turtle.pendown()
                        flower_turtle.right(30)
                        flower_turtle.color("orange red")
                        for i in range(6):
                            draw_petal_3()
                            flower_turtle.right(60)

                        flower_turtle.penup()
                        flower_turtle.goto(location_x-10, location_y-20)
                        flower_turtle.pendown()
                        flower_turtle.color("tomato")
                        flower_turtle.begin_fill()
                        flower_turtle.circle(20)
                        flower_turtle.end_fill()
                        flower_numbers += 1
                elif self.flower_type == "carnation":
                    flower_numbers = 0
                    while flower_numbers < int(self.flower_num[2]):
                        location_x = random.randint(-500, 500)
                        location_y = random.randint(-500, 500)
                        screen.bgcolor("skyblue")
                        flower_turtle = turtle.Turtle()
                        flower_turtle.speed(20)

                        flower_turtle.color("green")
                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y-20)
                        flower_turtle.right(90)
                        flower_turtle.pendown()
                        flower_turtle.pensize(15)
                        flower_turtle.forward(600)

                        flower_turtle.color("deep pink")
                        flower_turtle.left(90)
                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y)
                        flower_turtle.pendown()

                        def draw_petal():
                            flower_turtle.begin_fill()
                            flower_turtle.circle(62.5)
                            flower_turtle.left(90)
                            flower_turtle.circle(62.5)
                            flower_turtle.left(90)
                            flower_turtle.end_fill()

                        def draw_petal_2():
                            flower_turtle.begin_fill()
                            flower_turtle.circle(50)
                            flower_turtle.left(90)
                            flower_turtle.circle(50)
                            flower_turtle.left(90)
                            flower_turtle.end_fill()

                        def draw_petal_3():
                            flower_turtle.begin_fill()
                            flower_turtle.circle(37.5)
                            flower_turtle.left(90)
                            flower_turtle.circle(37.5)
                            flower_turtle.left(90)
                            flower_turtle.end_fill()

                        for i in range(int(self.petal_num[2])):
                            degree_turns = 360 / (int(self.petal_num[2]))
                            draw_petal()
                            flower_turtle.right(degree_turns)

                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y)
                        flower_turtle.pendown()
                        flower_turtle.right(30)
                        flower_turtle.color("hot pink")
                        for i in range(int(self.petal_num[2])):
                            degree_turns = 360 / (int(self.petal_num[2]))
                            draw_petal_2()
                            flower_turtle.right(degree_turns)

                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y)
                        flower_turtle.pendown()
                        flower_turtle.right(30)
                        flower_turtle.color("pale violet red")
                        for i in range(int(self.petal_num[2])):
                            degree_turns = 360 / (int(self.petal_num[2]))
                            draw_petal_3()
                            flower_turtle.right(degree_turns)
                        flower_numbers += 1
                elif self.flower_type == "lily":
                    flower_numbers = 0
                    while flower_numbers < int(int(str(self.flower_num[2]))):
                        location_x = random.randint(-500, 500)
                        location_y = random.randint(-500, 500)

                        flower_turtle = turtle.Turtle()
                        flower_turtle.speed(20)

                        flower_turtle.color("green")
                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y-20)
                        flower_turtle.right(90)
                        flower_turtle.pendown()
                        flower_turtle.pensize(15)
                        flower_turtle.forward(600)

                        flower_turtle.color("deep pink")
                        flower_turtle.left(90)
                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y)
                        flower_turtle.pendown()

                        def draw_petal():
                            flower_turtle.begin_fill()
                            flower_turtle.circle(150, 60)
                            flower_turtle.left(120)
                            flower_turtle.circle(150, 60)
                            flower_turtle.left(120)
                            flower_turtle.end_fill()

                        for i in range(int(self.petal_num[2])):
                            degree_turns = 360 / (int(self.petal_num[2]))
                            draw_petal()
                            flower_turtle.right(degree_turns)

                        def circle():
                            flower_turtle.begin_fill()
                            flower_turtle.circle(10)
                            flower_turtle.end_fill()

                        flower_turtle.color("orange red")
                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y-30)
                        flower_turtle.pendown()
                        circle()
                        flower_turtle.penup()
                        flower_turtle.goto(location_x-30, location_y)
                        flower_turtle.pendown()
                        circle()
                        flower_turtle.penup()
                        flower_turtle.goto(location_x+30, location_y)
                        flower_turtle.pendown()
                        circle()
                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y+30)
                        flower_turtle.pendown()
                        circle()
                        flower_numbers += 1
                elif self.flower_type == "daisy":
                    flower_numbers = 0
                    while flower_numbers < int(self.flower_num[2]):
                        location_x = random.randint(-500, 500)
                        location_y = random.randint(-500, 500)
                        flower_turtle = turtle.Turtle()
                        flower_turtle.speed(20)

                        flower_turtle.color("green")
                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y-20)
                        flower_turtle.right(90)
                        flower_turtle.pendown()
                        flower_turtle.pensize(15)
                        flower_turtle.forward(600)

                        flower_turtle = turtle.Turtle()
                        flower_turtle.speed(20)

                        flower_turtle.color("white")
                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y)
                        flower_turtle.pendown()

                        def draw_petal():
                            flower_turtle.begin_fill()
                            flower_turtle.circle(150, 60)
                            flower_turtle.left(120)
                            flower_turtle.circle(150, 60)
                            flower_turtle.left(120)
                            flower_turtle.end_fill()

                        for i in range(int(self.petal_num[2])):
                            degree_turns = 360 / (int(self.petal_num[2]))
                            draw_petal()
                            flower_turtle.right(degree_turns)

                        flower_turtle.penup()
                        flower_turtle.goto(location_x, location_y-30)
                        flower_turtle.pendown()
                        flower_turtle.color("yellow")
                        flower_turtle.begin_fill()
                        flower_turtle.circle(30)
                        flower_turtle.end_fill() 
                        flower_numbers += 1             
                elif self.flower_type == "random":
                    screen.bgcolor("skyblue")
                    flower_turtle = turtle.Turtle()
                    flower_turtle.speed(20)
                    flower_turtle.color("green")
                    flower_turtle.penup()
                    flower_turtle.goto(0, -20)
                    flower_turtle.right(90)
                    flower_turtle.pendown()
                    flower_turtle.pensize(15)
                    flower_turtle.forward(600)
                    color_list = ["red", "orange", "blue", "indigo", "purple", "pink", "brown", "white", "black"]
                    flower_turtle.left(90)
                    flower_turtle.penup()
                    flower_turtle.goto(0, 0)
                    flower_turtle.pendown()
                    def draw_petal():
                        flower_turtle.color(random.choice(color_list))
                        flower_turtle.begin_fill()
                        flower_turtle.circle(150, 60)
                        flower_turtle.left(120)
                        flower_turtle.circle(150, 60)
                        flower_turtle.left(120)
                        flower_turtle.end_fill()
                    for i in range(6):
                        draw_petal()
                        flower_turtle.right(60)
                    flower_turtle.penup()
                    flower_turtle.goto(0, -30)
                    flower_turtle.pendown()
                    flower_turtle.color("yellow")
                    flower_turtle.begin_fill()
                    flower_turtle.circle(30)
                    flower_turtle.end_fill()
    def __repr__(self):
        return "There you go! {} {} flower(s) with {} petals!".format(self.flower_num, self.flower_type, self.petal_num)
