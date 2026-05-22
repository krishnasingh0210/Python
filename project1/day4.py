import tkinter as tk


def say_hello():
    label.config(text="Hello Krishna!")


def change_color():
    window.config(bg="lightblue")


def big_text():
    label.config(font=("Arial", 30))


# One function calling multiple functions
def do_all():
    say_hello()
    change_color()
    big_text()


window = tk.Tk()

window.geometry("500x300")

label = tk.Label(
    window,
    text="Welcome",
    font=("Arial", 20)
)

label.pack(pady=20)


button = tk.Button(
    window,
    text="Click Me",
    font=("Arial", 16),
    command=do_all
)

button.pack(pady=20)


window.mainloop()