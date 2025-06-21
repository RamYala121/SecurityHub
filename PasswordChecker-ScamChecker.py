import tkinter as tk
from tkinter import ttk
import re

# --- Suspicious Keywords ---
suspicious_keywords = [
    "urgent", "verify", "account", "login", "click", "update", "password", "bank", "invoice", "guaranteed",
    "act now", "card", "payment", "claim", "money back", "suspended", "deactivated", "compromised", "alert", "unusual activity",
    "unauthorized", "limited access", "breach", "flagged", "locked", "secure message", "firewall", "risk", "secure server",
    "administrator", "helpdesk", "tech support", "official", "compliance", "security team", "resolution center", "IT department", "federal",
    "service desk", "enforcement", "internal affairs", "reward", "free gift", "promotion", "offer expires", "winner",
    "congratulations", "loyalty bonus", "exclusive offer", "no cost", "zero cost", "sweepstakes", "redeem", "selected", "pre-approved",
    "limited time", "expires soon", "deadline", "final notice", "last chance", "immediate response", "ends today", "today only", "closing soon",
    "billing", "payroll", "deposit", "wire transfer", "overdue", "transaction", "statement", "purchase", "shipping notice",
    "receipt", "refund", "escalation", "balance", "access now", "open here", "check now", "go here", "continue", "unlock",
    "respond", "act here", "confirm", "complete", "accept", "authorize", "enable", "download", "webmail", "portal", "online notice", "secure-web", "mailhub", "intranet",
    ".ru", ".tk", ".ml", "cloud-storage", "friend request", "reconnect", "see who viewed", "tagged you", "message waiting", "secret",
    "private document", "unknown sender", "gift card", "invitation", "warning", "error", "fail", "mistake", "concern", "trouble",
    "action required", "immediate attention", "disappointment", "unauthorized use"
]

# --- Common Passwords ---
common_passwords = [
    "123456", "password", "123456789", "12345678", "12345", "111111", "123123", "abc123", "qwerty", "letmein", "iloveyou", "admin", "welcome",
    "monkey", "login", "football", "1234", "passw0rd", "starwars", "dragon", "1234567", "1234567890", "000000", "123321", "1q2w3e4r", "654321",
    "7777777", "112233", "qwertyuiop", "qazwsx", "password1", "zaq12wsx", "lovely", "sunshine", "welcome1", "master", "login1", "trustno1",
    "letmein1", "admin123", "hello123", "freedom", "whatever", "123qwe", "baseball", "superman", "harley", "batman", "hottie", "flower",
    "shadow", "pokemon", "cheese", "iloveyou1", "asdfgh", "pass123", "monkey123", "access", "michelle", "princess", "secret", "cookie",
    "blink182", "ninja", "summer", "pepper", "tigger", "jordan23", "hunter", "killer", "soccer", "qwe123", "michael", "charlie", "matrix"
]

# --- Logic ---
def check_password_strength(password):
    if password.lower() in common_passwords:
        return "Weak (Common Password)"
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    score = sum([length, bool(upper), bool(lower), bool(digit), bool(symbol)])
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

def is_phishing(email_text):
    email_text = email_text.lower()
    for keyword in suspicious_keywords:
        if keyword in email_text:
            print(f"Matched keyword: {keyword}")
            return True
    return False

# --- Main Interface with Tabs ---
def launch_main_interface(default_tab=0):
    root = tk.Tk()
    root.title("Cybersecurity Hub")
    notebook = ttk.Notebook(root)

    # --- Password Tab ---
    tab_password = ttk.Frame(notebook)
    notebook.add(tab_password, text="Password Checker")

    ttk.Label(tab_password, text="Enter password:").pack(pady=5)
    entry_pass = ttk.Entry(tab_password, width=50, show="*")
    entry_pass.pack(pady=5)
    label_pass_result = ttk.Label(tab_password, text="", font=("Arial", 16))
    label_pass_result.pack(pady=10)

    def check_pass():
        result = check_password_strength(entry_pass.get())
        label_pass_result.config(text=f"Password Strength: {result}")

    ttk.Button(tab_password, text="Check", command=check_pass).pack()

    # --- Scam Tab ---
    tab_scam = ttk.Frame(notebook)
    notebook.add(tab_scam, text="Scam Checker")

    ttk.Label(tab_scam, text="Enter email or message:").pack(pady=5)
    entry_scam = ttk.Entry(tab_scam, width=50)
    entry_scam.pack(pady=5)
    label_scam_result = ttk.Label(tab_scam, text="", font=("Arial", 16))
    label_scam_result.pack(pady=10)

    def check_scam():
        phishing = is_phishing(entry_scam.get())
        if phishing:
            label_scam_result.config(text="⚠️ Potential phishing detected.")
        else:
            label_scam_result.config(text="✅ Looks clean.")

    ttk.Button(tab_scam, text="Check", command=check_scam).pack()

    notebook.pack(expand=True, fill="both", padx=10, pady=10)
    notebook.select(default_tab)
    root.mainloop()

# --- Startup Prompt ---
def startup_prompt():
    splash = tk.Tk()
    splash.title("Start")

    tk.Label(splash, text="Which checker do you want to use first?", font=("Arial", 14)).pack(pady=10)

    def launch(tab_index):
        splash.destroy()
        launch_main_interface(tab_index)

    tk.Button(splash, text="Password Checker", width=25, command=lambda: launch(0)).pack(pady=5)
    tk.Button(splash, text="Scam Checker", width=25, command=lambda: launch(1)).pack(pady=5)

    splash.mainloop()

# --- Run the App ---
startup_prompt()
