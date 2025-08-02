from tkinter import *
import random
import os
import sys
import pygame

# --------- Consts ----------
GAME_WIDTH = 400
GAME_HEIGHT = 400
SPACE_SIZE = 30
SLOWNESS = 200
BODY_SIZE = 2
SNACK_COLOR = "yellow"
BACKGROUND_COLOR = "black"
FOOD_COLOR = "red"
SCORE_FILE = "highscore.txt"

score = 0
high_score = 0
direction = "down"
paused = False
# ---------------------------

# load high score
def load_high_score():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as file:
            return int(file.read().strip())
    return 0

# save high score
def save_high_score():
    with open(SCORE_FILE, "w") as file:
        file.write(str(high_score))

# play sound
def play_sound(event):
    if event == "eat":
        pygame.mixer.Sound("eat.wav.mp3").play()
    elif event == "gameover":
        pygame.mixer.Sound("gameover.wav.mp3").play()

# class Snack
class Snack:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []

        for i in range(BODY_SIZE):
            self.coordinates.append([i * SPACE_SIZE, 0])

        for x, y in self.coordinates:
            square = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNACK_COLOR)
            self.squares.append(square)

# class Food
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# next_direction
def next_direction(snack, food):
    global score, SLOWNESS, paused, high_score

    if paused:
        window.after(SLOWNESS, next_direction, snack, food)
        return

    x, y = snack.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snack.coordinates.insert(0, [x, y])
    square = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNACK_COLOR)
    snack.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        play_sound("eat")
        if score > high_score:
            high_score = score
            save_high_score()
        label.config(text=f"Score: {score}  |  High Score: {high_score}")
        canvas.delete("food")
        food = Food()
        if SLOWNESS > 50:
            SLOWNESS -= 5
    else:
        del snack.coordinates[-1]
        canvas.delete(snack.squares[-1])
        del snack.squares[-1]

    if check_game_over(snack):
        game_over()
    else:
        window.after(SLOWNESS, next_direction, snack, food)

# change_direction
def change_direction(new_dir):
    global direction
    if new_dir == "left" and direction != "right":
        direction = new_dir
    elif new_dir == "right" and direction != "left":
        direction = new_dir
    elif new_dir == "up" and direction != "down":
        direction = new_dir
    elif new_dir == "down" and direction != "up":
        direction = new_dir

# check_game_over
def check_game_over(snack):
    x, y = snack.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for coord in snack.coordinates[1:]:
        if x == coord[0] and y == coord[1]:
            return True

    return False

# game_over
def game_over():
    play_sound("gameover")
    canvas.delete(ALL)
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2,
                       font=("Arial", 40), text="GAME OVER", fill="red", tag="gameover")

# restart_game
def restart_game():
    path = sys.executable
    os.execl(path, path, *sys.argv)

# toggle_pause
def toggle_pause(event=None):
    global paused
    paused = not paused
    if not paused:
        next_direction(snack, food)

# ----------- UI -----------
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

pygame.mixer.init()

high_score = load_high_score()

label = Label(window, text=f"Score: 0  |  High Score: {high_score}", font=("Arial", 16))
label.pack()

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

restart_btn = Button(window, text="RESTART", fg="white", bg="red", command=restart_game)
restart_btn.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<space>", toggle_pause)

snack = Snack()
food = Food()
next_direction(snack, food)

window.mainloop()
