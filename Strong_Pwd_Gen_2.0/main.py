import random
from tkinter import *
from tkinter import messagebox
import json

root = Tk()
root.title("SPG2.0")
root.geometry("680x230")

digits = list("0123456789")
lowercase_letters = list("abcdefghijklmnoprstuvwxyz")
uppercase_letters = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")
symbols = list("!@#$%^&*()_+|:<>?")
characters = digits + uppercase_letters + lowercase_letters + symbols


def generate_password():
    # Clear Entry Box
    pwd_entry.delete(0, END)
    # PWD Lenght in integers
    try:
        pwd_length = int(my_entry.get())
    except ValueError:
        messagebox.showinfo("Oooops", "Enter lenght of password")
    finally:
        # create to hold password
        strong_password = "".join(random.choices(characters, k=pwd_length))
        pwd_entry.insert(0, strong_password)


def clipper():
    # Clear clipboard
    root.clipboard_clear()
    # Copy CB
    root.clipboard_append(pwd_entry.get())


def save_password():

    website = website_entry.get()
    username = username_entry.get()
    password = pwd_entry.get()

    # Dict for JSON
    new_data = {website:
                {"username": username,
                 "password": password}}
    # check if all cells are full then open file and saves it in txt with succes info messagebox
    if website and username and password:
        try:
            with open("password_generator.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password_generator.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                messagebox.showinfo("Succes", f"You'r saved data \n Website: {website} \n Username: {username} \n Password: {password}")
        else:
            # Updating old data with new datadate(new_data)
            data.update(new_data)
            with open("password_generator.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
                messagebox.showinfo("Succes", f"You'r saved data \n Website: {website} \n Username: {username} \n Password: {password}")
        finally:
            website_entry.delete(0, END)
            pwd_entry.delete(0, END)

    else:
        messagebox.showinfo("Oooops", "Please fill cells")


def search_for_data():
    website = website_entry.get()
    if len(website) < 1:
        messagebox.showinfo("Oooops", "Enter correct lenght of website")
    else:
        with open("password_generator.json", "r") as json_file:
            file = json.load(json_file)
            if website in file:
                # Cliboard clear and copy
                root.clipboard_clear()
                root.clipboard_append(file[website]['password'])
                messagebox.showinfo(
                    "Succes", f"Your date for {website} website exists!  \nUsername: {file[website]['username']} \nPassword: {file[website]['password']} \nPassword is in clipboard")
            else:
                messagebox.showinfo(
                    "Failed", f"There is no saved date for {website}")


# Label Frame with number of char to input
main_label_frame = LabelFrame(root, text="SPG2.0")
# Password configure
label_frame = Label(text="How many characters do you want in password?")
label_frame.grid(row=0, column=0, pady=5)
my_entry = Entry(font=("Arial", 18), width=5)
my_entry.grid(row=0, column=1, pady=5, padx=5)
# Website details
website_label = Label(text="Website")
website_label.grid(row=1, column=0, pady=5)
website_entry = Entry(font=("Arial", 18))
website_entry.grid(row=1, column=2, pady=5, padx=5)
# Username details
username_label = Label(text="Username")
username_label.grid(row=2, column=0, pady=5)
username_entry = Entry(font=("Arial", 18))
username_entry.grid(row=2, column=2, pady=5, padx=10)
# Box of returned password
password_label = Label(text="Password")
password_label.grid(row=3, column=0, pady=5)
generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(row=0, column=2, padx=10)
pwd_entry = Entry(font=("Arial", 18))
pwd_entry.grid(row=3, column=2, pady=10, padx=10)
# Create buttons for clip and save
clip_button = Button(text="Copy Password to Clipboard", command=clipper)
clip_button.grid(row=4, column=2, pady=10)
save_pwd = Button(text="Save Data to file", command=save_password)
save_pwd.grid(row=4, column=1, pady=5)
# Search button
search_button = Button(text="Search in saved data", command=search_for_data)
search_button.grid(row=1, column=1, pady=5)


root.mainloop()
