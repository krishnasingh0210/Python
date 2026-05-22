import tkinter as tk

# Function to run when button is clicked
def say_hello():
        label.config(text="Hello Krishna!", fg="white") #foreground color

# Create window
window = tk.Tk()

# Window title
window.title("My First GUI"),
background_color = "black"

# Window size
window.geometry("400x200")
window.config(bg=background_color)

# Create label
label = tk.Label(
    window,
    text="Welcome",
    font=("Arial", 20),
    bg=background_color,
    fg="white"
)

label.pack(pady=20)

# Create button
button = tk.Button(
    window,
    text="Click Me",
    font=("Arial", 16),
    background="red",
    command=say_hello
)

button.pack()

# Run GUI
window.mainloop()