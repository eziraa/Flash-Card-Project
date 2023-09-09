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
canvas.grid(row=0, column=0)
canvas.config(bg=GREEN,highlightthickness=0)

window.mainloop()
