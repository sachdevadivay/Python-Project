import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
import datetime
import time
import math

# ---------------- THEME ----------------
COLORS = {
    "bg": "#05070a",
    "side": "#0d1117",
    "card": "#161b22",
    "accent": "#58a6ff",
    "success": "#238636",
    "border": "#30363d",
    "text": "#c9d1d9"
}

class NovaFinal:
    def __init__(self, root):
        self.root = root
        self.root.title("NOVA ULTIMATE | Divay Sachdeva")
        self.root.geometry("1250x850")
        self.root.configure(bg=COLORS["bg"])

        self.start_time = time.time()
        self.admin_pass = "Sachdiv@1"

        self.init_db()
        self.show_login()

    # ---------------- DATABASE ----------------
    def init_db(self):
        conn = sqlite3.connect("nova.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS goals (id INTEGER PRIMARY KEY, task TEXT, status TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS logs (activity TEXT, time TEXT)")
        conn.commit()
        conn.close()

    def add_log(self, activity):
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        conn = sqlite3.connect("nova.db")
        conn.execute("INSERT INTO logs VALUES (?, ?)", (activity, ts))
        conn.commit()
        conn.close()

    # ---------------- LOGIN ----------------
    def show_login(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg=COLORS["side"], padx=40, pady=40)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="🔐 NOVA LOGIN",
                 font=("Segoe UI", 22, "bold"),
                 fg=COLORS["accent"], bg=COLORS["side"]).pack(pady=10)

        self.p_ent = tk.Entry(frame, show="*", font=("Segoe UI", 14), width=25)
        self.p_ent.pack(pady=20)

        tk.Button(frame, text="LOGIN",
                  command=self.verify,
                  bg=COLORS["accent"], fg="black",
                  width=20).pack()

    def verify(self):
        if self.p_ent.get() == self.admin_pass:
            self.add_log("Login Success")
            self.main_ui()
        else:
            messagebox.showerror("Error", "Wrong Password")

    # ---------------- MAIN UI ----------------
    def main_ui(self):
        self.clear_screen()

        side = tk.Frame(self.root, bg=COLORS["side"], width=260)
        side.pack(side="left", fill="y")

        tk.Label(side, text="NOVA",
                 fg=COLORS["accent"],
                 bg=COLORS["side"],
                 font=("Segoe UI", 26, "bold")).pack(pady=20)

        buttons = [
            ("🏠 Dashboard", self.dashboard),
            ("🎯 Goals", self.goals_ui),
            ("🧮 Math", self.math_ui),
            ("📜 Logs", self.logs_ui),
            ("ℹ️ About", self.about_ui)
        ]

        # ✅ ONLY CHANGE: FONT SIZE + PADDING
        for t, cmd in buttons:
            b = tk.Button(side, text=t,
                          command=cmd,
                          bg=COLORS["side"], fg="white",
                          font=("Segoe UI", 14, "bold"),  # changed
                          bd=0, anchor="w",
                          padx=20, pady=8)  # added spacing
            b.pack(fill="x", padx=20, pady=5)

            b.bind("<Enter>", lambda e, btn=b: btn.config(bg=COLORS["accent"], fg="black"))
            b.bind("<Leave>", lambda e, btn=b: btn.config(bg=COLORS["side"], fg="white"))

        self.timer = tk.Label(side, fg=COLORS["accent"], bg=COLORS["side"])
        self.timer.pack(side="bottom", pady=20)
        self.update_timer()

        self.main = tk.Frame(self.root, bg=COLORS["bg"])
        self.main.pack(side="right", expand=True, fill="both")

        self.dashboard()

    # ---------------- DASHBOARD ----------------
    def dashboard(self):
        self.clear_main()

        tk.Label(self.main,
                 text="Nova – The Smart Assistant",
                 font=("Segoe UI", 30, "bold"),
                 fg=COLORS["accent"], bg=COLORS["bg"]).pack(expand=True)

        tk.Label(self.main,
                 text="Your Personal Python-Based AI System",
                 font=("Segoe UI", 14),
                 fg="white", bg=COLORS["bg"]).pack()

        tk.Label(self.main,
                 text="Divay Sachdeva | BTech CSE 1st Year",
                 font=("Segoe UI", 11, "bold"),
                 fg=COLORS["text"], bg=COLORS["bg"]).pack(side="bottom", pady=20)

    # ---------------- GOALS ----------------
    def goals_ui(self):
        self.clear_main()

        tk.Label(self.main, text="🎯 Goal Manager",
                 font=("Segoe UI", 22, "bold"),
                 fg=COLORS["accent"], bg=COLORS["bg"]).pack(pady=20)

        container = tk.Frame(self.main, bg=COLORS["bg"])
        container.pack()

        task = tk.Entry(container, font=("Segoe UI", 12), width=30)
        task.grid(row=0, column=0, padx=10)

        def add():
            t = task.get()
            if t:
                conn = sqlite3.connect("nova.db")
                conn.execute("INSERT INTO goals (task, status) VALUES (?,?)", (t, "Pending"))
                conn.commit()
                conn.close()
                self.add_log(f"Added goal: {t}")
                self.goals_ui()

        tk.Button(container, text="➕ Add",
                  command=add,
                  bg=COLORS["success"], fg="white").grid(row=0, column=1)

        conn = sqlite3.connect("nova.db")
        data = conn.execute("SELECT * FROM goals").fetchall()
        conn.close()

        for g in data:
            card = tk.Frame(self.main, bg=COLORS["card"])
            card.pack(fill="x", padx=80, pady=5)

            tk.Label(card, text=g[1], fg="white", bg=COLORS["card"]).pack(side="left", padx=15)

            tk.Button(card, text="✔ Done",
                      command=lambda id=g[0]: self.mark_done(id),
                      bg=COLORS["accent"], fg="black").pack(side="right", padx=5)

            tk.Button(card, text="❌ Delete",
                      command=lambda id=g[0]: self.delete_goal(id),
                      bg="#ef4444", fg="white").pack(side="right", padx=5)

    def mark_done(self, id):
        conn = sqlite3.connect("nova.db")
        conn.execute("UPDATE goals SET status='Done' WHERE id=?", (id,))
        conn.commit()
        conn.close()
        self.add_log("Marked goal done")
        self.goals_ui()

    def delete_goal(self, id):
        conn = sqlite3.connect("nova.db")
        conn.execute("DELETE FROM goals WHERE id=?", (id,))
        conn.commit()
        conn.close()
        self.add_log("Deleted goal")
        self.goals_ui()

    # ---------------- ADVANCED MATH ----------------
    def math_ui(self):
        self.clear_main()

        tk.Label(self.main, text="🧮 Advanced Math Lab",
                 font=("Segoe UI", 26, "bold"),
                 fg=COLORS["accent"], bg=COLORS["bg"]).pack(pady=20)

        grid = tk.Frame(self.main, bg=COLORS["bg"])
        grid.pack()

        def safe_float(p):
            try:
                return simpledialog.askfloat("Input", p)
            except:
                messagebox.showerror("Error", "Invalid Input")

        funcs = [
            ("Square", lambda: messagebox.showinfo("Result", safe_float("Enter number")**2)),
            ("Root", lambda: messagebox.showinfo("Result", math.sqrt(safe_float("Enter number")))),
            ("Power", lambda: messagebox.showinfo("Result", safe_float("Base")**safe_float("Exponent"))),
            ("Log", lambda: messagebox.showinfo("Result", math.log10(safe_float("Enter number")))),
            ("Factorial", lambda: messagebox.showinfo("Result", math.factorial(simpledialog.askinteger("Input","Enter integer")))),
            ("Trig", lambda: messagebox.showinfo("Result", math.sin(math.radians(safe_float("Angle"))))),
            ("Percentage", lambda: messagebox.showinfo("Result", (safe_float("Part")/safe_float("Total"))*100)),
            ("Solve ax+b", lambda: messagebox.showinfo("Result", -safe_float("b")/safe_float("a")))
        ]

        r=c=0
        for t,f in funcs:
            b=tk.Button(grid,text=t,command=f,width=18,height=3,
                        bg=COLORS["card"],fg="white",bd=0)
            b.grid(row=r,column=c,padx=15,pady=15)

            b.bind("<Enter>", lambda e,btn=b: btn.config(bg=COLORS["accent"],fg="black"))
            b.bind("<Leave>", lambda e,btn=b: btn.config(bg=COLORS["card"],fg="white"))

            c+=1
            if c==3:
                c=0;r+=1

    # ---------------- LOGS ----------------
    def logs_ui(self):
        self.clear_main()

        tk.Label(self.main, text="📜 Logs",
                 font=("Segoe UI", 20, "bold"),
                 fg=COLORS["accent"], bg=COLORS["bg"]).pack(pady=10)

        txt = tk.Text(self.main, bg=COLORS["side"], fg="white")
        txt.pack(fill="both", expand=True, padx=40, pady=10)

        conn = sqlite3.connect("nova.db")
        logs = conn.execute("SELECT * FROM logs").fetchall()
        conn.close()

        for l in logs:
            txt.insert("end", f"{l[1]} - {l[0]}\n")

    # ---------------- ABOUT ----------------
    def about_ui(self):
        self.clear_main()

        tk.Label(self.main, text="ℹ️ About NOVA",
             font=("Segoe UI", 28, "bold"),
             fg=COLORS["accent"], bg=COLORS["bg"]).pack(pady=20)

        canvas = tk.Canvas(self.main, bg=COLORS["bg"], highlightthickness=0)
        scrollbar = tk.Scrollbar(self.main, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=COLORS["bg"])

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=40)
        scrollbar.pack(side="right", fill="y")

        card = tk.Frame(scroll_frame, bg=COLORS["card"], padx=30, pady=25)
        card.pack(fill="both", expand=True)

        tk.Label(card, text="👨‍💻 Developer",
             font=("Segoe UI", 16, "bold"),
             fg=COLORS["accent"], bg=COLORS["card"]).pack(anchor="w")

        tk.Label(card, text="Divay Sachdeva\nBTech CSE | 1st Year",
             fg="white", bg=COLORS["card"]).pack(anchor="w", pady=10)

        tk.Label(card, text="📚 Topics Covered",
             font=("Segoe UI", 16, "bold"),
             fg=COLORS["accent"], bg=COLORS["card"]).pack(anchor="w")

        topics = [
        "Python Basics (Variables, Data Types)",
        "Control Structures (Loops, Conditions)",
        "Functions & Modular Programming",
        "Object-Oriented Programming (Classes & Objects)",
        "SQLite Database (CRUD Operations)",
        "GUI Development using Tkinter",
        "Mathematical Computation using math module",
        "Error Handling (try-except)"
    ]

        for t in topics:
            tk.Label(card, text="✔ " + t, fg="white", bg=COLORS["card"]).pack(anchor="w")

    # ---------------- TIMER ----------------
    def update_timer(self):
        t = int(time.time() - self.start_time)
        self.timer.config(text=f"{t}s")
        self.root.after(1000, self.update_timer)

    def clear_screen(self):
        for w in self.root.winfo_children():
            w.destroy()

    def clear_main(self):
        for w in self.main.winfo_children():
            w.destroy()

# ---------------- RUN ----------------
root = tk.Tk()
app = NovaFinal(root)
root.mainloop()
