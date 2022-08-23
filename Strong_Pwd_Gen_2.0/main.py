import random
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("SPG2.0")
root.geometry("580x300")

digits = list("0123456789")
lowercase_letters = list("abcdefghijklmnoprstuvwxyz")
uppercase_letters = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")
symbols = list("!@#$%^&*()_+|:<>?")
characters = digits + uppercase_letters + lowercase_letters + symbols


def generate_password():
    # Clear Entry Box
    pwd_entry.delete(0, END)
    # PWD Lenght in integers
    pwd_length = int(my_entry.get())
    # create to hold password
    strong_password = "".join(random.choices(characters, k=pwd_length))
    pwd_entry.insert(0, strong_password)


def clipper():
    # Clear clipboard
    root.clipboard_clear()
    # Copy CB
    root.clipboard_append(pwd_entry.get())


def save_password():
    #check if all cells are full then open file and saves it in txt with succes info messagebox 
    if website_entry.get() and username_entry.get() and pwd_entry.get():
        with open("strong_password.txt", "a") as file:
            file.write(
                f"{website_entry.get()} | {username_entry.get()} | {pwd_entry.get()} \n")
        messagebox.showinfo("Succes", "You have saved data")
    else:
        messagebox.showinfo("Oooops", "Please fill cells")

# Label Frame with number of char to input
main_label_frame = LabelFrame(root, text="SPG2.0")
# Password configure
label_frame = Label(text="How many characters do you want in password?")
label_frame.grid(row=0, column=0, pady=20)
my_entry = Entry(font=("Arial", 18))
my_entry.grid(row=0, column=1, pady=10, padx=10)
# Website details
website_label = Label(text="Website")
website_label.grid(row=1, column=0, pady=20)
website_entry = Entry(font=("Arial", 18))
website_entry.grid(row=1, column=1, pady=10, padx=10)
# Username details
username_label = Label(text="Username")
username_label.grid(row=2, column=0, pady=20)
username_entry = Entry(font=("Arial", 18))
username_entry.grid(row=2, column=1, pady=10, padx=10)
# Box of returned password
generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(row=3, column=0, padx=10)
pwd_entry = Entry(font=("Arial", 18))
pwd_entry.grid(row=3, column=1, pady=10, padx=10)
# Create buttons for clip and save
clip_button = Button(text="Copy to Clipboard", command=clipper)
clip_button.grid(row=4, column=0, pady=10)
save_pwd = Button(text="Save to file", command=save_password)
save_pwd.grid(row=4, column=1, pady=10)


root.mainloop()
