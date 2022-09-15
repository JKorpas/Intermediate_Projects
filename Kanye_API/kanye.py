from cgitb import text
import requests
from tkinter import *

URL = "https://api.kanye.rest/"
QUOTE_FONT = ('Arial', 24, 'italic')\

# Retriving Data from API


def take_quote():
    response = requests.get(URL)
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


# UI
window = Tk()
window.config(padx=50, pady=50)
# Canvas
canvas = Canvas(width=300, height=414)

quote_background_img = PhotoImage(file="Kanye_Images\\background.png")
quote_background = canvas.create_image(150, 207, image=quote_background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=QUOTE_FONT)
canvas.grid(row=0, column=0)

kanye_head_img = PhotoImage(file="Kanye_Images\kanye.png")
kanye_head = Button(image=kanye_head_img, command=take_quote)
kanye_head.grid()

take_quote()
window.mainloop()
