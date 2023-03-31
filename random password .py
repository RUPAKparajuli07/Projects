import random
import string
import tkinter as tk

def generate_password(length):
    """Generate a random password with given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def is_complex(password):
    """Check if a password is complex."""
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    return has_lowercase and has_uppercase and has_digit and has_special

def generate():
    """Generate a complex password and display it in the GUI."""
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError
    except ValueError:
        password_label.configure(text="Invalid input. Please enter a positive integer.")
        return

    while True:
        password = generate_password(length)
        if is_complex(password):
            break

    password_label.configure(text=password, foreground="#006400") # Set text color to dark green

# Create a new Tkinter window
window = tk.Tk()
window.title("Random Password Generator")

# Add a label and an entry field for password length
length_label = tk.Label(window, text="Enter password length:", font=("Arial", 14), foreground="white", background="#3B3B3B")
length_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
length_entry = tk.Entry(window, font=("Arial", 14))
length_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Add a button to generate a password
generate_button = tk.Button(window, text="Generate Password", command=generate, font=("Arial", 14), foreground="#3B3B3B", background="#C4C4C4")
generate_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Add a label to display the generated password
password_label = tk.Label(window, text="", font=("Arial", 14), foreground="#006400", background="white")
password_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Set the size and background color of the window and center it
window.geometry("400x300")
window.configure(background="#3B3B3B")
window.eval('tk::PlaceWindow . center')

# Start the Tkinter event loop
window.mainloop()

