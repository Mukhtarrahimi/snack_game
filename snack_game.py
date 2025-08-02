from tkinter import *
import random

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
# restart game function
def restart_game():
    pass


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

snack = Snack()
food = Food()

window.mainloop()
