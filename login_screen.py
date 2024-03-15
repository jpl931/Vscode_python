import tkinter as tk
from tkinter import messagebox as tkmb

# Predefined username and password
USERNAME = "Geeks"
PASSWORD = "12345"

def login():
    # Get user input from entry widgets
    entered_username = user_entry.get()
    entered_password = user_pass.get()

    # Check if the input matches the predefined credentials
    if entered_username == USERNAME and entered_password == PASSWORD:
        tkmb.showinfo(title="Login Successful", message="You have logged in successfully!")
        # You can add further actions here, such as opening a new window or redirecting to another page.
    elif entered_username == USERNAME and entered_password != PASSWORD:
        tkmb.showwarning(title='Wrong Password', message='Please check your password.')
    elif entered_username != USERNAME and entered_password == PASSWORD:
        tkmb.showwarning(title='Wrong Username', message='Please check your username.')
    else:
        tkmb.showerror(title="Login Failed", message="Invalid username and password.")

# Create the main application window
app = tk.Tk()
app.title("Modern Login UI using Tkinter")
app.geometry("400x200")

# Create widgets
user_label = tk.Label(app, text="Username:")
user_entry = tk.Entry(app)
pass_label = tk.Label(app, text="Password:")
user_pass = tk.Entry(app, show="*")
login_button = tk.Button(app, text="Login", command=login)

# Place widgets on the screen
user_label.pack()
user_entry.pack()
pass_label.pack()
user_pass.pack()
login_button.pack()

# Start the application event loop
app.mainloop()
