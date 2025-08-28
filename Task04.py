import tkinter as tk

def log_key(event):
    key = event.char
    if key:  # ignore non-character keys
        with open("keystrokes.txt", "a") as f:
            f.write(key)
    print(f"Key pressed: {key}")

# Create a simple GUI
root = tk.Tk()
root.title("Safe Key Logger Demo")

label = tk.Label(root, text="Type something here:")
label.pack()

text_box = tk.Text(root, width=50, height=10)
text_box.pack()

# Bind key events only inside this text box
text_box.bind("<Key>", log_key)

root.mainloop()