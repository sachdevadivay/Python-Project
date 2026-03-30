import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import datetime
import string

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("NOVA - Animated Assistant")
root.geometry("600x700")
root.configure(bg="#0d1117")
root.resizable(False, False)

# -------- Fade-in Animation --------
root.attributes("-alpha", 0.0)

def fade_in(alpha=0):
    alpha += 0.02
    if alpha <= 1:
        root.attributes("-alpha", alpha)
        root.after(20, lambda: fade_in(alpha))

fade_in()

# ---------------- HEADER ----------------
header = tk.Frame(root, bg="#161b22", height=120)
header.pack(fill="x")

title = tk.Label(
    header,
    text="NOVA",
    font=("Segoe UI", 28, "bold"),
    fg="#58a6ff",
    bg="#161b22"
)
title.pack(pady=(25, 5))

subtitle = tk.Label(
    header,
    text="Modern Python Assistant  |  Welcome Divay 👋",
    font=("Segoe UI", 12),
    fg="#c9d1d9",
    bg="#161b22"
)
subtitle.pack()

# ---------------- CONTENT FRAME ----------------
content = tk.Frame(root, bg="#0d1117")
content.pack(pady=30)

# ---------------- FUNCTIONS ----------------

def calculator():
    try:
        a = float(simpledialog.askstring("Calculator", "Enter first number:"))
        b = float(simpledialog.askstring("Calculator", "Enter second number:"))
        op = simpledialog.askstring("Calculator", "Enter operator (+ - * /):")

        if op == "+": result = a + b
        elif op == "-": result = a - b
        elif op == "*": result = a * b
        elif op == "/": result = a / b
        else: result = "Invalid Operator"

        messagebox.showinfo("Result", f"Result: {result}")
    except:
        messagebox.showerror("Error", "Invalid Input")

def even_odd():
    try:
        n = int(simpledialog.askstring("Even/Odd", "Enter number:"))
        result = "Even Number" if n % 2 == 0 else "Odd Number"
        messagebox.showinfo("Result", result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def table():
    try:
        n = int(simpledialog.askstring("Table Generator", "Enter number:"))
        result = ""
        for i in range(1, 11):
            result += f"{n} x {i} = {n*i}\n"
        messagebox.showinfo("Table", result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def joke():
    jokes = [
        "Why do programmers love Python? Because it is simple.",
        "Why was the computer cold? It left Windows open.",
        "Why did the developer go broke? Because he used up all his cache."
    ]
    messagebox.showinfo("Joke", random.choice(jokes))

def password():
    try:
        length = int(simpledialog.askstring("Password", "Enter length:"))
        chars = string.ascii_letters + string.digits
        pwd = "".join(random.choice(chars) for _ in range(length))
        messagebox.showinfo("Generated Password", pwd)
    except:
        messagebox.showerror("Error", "Invalid Length")

def show_date():
    messagebox.showinfo("Date", datetime.datetime.now().strftime("%d %B %Y"))

def show_time():
    messagebox.showinfo("Time", datetime.datetime.now().strftime("%H:%M:%S"))

# ---------------- BUTTON STYLE WITH ANIMATION ----------------

def create_button(text, command):
    btn = tk.Button(
        content,
        text=text,
        command=command,
        font=("Segoe UI", 13),
        width=30,
        height=2,
        bg="#21262d",
        fg="white",
        bd=0,
        cursor="hand2"
    )

    # Hover animation
    def on_enter(e):
        btn.config(bg="#58a6ff", fg="black")

    def on_leave(e):
        btn.config(bg="#21262d", fg="white")

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    return btn

# ---------------- BUTTONS ----------------

create_button("🧮  Calculator", calculator).pack(pady=8)
create_button("🔢  Even / Odd Checker", even_odd).pack(pady=8)
create_button("📊  Table Generator", table).pack(pady=8)
create_button("😂  Joke Teller", joke).pack(pady=8)
create_button("🔐  Password Generator", password).pack(pady=8)
create_button("📅  Show Date", show_date).pack(pady=8)
create_button("⏰  Show Time", show_time).pack(pady=8)

# Exit button
exit_btn = tk.Button(
    root,
    text="Exit Application",
    command=root.destroy,
    font=("Segoe UI", 13, "bold"),
    width=30,
    height=2,
    bg="#da3633",
    fg="white",
    bd=0,
    cursor="hand2"
)
exit_btn.pack(pady=30)

# Exit hover animation
exit_btn.bind("<Enter>", lambda e: exit_btn.config(bg="#ff7b72"))
exit_btn.bind("<Leave>", lambda e: exit_btn.config(bg="#da3633"))

root.mainloop()

