import tkinter as tk
from tkinter import ttk

# Create the main application window
app = tk.Tk()
app.geometry("600x400")
app.title("ADD TITLE HERE")

# Create the tab system using ttk.Notebook
tabs = ttk.Notebook(app)
tabs.pack(fill="both", expand=True, padx=20, pady=20)

# === Email Scam Checker Tab ===
email_tab = tk.Frame(tabs)
tabs.add(email_tab, text="Email Scam Checker")

tk.Label(email_tab, text="Scan last 10 emails for possible scams").pack(pady=10)

result_label = tk.Label(email_tab, text="")
result_label.pack(pady=10)

def scan_emails():
    # TODO: Replace with actual email scanning function
    result_label.config(text="Scanning last 10 emails...(placeholder)")

scan_button = tk.Button(email_tab, text="Scan Emails", command=scan_emails)
scan_button.pack(pady=10)

# === Password Strength Checker Tab ===
password_tab = tk.Frame(tabs)
tabs.add(password_tab, text="Password Strength Checker")

tk.Label(password_tab, text="Input Password to Check Strength").pack(pady=10)

password_entry = tk.Entry(password_tab, show="*")
password_entry.pack(pady=5)
password_entry.insert(0, "Enter Password")  # Simulating placeholder

password_result_label = tk.Label(password_tab, text="")
password_result_label.pack(pady=10)

def check_password_strength():
    password = password_entry.get()
    password_result_label.config(text="password strength")  # Placeholder

check_button = tk.Button(password_tab, text="Check Strength", command=check_password_strength)
check_button.pack(pady=5)

# Run the app
app.mainloop()