import tkinter as tk

# Function to run when button is clicked
def say_hello():
        label.config(text="Hello Krishna!", foreground="white") #(foreground color or fg) is used to change text color of label

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
    foreground="white"
)

label.pack(pady=20)

# Create button
button = tk.Button(
    window,
    text="Click Me",
    font=("Arial", 16),
    background="lightgrey",
    foreground="black",
    command=say_hello
)

button.pack()

# Run GUI
window.mainloop()