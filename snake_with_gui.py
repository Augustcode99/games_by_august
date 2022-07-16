from tkinter import *
from tkinter import ttk
import random

options = False
highscores = False
GAME_WIDTH = 900
GAME_HEIGHT = 540
SPEED = 130
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOR = "#9F009F" 
BACKGROUND_COLOR = "black"
gameover = False
high_score = 0
score = 0

highscore_1 = 0
highscore_2 = 0
highscore_3 = 0
highscore_4 = 0
highscore_5 = 0


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

        #canvas.create_oval(x, y, x + SPACE_SIZE, y +
                         # SPACE_SIZE, fill=FOOD_COLOR, tag="food")

        #canvas.create_image(x, y, x + SPACE_SIZE, y +
                           #SPACE_SIZE, fill=FOOD_COLOR, tag="food", image=apple)
        canvas.create_image(x, y, image=apple,anchor = NW, tag="food")

       


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

    # square = canvas.create_rectangle(
    #     x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    head = canvas.create_image(x, y, image=snakehead,anchor = NW, tag="snakehead")

         
    snake.squares.insert(0, head)

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
    global highscore_1
    global highscore_2
    global highscore_3
    global highscore_4
    global highscore_5
    if score > highscore_1:
        highscore_5 = highscore_4
        highscore_4 = highscore_3
        highscore_3 = highscore_2
        highscore_2 = highscore_1
        highscore_1 = score
    elif score > highscore_2:
        highscore_5 = highscore_4
        highscore_4 = highscore_3
        highscore_3 = highscore_2
        highscore_2 = score
    elif score > highscore_3:
        highscore_5 = highscore_4
        highscore_4 = highscore_3        
        highscore_3 = score
    elif score > highscore_4:
        highscore_5 = highscore_4
        highscore_4 = score
    elif score > highscore_5:
        highscore_5 = score
    score = 0   
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2.2,
                       font=("consolas", 60), text="GAME OVER", fill="#AE0000", tag="over")
    #canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/20,
                       #font=("consolas", 23), text=f"Your highscore is: {high_score}", fill="white", tag="over")                   
    # canvas.create_text(canvas.winfo_width()/3, canvas.winfo_height()/3,
    #                    font=("consolas", 30), text="\t     spacebar to restart", fill="white", tag="over")
    back_button = Button(canvas, image = button_image, background="black", activebackground="black",border=0, command=click_back)
    back_button.place(x=12,y=15)
    

def click_back():
    global highscores
    global options
    global gameover
    global label
    if highscores == True:
        hsframe.pack_forget()
        highscores = False
        frame.pack()
    if options == True:
        options_frame.pack_forget()
        options = False
        frame.pack()
    if gameover == True:
        try:
            canvas.destroy()
        finally:
            label.destroy()
            frame.place(x=0,y=0)
            image_label = ttk.Label(frame, image = start_image)
            image_label.place(x=0, y=0)

            game_title = ttk.Label(frame, text = "Snake Classic")
            game_title.place(x=250, y=25)

            start_button = ttk.Button(frame, text = "START", command = restart)
            start_button.place(x=350, y=330)
            high_button = ttk.Button(frame, text = "HIGHSCORES",command = hs_event)
            high_button.place(x=350, y=400)
            option_button = ttk.Button(frame, text = "SETTINGS",command = options_event)
            option_button.place(x=350, y=470)

    
def restart():
    global gameover
    if gameover == False:
        pass
    elif gameover == True:
        global direction
        global canvas
        global score
        global label
        global frame

        try:
            frame.pack_forget()
            canvas.delete("all")
        finally:
            label = Label(window, text=f"Score:{score}", font=("consolas", 44), bg="black", fg="#0007D4", justify=CENTER, width=28)
            label.pack()
            label.config(text = "Score:0", font=("consolas", 44), bg="black", fg="#0007D4", justify=CENTER, width=28)
            canvas = Canvas(window, bg=BACKGROUND_COLOR,
                    height=GAME_HEIGHT, width=GAME_WIDTH)
            canvas.pack()
            score = 0
            direction = "down"
            snake = Snake()
            food = Food()
            next_turn(snake, food)
            gameover = False

