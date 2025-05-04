import tkinter as tk
from tkinter import messagebox
import time

def submit_form(auto_fill=False):
    start_time = time.time()
    if auto_fill:
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        username_entry.insert(0, "testuser")
        password_entry.insert(0, "testpassword")
    username = username_entry.get()
    password = password_entry.get()
    end_time = time.time()
    messagebox.showinfo("Result", f"Username: {username}\nPassword: {password}\nTime: {end_time - start_time:.2f}s")

root = tk.Tk()
root.title("Login Form")
tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()
tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
tk.Button(root, text="Manual Submit", command=lambda: submit_form()).pack()
tk.Button(root, text="Auto-Fill Submit", command=lambda: submit_form(auto_fill=True)).pack()
root.mainloop()