import csv
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")  # Sets the parameters of the window


def logInValidate(usernameTk, passwordTk):  # Checks if username and password are in table together

    username = usernameTk.get()
    password = passwordTk.get()
    username = str(username)
    with open("data/users.csv", "r") as file:
        users = csv.reader(file)
        i = 0
        line = 0
        for row in users:
            if row[i] == username and row[i + 1] == password:  # ==> need to move down a line
                login = True
                print(row)
                break
            else:
                login = False
                i = i + 1
        if login is True:
            print("Found")
        else:
            print("Not found")


# =======================================Log In Labels====================================================
tk.Label(root, text="Username").grid(row=0, column=0)  # Labels the fields that need to be entered
tk.Label(root, text="Password").grid(row=1, column=0)


# =======================================Entry Widgets====================================================
usernameEnter = tk.Entry(root, width=50)
passwordEnter = tk.Entry(root, width=50)

# =======================================Config of Entry Widgets==========================================
usernameEnter.grid(row=0, column=1)  # Aligns entry box with tkinter grid
passwordEnter.grid(row=1, column=1)
passwordEnter.config(show="*")


login = tk.Button(root, text="Log In", command=lambda: logInValidate(usernameEnter, passwordEnter)).grid(
    row=2, pady=10, column=1
)  # :Log In Button
# signup = tk.Button(root, text ="Sign Up" , command = lambda:passwordValidate(passwordEnter)).grid(row = 2, column = 0) # Sign Up Button

root.mainloop()  # runs the GUI


# you smell of hamsters poo poo pooo pooo poo
