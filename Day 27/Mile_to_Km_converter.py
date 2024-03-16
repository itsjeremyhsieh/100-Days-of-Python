from tkinter import *

window = Tk()
window.title("Mile to KM converter")
window.config(padx=30, pady=30)
mile = Entry(width=7)
mile.grid(column=1, row=0)
mile_text = Label(text="Miles")
mile_text.grid(column=2, row=0)
equal = Label(text="is equal to")
equal.grid(column=0, row=1)
answer = Label(text="0")
answer.grid(column=1, row=1)
Km = Label(text="Km")
Km.grid(column=2, row=1)

def calculate():
    user_input = mile.get()
    try:
        answer.config(text=str(round(int(user_input) * 1.60934, 2)))
    except:
        return
buttom = Button(text="Calculate", command= calculate)
buttom.grid(column=1, row=2)

window.mainloop()
