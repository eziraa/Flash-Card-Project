import random
from tkinter import *

GREEN = "#9fd6b8"

with open("Data/french_words.csv") as data_file:
    data = data_file.readlines()
    word_list = []
    for item in data:
        single_word = item.split(",")
        word_list.append([single_word[0], single_word[1].strip()])

random_word = []


def next_card():
    global random_word
    global flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(word_list)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word[0], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)




def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(word_text, text=random_word[1], fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")


# Creating the main window
window = Tk()
window.title("Flashy")
window.config(pady=20, padx=20, bg=GREEN)
canvas = Canvas(width=867, height=568)
card_front_img = PhotoImage(file="Images/card-front.png")
card_back_img = PhotoImage(file="Images/card-back.png")
flip_timer = window.after(2000, func=next_card)
canvas_img = canvas.create_image(433.5, 279, image=card_front_img)
language_text = canvas.create_text(433.5, 180, text="Learn Immersive Language", font=("Arial", 40, "italic"))
word_text = canvas.create_text(433.5, 279, text="Try it!!!!", font=("Arial", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=GREEN, highlightthickness=0)

# Buttons
wrong_img = PhotoImage(file="Images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)
right_img = PhotoImage(file="Images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=next_card)
right_btn.grid(row=1, column=1)
window.mainloop()
