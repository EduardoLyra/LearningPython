from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers)for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showerror(
            title='Oops', message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail/Username: {user}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open('password-manager/data.txt', 'a') as file:
                file.write(f'{website} | {user} | {password}\n')
                website_input.delete(0, END)
                user_input.delete(0, END)
                password_input.delete(0, END)


    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
locker_img = PhotoImage(file='password-manager/logo.png')
canvas.create_image(100, 100, image=locker_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website: ')
website_label.grid(column=0, row=1)

user_label = Label(text='Email/Username: ')
user_label.grid(column=0, row=2)

password_label = Label(text='Password: ')
password_label.grid(column=0, row=3)

# Inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()

user_input = Entry(width=35)
user_input.grid(column=1, row=2, columnspan=2, sticky="EW")
user_input.focus()

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")
password_input.focus()

# Buttons
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
