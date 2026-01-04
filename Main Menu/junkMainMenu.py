import tkinter as tk #GUI library
from tkinter import messagebox

USER_FILE = "users.txt"

def register_user():
    username = reg_username.get()
    password = reg_password.get()

    if not username or not password:
        messagebox.showerror("Error", "All fields required")
        return

    with open(USER_FILE, "r") as file:
        for line in file:
            if line.split(",")[0] == username:
                messagebox.showerror("Error", "Username already exists")
                return

    with open(USER_FILE, "a") as file:
        file.write(f"{username},{password}\n")

    messagebox.showinfo("Success", "Registration successful")
    register_window.destroy()


def login_user():
    username = login_username.get()
    password = login_password.get()

    with open(USER_FILE, "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(",")
            if stored_user == username and stored_pass == password:
                open_main_menu(username)
                return

    messagebox.showerror("Error", "Invalid login details")


def open_register():
    global register_window, reg_username, reg_password

    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("300x200")

    tk.Label(register_window, text="Username").pack(pady=5)
    reg_username = tk.Entry(register_window)
    reg_username.pack()

    tk.Label(register_window, text="Password").pack(pady=5)
    reg_password = tk.Entry(register_window, show="*")
    reg_password.pack()

    tk.Button(register_window, text="Register", command=register_user).pack(pady=10)


def open_main_menu(username):
    menu = tk.Toplevel(root)
    menu.title("Main Menu")
    menu.geometry("300x200")

    tk.Label(menu, text=f"Welcome, {username}!", font=("Arial", 14)).pack(pady=20)

    tk.Button(menu, text="View Profile",
              command=lambda: messagebox.showinfo("Profile", f"Username: {username}")).pack(pady=5)

    tk.Button(menu, text="Logout", command=menu.destroy).pack(pady=5)


# Main Window
root = tk.Tk()
root.title("Login System")
root.geometry("300x250")

tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Username").pack()
login_username = tk.Entry(root)
login_username.pack()

tk.Label(root, text="Password").pack()
login_password = tk.Entry(root, show="*")
login_password.pack()

tk.Button(root, text="Login", command=login_user).pack(pady=10)
tk.Button(root, text="Register", command=open_register).pack()

root.mainloop()
