from tkinter import *
import random
import os
import sys

# class snack
class Snack:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []
        
        for i in range(0, BODY_SIZE):
            self.coordinates.append([0, 0])
        
        for x, y in self.coordinates:
            square = convas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNACK_COLOR)
            self.squares.append(square)

# class food
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) -1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) -1) * SPACE_SIZE
        self.coordinates = [x, y]
        convas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag="food")

# next_direction 
def next_direction(snack, food):
    x,y = snack.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    
    snack.coordinates.insert(0, [x,y])
    square = convas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNACK_COLOR)
    snack.squares.insert(0, square)
    
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text = f"score : {score}")
        convas.delete("food")
        food = Food()
    else:
        del snack.coordinates[-1]
        convas.delete(snack.squares[-1])
        del snack.squares[-1]
    
    if check_game_over():
        game_over()
    else:
        window.after(SLOWNESS, next_direction, snack, food)
        


# change direction
def change_direction(new_dir):
    global direction
    if new_dir == "left":
        if direction != "right":
            direction = new_dir
    elif new_dir == "right":
        if direction != "left":
            direction = new_dir
    elif new_dir == "up":
        if direction != "down":
            direction = new_dir
    elif new_dir == "down":
        if direction != "up":
            direction = new_dir

# check game over
def check_game_over(snack):
    x, y = snack.coordinates[0]
    if x < 0 or x > GAME_WIDTH:
        return True
    if y < 0 or y > GAME_HEIGHT:
        return True
    
    for sq in snack.coordinates[1:]:
        if x == sq[0] and y == sq[1]:
            return True
    return False

# game over
def game_over():
    convas.delete(ALL)
    convas.create_text(convas.winfo_width() / 2, convas.winfo_height() / 2, font =("terminal", 60),
    text = "GAME OVER", fill = "red", tag="gameover")

# restart game function
def restart_game():
    path = sys.executable
    os.execl(path, path, *sys.argv)


# ------------ const variable -------------
# GAME_WIDTH = 700
# GAME_HEIGHT = 700
GAME_WIDTH = 400
GAME_HEIGHT = 400
SPACE_SIZE = 30
SLOWNESS = 200
BODY_SIZE = 2
SNACK_COLOR = "yellow"
BAKCGROUND_COLOR = "black"
FOOD_COLOR = "red"
score = 0
direction = "down"
# ----------------------------------------

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

label = Label(window, text="Score: 0", font=("Arial", 20))
label.pack()

convas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BAKCGROUND_COLOR)
convas.pack()

restart = Button(window, text="RESTART", fg="white", bg="red" , command=lambda: restart_game())
restart.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
print(x, y)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))


snack = Snack()
food = Food()
next_direction(snack, food)

window.mainloop()
