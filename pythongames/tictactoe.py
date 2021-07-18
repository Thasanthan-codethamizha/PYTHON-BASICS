from tkinter import *
import random


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player+"turn")


window = Tk()
window.title("OUR TIC TAC TOE")
players = ["x", "o"]
player = random.choice(players)
buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]

]


label = Label(text=player+"turn", font=('consolas', 40))
label.pack(side="top")


reset_button = Button(text="Restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

window.mainloop()
