import re
import tkinter as tk
from tkinter import messagebox

def valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    else:
        return False
    
def validate_email():
    email = email_entry.get()
    if valid_email(email):
        messagebox.showinfo("Success", f"{email} is a valid email address.")
    else:
        messagebox.showerror("Error", f"{email} is not a valid email address.")

root = tk.Tk()
root.title("Email Validation")

label = tk.Label(root, text="Enter an email address:", wraplength=300, justify="center")
label.pack(pady=10)
email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=10)
validate_button = tk.Button(root, text="Validate Email", command=validate_email)
validate_button.pack(pady=20)

root.mainloop()


""" def valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_regex, email):
        return True
    else:
        return False

email = input("Enter an email address: ")

if valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
 """