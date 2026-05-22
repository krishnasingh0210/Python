import tkinter as tk

# Function to run when button is clicked
def say_hello():
        label.config(text="Hello Class!", foreground="white") #(foreground color or fg) is used to change text color of label

# Create window
window = tk.Tk()

# Window title
window.title("My First GUI"),
background_color = "black"

# Window size
window.geometry("800x500")
window.config(bg=background_color)

# Create label
label = tk.Label(
    window,
    text="Welcome",
    font=("Arial", 20),
    bg=background_color,
    foreground="white"
)

label.place(x=350, y=200)#pack is used to add the label to the window and pady is used to add vertical padding around the label 
                    #and padx is used to add horizontal padding around the label   (place is also used in positioning)

# Create button
button = tk.Button(
    window,
    text="Click Me",
    font=("Arial", 16),
    background="lightgrey",
    foreground="black",
    command=say_hello
)

button.place(x=350, y=300)

# Run GUI
window.mainloop()