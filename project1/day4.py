import tkinter as tk

messages = [
    "Hello Krishna!",
    "Welcome to Python",
    "You are learning GUI",
    "Great job!"
]

index = 0

def next_message():
    global index

    label.config(text=messages[index])

    index += 1

    if index >= len(messages):
        index = 0


window = tk.Tk()

window.geometry("400x250")

label = tk.Label(
    window,
    text="Press Button",
    font=("Arial", 18)
)

label.pack(pady=20)

button = tk.Button(
    window,
    text="Next Message",
    font=("Arial", 14),
    command=next_message
)

button.pack()

window.mainloop()