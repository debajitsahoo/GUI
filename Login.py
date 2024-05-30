import tkinter as tk
def validate_login():
    pass
parent = tk.Tk()
parent.title("Login Form")
username_label = tk.Label(parent, text="Username:")
username_label.pack()
username_entry = tk.Entry(parent)
username_entry.pack()
password_label = tk.Label(parent, text="Password:")
password_label.pack()
password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack()
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()
parent.mainloop()
