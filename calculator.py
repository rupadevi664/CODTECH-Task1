import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Display
display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief="ridge"
)
display.pack(fill="both", padx=10, pady=10, ipady=10)


# Function to display button value
def click(value):
    display.insert(tk.END, value)


# Function to clear display
def clear():
    display.delete(0, tk.END)


# Function to calculate result
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Button frame
frame = tk.Frame(root)
frame.pack()


# Buttons
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
]


for text, row, column in buttons:

    if text == "=":
        command = calculate
    else:
        command = lambda value=text: click(value)

    tk.Button(
        frame,
        text=text,
        font=("Arial", 18),
        width=5,
        height=2,
        command=command
    ).grid(row=row, column=column, padx=3, pady=3)


# Clear button
tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 16),
    width=22,
    height=2,
    command=clear
).pack(pady=10)


# Start application
root.mainloop()
