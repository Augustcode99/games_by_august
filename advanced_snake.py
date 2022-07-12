from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Snake Game")
root.resizable(False, False)
root.geometry("900x565")
s = ttk.Style()
s.theme_use('alt')
s.configure("TLabel", font=("consolas", 40, "bold"), background = "#84A600", foreground="black")
# s.configure("Header.TLabel", font=("consolas", 20), background = "white", foreground="#83A600")
s.configure("TButton", font=("consolas", 20, "bold"), background = "black", foreground = "#83A600")
s.map('TButton', background=[('active','black')])

def start_event():
    frame.pack_forget()

def hs_event():
    frame.pack_forget()
    hsframe = ttk.Frame(root, width=900, height=600)
    hsframe.pack()
    
    hs_image = ttk.Label(hsframe, image = bg_image)
    hs_image.place(x=0, y=0)

    hs_label2 = Label(hsframe, text= "HIGH SCORES", background="#75E001", foreground="white", font=("consolas", 40)).place(x = 315, y=50)
    hs_label3 = Label(hsframe, text= "1 {highscore_1} : {player_name} ", background="#75E001", foreground="white", font=("consolas", 20))
    hs_label3.place(x=250, y=180)
    hs_label4 = Label(hsframe, text= "2 {highscore_2} : {player_name} ", background="#75E001", foreground="white", font=("consolas", 20))
    hs_label4.place(x=250, y=260)
    hs_label5 = Label(hsframe, text= "3 {highscore_3} : {player_name} ", background="#75E001", foreground="white", font=("consolas", 20))
    hs_label5.place(x=250, y=340)
    hs_label6 = Label(hsframe, text= "4 {highscore_4} : {player_name} ", background="#75E001", foreground="white", font=("consolas", 20))
    hs_label6.place(x=250, y=420)
    hs_label7 = Label(hsframe, text= "5 {highscore_5} : {player_name} ", background="#75E001", foreground="white", font=("consolas", 20))
    hs_label7.place(x=250, y=500)

    back_button = Button(hsframe, image = button_image, background="#75E001", activebackground="#75E001",border=0, command=click_back)
    back_button.place(x=10,y=10)

def options_event():
    frame.pack_forget()
    options_frame = ttk.Frame(root, width=900, height=600)
    options_frame.pack()
    option_image = ttk.Label(options_frame, image =bg_image)
    option_image.place(x=0, y=0)
    back_button = Button(options_frame, image = button_image, background="#75E001", activebackground="#75E001",border=0, command=click_back)
    back_button.place(x=10,y=10)

def click_back():
    pass

frame = ttk.Frame(root, width=900, height=600)
frame.pack()

start_image = PhotoImage(file="snake_start_screen.png")
bg_image = PhotoImage(file="hs_image.png")
button_image = PhotoImage(file="back_button.png")

image_label = ttk.Label(frame, image = start_image)
image_label.place(x=0, y=0)

game_title = ttk.Label(frame, text = "Snake Classic")
game_title.place(x=250, y=25)

start_button = ttk.Button(frame, text = "START", command = start_event)
start_button.place(x=350, y=300)
high_button = ttk.Button(frame, text = "HIGHSCORES",command = hs_event)
high_button.place(x=350, y=370)
option_button = ttk.Button(frame, text = "OPTIONS",command = options_event)
option_button.place(x=350, y=440)


root.mainloop()
