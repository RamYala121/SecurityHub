import tkinter as tk
import re

suspicious_keywords = ["urgent", "verify", "account", "login", "click", "update", "password", "bank", "invoice", "guaranteed", 
"act now","card", "payment","claim", "money back", "suspended", "deactivated", "compromised", "alert", "unusual activity",
    "unauthorized", "limited access", "breach", "flagged", "locked",
    "secure message", "firewall", "risk", "secure server",

    "administrator", "helpdesk", "tech support", "official", "compliance",
    "security team", "resolution center", "IT department", "federal",
    "service desk", "enforcement", "internal affairs",

    "reward", "free gift", "promotion", "offer expires", "winner",
    "congratulations", "loyalty bonus", "exclusive offer", "no cost",
    "zero cost", "sweepstakes", "redeem", "selected", "pre-approved",

    "limited time", "expires soon", "deadline", "final notice", "last chance",
    "immediate response", "ends today", "today only", "closing soon",

    "billing", "payroll", "deposit", "wire transfer", "overdue",
    "transaction", "statement", "purchase", "shipping notice",
    "receipt", "refund", "escalation", "balance",

    "access now", "open here", "check now", "go here", "continue", "unlock",
    "respond", "act here", "confirm", "complete", "accept", "authorize",
    "enable", "download",

    "webmail", "portal", "online notice", "secure-web", "mailhub", "intranet",
    ".ru", ".tk", ".ml", "cloud-storage",

    "friend request", "reconnect", "see who viewed", "tagged you",
    "message waiting", "secret", "private document", "unknown sender",
    "gift card", "invitation",

    "warning", "error", "fail", "mistake", "concern", "trouble",
    "action required", "immediate attention", "disappointment",
    "unauthorized use"   ]

def check_password_strength(password):
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
            return True
    return False

def on_check():
    choice = var_choice.get()
    user_input = entry_input.get()

    if choice == "P":
        result = check_password_strength(user_input)
        label_result.config(text=f"Password Strength: {result}")
    elif choice == "S":
        phishing = is_phishing(user_input)
        if phishing:
            label_result.config(text="⚠️ Potential phishing detected.")
        else:
            label_result.config(text="✅ Looks clean.")
    else:
        label_result.config(text="Please select P or S.")

# Create main window
root = tk.Tk()
root.title("Cybersecurity Hub")

# Choice input
tk.Label(root, text="Choose checker:").pack()
var_choice = tk.StringVar(value="P")
frame_choices = tk.Frame(root)
tk.Radiobutton(frame_choices, text="Password Checker", variable=var_choice, value="P").pack(side="left")
tk.Radiobutton(frame_choices, text="Scam Checker", variable=var_choice, value="S").pack(side="left")
frame_choices.pack(pady=5)

# User input entry
tk.Label(root, text="Enter password or email text:").pack()
entry_input = tk.Entry(root, width=50)
entry_input.pack(pady=5)

# Check button
btn_check = tk.Button(root, text="Check", command=on_check)
btn_check.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 20))
label_result.pack(pady=10)

root.mainloop()