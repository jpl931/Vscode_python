from tkinter import *
from tkinter import messagebox

root =Tk()
root.title("My Message Box Examples")
root.geometry("300x300")

w = Label(root, text ='Geeks for Geeks', font = "50")
w.pack()

messagebox.showinfo("show_info", "Information")

messagebox.showwarning("show_warning", "Warning")

messagebox.showerror("show_error", "Error")

messagebox.askquestion("ask_question", "Are you sure?")

messagebox.askokcancel("ask_ok_cancel", "Want to continue?")

messagebox.askyesno("ask_yes_no", "Find the value?")

messagebox.askretrycancel("askretrycancel", "Try again?")

root.mainloop()