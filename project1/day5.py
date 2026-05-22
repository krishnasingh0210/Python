import tkinter as tk

# Function to run when button is clicked
def say_hello():
    label.config(text="Hello Krishna!")

# Create window
window = tk.Tk()

# Window title
window.title("My First GUI")

# Window size
window.geometry("400x200")

# Create label
label = tk.Label(
    window,
    text="Welcome",
    font=("Arial", 20)
)

label.pack(pady=20)

# Create button
button = tk.Button(
    window,
    text="Click Me",
    font=("Arial", 16),
    command=say_hello
)

button.pack()

# Run GUI
window.mainloop()