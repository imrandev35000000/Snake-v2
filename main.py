from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50
SPEED = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
#seting the constents



class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_derection(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass
#adding functions

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)

window.mainloop()
#windows creating


