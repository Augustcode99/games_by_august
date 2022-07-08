from tkinter import *
import random

GAME_WIDTH = 900
GAME_HEIGHT = 600
SPEED = 150
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "#9F009F" 
FOOD_COLOR = "#00A600"
BACKGROUND_COLOR = "#000000"
gameover = False
high_score = 0
score = 0


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y +
                           SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score
        score += 1
        label.config(text=f"\t   Score:{score}          " , font=("consolas", 44), bg="black", fg="#0007D4")

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):

    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    global gameover
    global label
    gameover = True

    canvas.delete(ALL)
    BODY_PARTS = 3
    global score
    global high_score
    if score > high_score:
        high_score = score
    score = 0   
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=("consolas", 70), text="GAME OVER", fill="#AE0000", tag="over")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/25,
                       font=("consolas", 25), text=f"Your highscore is: {high_score}", fill="white", tag="over")                   
    canvas.create_text(canvas.winfo_width()/3, canvas.winfo_height()/3,
                       font=("consolas", 30), text="\t     spacebar to restart", fill="white", tag="over")
    
def restart():
    global gameover
    if gameover == False:
        pass
    elif gameover == True:
        global direction
        global canvas
        global score
        global label
        label.config(text = "\t   Score:0          ", font=("consolas", 44), bg="black", fg="#0007D4", justify=CENTER)
        canvas.delete(ALL)
        score = 0
        direction = "down"
        snake = Snake()
        food = Food()
        next_turn(snake, food)
        gameover = False

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text=f"\t   Score:{score}          ", font=("consolas", 44), bg="black", fg="#0007D4", justify=CENTER)
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR,
                height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<space>", lambda event: restart())

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()