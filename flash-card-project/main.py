from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
timer = 0


def question_words():
    data = pandas.read_csv('flash-card-project/data/french_words.csv')
    question_count = randint(2, 102)
    french_word = data.French[question_count]
    canvas.itemconfig(language_text, text='French')
    canvas.itemconfig(word_text, text=f'{french_word}')
    canvas.itemconfig(image_on_canvas, image=card_front)
    window.after(1000, answer_words(question_count))


def answer_words(question_count):
    data = pandas.read_csv('flash-card-project/data/french_words.csv')
    english_word = data.English[question_count]
    canvas.itemconfig(language_text, text='English')
    canvas.itemconfig(word_text, text=f'{english_word}')
    canvas.itemconfig(image_on_canvas, image=card_back)


window = Tk()
window.title('Study')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='flash-card-project/images/card_front.png')
card_back = PhotoImage(file='flash-card-project/images/card_back.png')
image_on_canvas = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(
    400, 150, fill='black', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(
    400, 263, fill='black', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons

wrong_image = PhotoImage(file='flash-card-project/images/wrong.png')
wrong_button = Button(highlightthickness=0,
                      image=wrong_image, command=question_words)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file='flash-card-project/images/right.png')
right_button = Button(highlightthickness=0,
                      image=right_image, command=question_words)
right_button.grid(column=1, row=1)

question_words()
window.mainloop()
