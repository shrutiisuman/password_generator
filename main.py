from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','@','#','$','%','^','&','*','(',')']

    num_let= random.randint(8,10)
    num_sym= random.randint(2,4)
    num_nu= random.randint(2,4)

    pwd_letters = [random.choice(letters) for _ in range(num_let)]
    pwd_symbol = [random.choice(symbols) for _ in range(num_sym)]
    pwd_numbers = [random.choice(numbers) for _ in range(num_nu)]

    password = pwd_letters + pwd_numbers + pwd_symbol
    random.shuffle(password)

    # final_pass=""
    # for char in password:
    #     final_pass +=char

    final_pass = "".join(password)

    pwd_input.insert(0, final_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website= website_input.get()
    email = username_input.get()
    pwd = pwd_input.get()
    new_data = {
        website: {
            "email": email,
            "password": pwd,
        }
    }

    if len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please enter all the fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)


        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        except json.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating old data with new data

            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            pwd_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_pwd():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found")

    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="No Data File found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1, row=0)

#labels
website_label= Label(text="Website:")
website_label.grid(column=0, row=1)
username_label= Label(text="Email/Username:")
username_label.grid(column=0, row=2)
pwd_label= Label(text="Password:")
pwd_label.grid(column=0, row=3)

#entries
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "shrutisuman0651@gmail.com")
pwd_input = Entry(width=21)
pwd_input.grid(column=1, row=3)

#buttons
search_button = Button(text="Search", width=13, command=find_pwd)
search_button.grid(row=1, column=2)
pwd_button = Button(text="Generate Password", command=generate)
pwd_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()