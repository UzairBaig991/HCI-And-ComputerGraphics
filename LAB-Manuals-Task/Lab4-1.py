import tkinter as tk
import threading, time, random
def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Notification")
    tk.Label(popup, text="New Message!").pack()
    popup.after(2000, popup.destroy)
def random_popups():
    while True:
        time.sleep(random.randint(3, 8))
        root.after(0, show_popup)
root = tk.Tk()
root.title("Attention Test")
tk.Label(root, text="Read the text carefully and ignore popups.").pack()
threading.Thread(target=random_popups, daemon=True).start()
root.mainloop()