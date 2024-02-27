from tkinter import *
from tkinter import messagebox
import os
import random
PURPLE = "#5E1675"
YELLOW = "#FFD23F"
RED="#B31312"
WHITE="#EEE2DE"
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path= os.path.join(desktop_path, "DAY29_GUI_Password_Manager", "database.txt")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters) ]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols) ]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers) ]

    password_list = password_letters + password_symbols + password_numbers

    password= "".join(password_list)
    random.shuffle(password_list)
    if password_entry_widget == "":
        password_entry_widget.insert(0,password)
    else:
        password_entry_widget.delete(0, END)
        password_entry_widget.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def adder():
    global website_entry_widget,username_entry_widget,password_entry_widget
    website_entry = website_entry_widget.get()
    username_entry = username_entry_widget.get()
    password_entry = password_entry_widget.get()

    if website_entry != "" and password_entry != "":
        is_ok = messagebox.askokcancel(title=website_entry,message=f'These are the details entered: \n\nE-mail: {username_entry}\nPassword: {password_entry}\nis it ok to save?')
        if is_ok == True:
            if os.path.exists(file_path):
                with open(r'C:\Users\TEOMAN\Desktop\DAY29_GUI_Password_Manager\database.txt','a') as file:
                    file.write(f'{website_entry}|{username_entry}|{password_entry}\n')
                    website_entry_widget.delete(0,END)
                    password_entry_widget.delete(0,END)
            else:
                with open(r'C:\Users\TEOMAN\Desktop\DAY29_GUI_Password_Manager\database.txt','w') as file:
                    file.write(f'{website_entry_widget} | {username_entry} | {password_entry}\n')
    else:
        messagebox.showinfo(title="Blanks are present!",message="Please do not leave any blanks for data to be saved.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg=PURPLE)


canvas = Canvas(width=200,height=200,highlightthickness=0,bg=PURPLE)
photo_img=PhotoImage(file="logo.png")

canvas.create_image(100,100,image=photo_img)
canvas.grid(row=0,column=1)

#Website Label and Entry
website = Label(text="Website: ", font=("Arial",14,"bold"),bg=PURPLE,fg=YELLOW)
website.grid(row=1,column=0)
website_entry_widget = Entry(width=35)
website_entry_widget.focus()
website_entry_widget.grid(row=1, column=1, columnspan=2)


#Username Label and Entry
username= Label(text="Email/Username: ",font=("Arial",14,"bold"),bg=PURPLE,fg=YELLOW)
username.grid(row=2,column=0)
username_entry_widget = Entry(width=35)
username_entry_widget.insert(0,"teomanaknc@outlook.com")
username_entry_widget.grid(row=2,column=1,columnspan=2)


#Password
password_label = Label(text="Password: ", font=("Arial",14,"bold"),bg=PURPLE,fg=YELLOW)
password_label.grid(row=3,column=0)
password_entry_widget = Entry(width=29)
password_entry_widget.grid(row=3,column=1,sticky="e")



#Generate button
generate_b = Button(text="Generate Password ", width=15, font=('Arial',8,'bold'),bg=RED,fg=YELLOW,command=generate_password)
generate_b.grid(row=3,column=2,padx=20)

#Add Button
add_b = Button(text="Add",width=36,font=('Arial',8,'bold'),bg=RED,fg=YELLOW,command=adder)
add_b.grid(row=4,column=1,columnspan=2)












window.mainloop()