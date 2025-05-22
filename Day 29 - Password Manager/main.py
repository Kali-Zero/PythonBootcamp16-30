from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    textbox_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    textbox_password.insert(0, f"{password}")

    #Automatically copy new password to clipboard!
    #https://pypi.org/project/pyperclip/
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    missing_text = ""
    good_to_save = True

    if len(textbox_website.get()) == 0:
        missing_text += "You forgot to add a website!\n"
        good_to_save = False
    if len(textbox_email_un.get()) == 0:
        missing_text += "You forgot to add an email!\n"
        good_to_save = False
    if len(textbox_password.get()) == 0:
        missing_text += "You forgot to add a password!"
        good_to_save = False

    if good_to_save:
        #Pop-up Message Box
        is_ok = messagebox.askokcancel(
            title=f"Website: {textbox_website.get()}",
            message="These are the details entered:\n\n"
                    f"Email:\n {textbox_email_un.get()}\n\n"
                    f"Password:\n {textbox_password.get()}\n\n"
                    "Is it ok to save?")

        if is_ok:
            with open("pw_data.txt", "a") as password_file:
                password_file.write(f"{textbox_website.get()} | {textbox_email_un.get()} | {textbox_password.get()}\n")
                password_file.close()
                textbox_website.delete(0, END)
                textbox_password.delete(0, END)
                messagebox.showinfo("Password Generated", "Your password has been saved.")
    else:
        messagebox.showinfo("Error", missing_text)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(" " * 50 + "Password Manager") #Hacky way to center it. :-P
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(window, width=200, height=200, background="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels--------------------------------------------------------------------------
label_website = Label(text="Website:", font=("New Times Roman", 10, "bold"), bg="white")
label_website.grid(column=0, row=1)

label_email_un = Label(text="Email/Username:", font=("New Times Roman", 10, "bold"), bg="white")
label_email_un.grid(column=0, row=2)

label_password = Label(text="Password:", font=("New Times Roman", 10, "bold"), bg="white")
label_password.grid(column=0, row=3)

#Text Boxes-----------------------------------------------------------------------
textbox_website = Entry(width=35)
textbox_website.grid(column=1, row=1, columnspan=2, sticky="ew")
textbox_website.focus()
textbox_website.get()

textbox_email_un = Entry(width=35)
textbox_email_un.grid(column=1, row=2, columnspan=2, sticky="ew")
textbox_email_un.insert(0, "first.last@email.com")
textbox_email_un.get()

textbox_password = Entry(width=30)
textbox_password.grid(column=1, row=3, sticky="ew")
textbox_password.get()

#Buttons--------------------------------------------------------------------------
button_generate_password = Button(window, text="Generate Password", command=generate_password)
button_generate_password.grid(column=2, row=3)

button_save_password = Button(window, text="Add", command=save_password, width=35)
button_save_password.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()
