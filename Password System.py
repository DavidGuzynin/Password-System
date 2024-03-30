import tkinter as tk
win=tk.Tk()
entry=tk.Entry(win)
win.geometry("300x400")
win.title("password")
entry.pack()
password = [('5398')]
def check_password():
    if (entry.get()) in password:
        label_1 = tk. Label (win, text='welcome')
        label_1.pack()
        win2=tk.Tk()
        win2.geometry("400x400")
        win2.title("Welcome")
        label_1 = tk. Label (win2, text='welcome here is an example of a login system in python')
        label_1.pack()
    else:
        label_1 = tk. Label (win, text='wrong password')
        label_1.pack()
    return password
tk.Button(win, text="login", command=check_password).pack()
win.mainloop()