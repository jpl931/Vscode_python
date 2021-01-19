from tkinter import Tk, Label
from tkinter import messagebox

root =Tk()
root.title("My Message Box Examples")
root.geometry("300x300")

w = Label(root, text ='TKinter Message Boxes', font = "50")
w.pack()

messagebox.showinfo("Info", "Information")

messagebox.showwarning("Warning", "Warning")

messagebox.showerror("Error", "Error")

messagebox.askquestion("Question", "Are you sure?")

messagebox.askokcancel("ask_ok_cancel", "Want to continue?")

messagebox.askyesno("ask_yes_no", "Find the value?")

messagebox.askretrycancel("askretrycancel", "Try again?")

root.mainloop()