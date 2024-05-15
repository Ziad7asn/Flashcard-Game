from tkinter import *
import pandas as pd 
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient="records")
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")





def next_word():
    global current_card ,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill='black')
    canvas.itemconfig(card_word, text=current_card["French"],fill='black')
    canvas.itemconfig(canvas_image, image=old_image)
    flip_timer=window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text="English",fill='white')    
    canvas.itemconfig(card_word,text=current_card['English'],fill='white') 
    canvas.itemconfig(canvas_image, image=new_image)


def is_known():

    to_learn.remove(current_card)
    data=pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    
    next_word()


window = Tk()
window.title("flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

flip_timer= window.after(3000, func=flip_card)

canvas=Canvas(width=800,height=526)

old_image = PhotoImage(file="images\card_front.png")
new_image = PhotoImage(file="images\card_back.png")

canvas_image=canvas.create_image(400, 263,image=old_image)
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

card_title=canvas.create_text(400,150,text="", font=("Ariel",40,'italic'))
card_word=canvas.create_text(400,263,text="",font=("Ariel", 60, "bold"))


wrong_image = PhotoImage(file="images\wrong.png")
wrong_btn = Button(image=wrong_image,highlightthickness=0,command=next_word)
wrong_btn.grid(row=1,column=0)


right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image,highlightthickness=0,command=is_known)
right_btn.grid(row=1,column=1)

next_word()

window.mainloop()
