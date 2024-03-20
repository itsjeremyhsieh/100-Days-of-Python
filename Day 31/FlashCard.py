BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
import time
# data=pandas.read_csv("./data/french_words.csv")
# data_dict = data.to_dict()
# print(len(data_dict["English"]))
data = pandas.read_csv("./data/french_words.csv")
data_dict = data.to_dict()
# print(data)
random_int=0
def random_card():

    global random_int, flip_timer
    window.after_cancel(flip_timer)
    canva.itemconfig(canva_image, image=front)
    canva.delete("voc")
    canva.delete("title")
    canva.create_text(400, 150, text="French", font=("Ariel", 30, "italic"), fill="black", tag="title")
    random_int = random.randint(0, len(data_dict["French"]) - 1)
    canva.create_text(400, 263, text=data_dict["French"][random_int], font=("Ariel", 60, "bold"), fill="black", tag="voc")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():

    global random_int
    canva.itemconfig(canva_image, image=back)
    canva.delete("voc")
    canva.delete("title")
    canva.create_text(400, 150, text="English", font=("Ariel", 30, "italic"), fill="white",tag="title")
    canva.create_text(400, 263, text=data_dict["English"][random_int], font=("Ariel", 60, "bold"), fill="white",tag="voc")
cnt = 0
def check():
    global random_int, cnt, data
    if cnt == 0:
        cnt += 1
        random_card()
    else:
        data = data.drop(random_int)
        data.to_csv("./data/french_words.csv", index=False)
        random_card()

def uncheck():
    random_card()

window = Tk()
window.minsize(width=900, height=670)
window.config(padx=50, pady=50)
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=check)
canva = Canvas(width=800, height=526)
canva.config(highlightthickness=0, bg=BACKGROUND_COLOR)
front = PhotoImage(file="./images/card_front.png")
canva_image = canva.create_image(400, 263, image=front)
canva.create_text(400, 150, text="French", font=("Ariel", 30, "italic"), tag = "title")
back = PhotoImage(file="./images/card_back.png")
canva.create_text(400, 263, text="Vocabulary", font=("Ariel", 60, "bold"), tag = "voc")
canva.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong, highlightthickness=0, command=uncheck)
wrong_btn.grid(row=1, column=0)

right = PhotoImage(file="./images/right.png")
check_btn = Button(image=right, highlightthickness=0, command=check)
check_btn.grid(row=1, column=1)

window.mainloop()
