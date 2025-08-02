from tkinter import *

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

restart = Button(window, text="RESTART", fg="white", command=lambda: restart_game())
restart.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.mainloop()
