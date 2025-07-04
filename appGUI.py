import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry("600x400")
app.title("Cybersecurity Hub")

tabs = ttk.Notebook(app)
tabs.pack(fill="both", expand=True, padx=20, pady=20)

# === Email Scam Checker / Password Strength Checker Tab ===
checker_tab = tk.Frame(tabs)
tabs.add(checker_tab, text="Password / Scam Checker")

ttk.Label(checker_tab, text="placeholder").pack(pady=10)

# === Website Blocker Tab ===
blocker_tab = tk.Frame(tabs)
tabs.add(blocker_tab, text="Website Blocker")

ttk.Combobox(blocker_tab, values=["Y","N"]).pack(pady=10)
app.mainloop()