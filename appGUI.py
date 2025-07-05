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
blocker_tab = ttk.Frame(tabs)
tabs.add(blocker_tab, text="Website Blocker")

ttk.Label(blocker_tab, text="Select block or unblock:").pack(pady=10)

button_frame = ttk.Frame(blocker_tab)
button_frame.pack(pady=10)
selected = tk.StringVar(value="")
ttk.Radiobutton(button_frame, text="Block", variable=selected, value="Y").pack(side="left", padx=5)
ttk.Radiobutton(button_frame, text="Unblock", variable=selected, value="N").pack(side="left", padx=5)

ttk.Label(blocker_tab, text="Enter Website URL (without the www.):").pack(pady=10)
ttk.Entry(blocker_tab, placeholder="Website URL").pack(pady=5)
app.mainloop()