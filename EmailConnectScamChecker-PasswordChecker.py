import tkinter as tk
from tkinter import ttk, messagebox
import imaplib
import email
from email.header import decode_header
import re

# --- Suspicious Keywords ---
suspicious_keywords = [  # shortened here for readability — use your full list
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

def is_phishing(text):
    text = text.lower()
    for keyword in suspicious_keywords:
        if keyword in text:
            print(f"Matched keyword: {keyword}")
            return True
    return False

# --- Email Scanner ---
def check_email_for_spam():
    IMAP_SERVER = "imap.gmail.com"
    EMAIL_USER = "c4g.testing@gmail.com"         # ← Replace this
    EMAIL_PASS = "lgxfqgsgrtcifoey"              # ← Replace this (App Password if using Gmail 2FA)

    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")

        status, messages = mail.search(None, 'ALL')
        mail_ids = messages[0].split()
        last_10 = reversed(mail_ids[-10:])

        found_spam = False
        for num in last_10:
            status, data = mail.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(data[0][1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8", errors="ignore")

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        try:
                            body = part.get_payload(decode=True).decode(errors="ignore")
                            break
                        except:
                            pass
            else:
                try:
                    body = msg.get_payload(decode=True).decode(errors="ignore")
                except:
                    body = ""

            if is_phishing(subject + " " + body):
                found_spam = True
                messagebox.showwarning("Phishing Alert", f"⚠️ Scam detected in:\n\nSubject: {subject}")
                break

        if not found_spam:
            messagebox.showinfo("Email Scan", "✅ No scams found in the last 10 emails.")

        mail.logout()

    except Exception as e:
        messagebox.showerror("Error", f"Could not connect to email:\n\n{e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Cybersecurity Hub")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# --- Tab 1: Email Scam Scanner (Now First) ---
tab_email = ttk.Frame(notebook)
notebook.add(tab_email, text="Email Scam Scanner")

label_email_info = tk.Label(tab_email, text="Click the button below to scan your last 10 emails for scams.")
label_email_info.pack(pady=20)

btn_email_check = tk.Button(tab_email, text="Check My Email for Scams", command=check_email_for_spam)
btn_email_check.pack(pady=10)

# --- Tab 2: Password Checker ---
tab_password = ttk.Frame(notebook)
notebook.add(tab_password, text="Password Checker")

label_pw = tk.Label(tab_password, text="Enter a password:")
label_pw.pack(pady=5)

entry_pw = tk.Entry(tab_password, width=50, show="*")
entry_pw.pack(pady=5)

label_pw_result = tk.Label(tab_password, text="", font=("Arial", 16))
label_pw_result.pack(pady=10)

def handle_password_check():
    password = entry_pw.get()
    result = check_password_strength(password)
    label_pw_result.config(text=f"Password Strength: {result}")

btn_pw_check = tk.Button(tab_password, text="Check Strength", command=handle_password_check)
btn_pw_check.pack(pady=5)

root.mainloop()