def hs_event():
    global highscores
    highscores = True
    frame.pack_forget()
    hsframe.pack()
    
    hs_image = ttk.Label(hsframe, image = bg_image)
    hs_image.place(x=0, y=0)

    hs_label2 = Label(hsframe, text= "HIGH SCORES", background="#75E001", foreground="white", font=("consolas", 40, "bold")).place(x = 315, y=30)
    hs_label3 = Label(hsframe, text= f"highscore_1 : {highscore_1} ", background="#75E001", foreground="white", font=("consolas", 20))
    hs_label3.place(x=250, y=180)
    hs_label4 = Label(hsframe, text= f"highscore_2 : {highscore_2} ", background="#75E001", foreground="white", font=("consolas", 20))
    hs_label4.place(x=250, y=260)
    hs_label5 = Label(hsframe, text= f"highscore_3 : {highscore_3} ", background="#75E001", foreground="white", font=("consolas", 20))
    hs_label5.place(x=250, y=340)
    hs_label6 = Label(hsframe, text= f"highscore_4 : {highscore_4} ", background="#75E001", foreground="white", font=("consolas", 20))
    hs_label6.place(x=250, y=420)
    hs_label7 = Label(hsframe, text= f"highscore_5 : {highscore_5} ", background="#75E001", foreground="white", font=("consolas", 20))
    hs_label7.place(x=250, y=500)

    back_button = Button(hsframe, image = button_image, background="#18A203", activebackground="#18A203",border=0, command=click_back)
    back_button.place(x=12,y=15)

def options_event():
    global options
    options = True
    frame.pack_forget()
    options_frame.pack()
    option_image = ttk.Label(options_frame, image =bg_image)
    option_image.place(x=0, y=0)
    back_button = Button(options_frame, image = button_image, background="#18A203", activebackground="#18A203",border=0, command=click_back)
    back_button.place(x=12,y=15)
    opts_label = Label(options_frame, text= "SETTINGS", background="#75E001", foreground="white", font=("consolas", 40, "bold")).place(x = 315, y=30)
    
    v1 = DoubleVar()

    music_scale = Scale(options_frame, variable = v1, orient= HORIZONTAL ,bg="#7EE400", fg="white",troughcolor= "#7EE400" ,from_ = 0.0, to = 1, sliderlength=15, width=25)
    music_scale.place(x=240, y=210)
    
    sfx_scale = Scale(options_frame, orient= HORIZONTAL ,bg="#7EE400", fg="white",troughcolor= "#7EE400" ,from_ = 0.0, to = 1, sliderlength=15, width=25)
    sfx_scale.place(x=240, y=340)
    
    difficulty_scale = Scale(options_frame,label="Easy|Normal|Hard", cursor="arrow" ,orient= HORIZONTAL ,bg="#7EE400", fg="white",troughcolor= "#7EE400" ,from_ = 0.0, to = 2, sliderlength=15, width=25)
    difficulty_scale.place(x=240, y=470)
    
    music_label = Label(options_frame, text= "Music", background="#75E001", foreground="white", font=("consolas", 20, "bold"))
    music_label.place(x=240 ,y=160)
    
    sfx_label = Label(options_frame, text= "SFX", background="#75E001", foreground="white", font=("consolas", 20, "bold"))
    sfx_label.place(x=240 ,y=290)
    
    difficulty_label = Label(options_frame, text= "Difficulty", background="#75E001", foreground="white", font=("consolas", 20, "bold"))
    difficulty_label.place(x=240 ,y=420)




window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text=f"Score:{score}", font=("consolas", 44), bg="black", fg="#0007D4", justify=CENTER, width=28)
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR,
                height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


button_image = PhotoImage(file="back_button.png")
apple = PhotoImage(file='apple.png')
snakehead = PhotoImage(file='snakehead.png')
start_image = PhotoImage(file="start_image.png")
bg_image = PhotoImage(file="hs_image.png")

frame = ttk.Frame(window, width=900, height=600)
hsframe = ttk.Frame(window, width=900, height=600)
options_frame = ttk.Frame(window, width=900, height=600)


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
#window.bind("<space>", lambda event: restart())

snake = Snake()
food = Food()

next_turn(snake, food)


s = ttk.Style()
s.theme_use('alt')
s.configure("TLabel", font=("consolas", 40, "bold"), background = "#84A600", foreground="black")
s.configure("TButton", font=("consolas", 20, "bold"), background = "black", foreground = "#83A600")
s.map('TButton', background=[('active','black')])


window.mainloop()