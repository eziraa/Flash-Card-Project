from tkinter import *

GREEN = "#9fd6b8"
# Creating the main window
window = Tk()
window.title("Flashy")
window.config(pady=20, padx=20, bg=GREEN)
canvas = Canvas(width=867, height=568)
card_front_img = PhotoImage(file="Images/card-front.png")

canvas.create_image(433.5, 279, image=card_front_img)
canvas.create_text(433.5, 180, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(433.5, 279, text="Data", font=("Arial", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=GREEN,highlightthickness=0)

# Buttons
wrong_img = PhotoImage(file="Images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0)
wrong_btn.grid(row=1, column=0)
right_img = PhotoImage(file="Images/right.png")
right_btn = Button(image=right_img, highlightthickness=0)
right_btn.grid(row=1, column=1)
window.mainloop()
