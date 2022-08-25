
import pandas
import random
from tkinter import *
import csv

TITLE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
BACKGROUNDCOLOR = "#B1DDC6"
FLASHY_CARD = None



'''# read words from csv and but it into dict / NOOB WAY
es_to_en_dict = pandas.read_csv(
    "Flash_Card\Data\Spanish_Words.csv", index_col=0)
spanish_word = es_to_en_dict.iloc[:, 0]
english_word = es_to_en_dict.iloc[:, 1]
es_to_en_dict = {key: value for key, value in zip(spanish_word, english_word)}
'''
try:
    tutorial_dict = pandas.read_csv(
    "Data\Words_to_learn.csv", index_col=0).to_dict(orient="records")
except FileNotFoundError:
    tutorial_dict = pandas.read_csv(
    "Data\Spanish_Words.csv", index_col=0).to_dict(orient="records")



def correct_answer():
    tutorial_dict.remove(FLASHY_CARD)
    print(len(tutorial_dict))
    data = pandas.DataFrame(tutorial_dict)
    data.to_csv("Data\Words_to_learn.csv", index=False)
    next_card()

def incorrect_answer():
    next_card()

def next_card():
    global FLASHY_CARD
    FLASHY_CARD = random.choice(tutorial_dict)
    spanish_word = FLASHY_CARD["Spanish"]
    canvas.itemconfig(title_text, text="Spanish")
    canvas.itemconfig(card_image, image=front_card__img)
    canvas.itemconfig(word_text, text=spanish_word)
    root.after(3000, reverse_card)

def reverse_card():
    global FLASHY_CARD
    english_word = FLASHY_CARD["in English"]
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(card_image, image=back_card_img)
    canvas.itemconfig(word_text, text=english_word)


# Window Config
root = Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUNDCOLOR)
# Flash Card canvas
canvas = Canvas(width=800, height=526)
# Back Flash Card
back_card_img = PhotoImage(file="images\card_back.png")
# Front Flash Card
front_card__img = PhotoImage(file="images\card_front.png")
#Flashcard config
card_image = canvas.create_image(400, 263, image=front_card__img)
canvas.config(bg=BACKGROUNDCOLOR, highlightthickness=0)
title_text = canvas.create_text(
    400, 150, text="Spanish", fill="black", font=TITLE_FONT)
word_text = canvas.create_text(
    400, 263, text="Word", fill="black", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)
# Buttons
# Wrong
wrong_answer_photo = PhotoImage(file="images\wrong.png")
wrong_button = Button(image=wrong_answer_photo,
                      highlightthickness=0, command=incorrect_answer)
wrong_button.grid(row=1, column=0)
# Right
right_answer_photo = PhotoImage(file="images\\right.png")
right_button = Button(image=right_answer_photo,
                      highlightthickness=0, command=correct_answer)
right_button.grid(row=1, column=1)

next_card()

root.mainloop()
