import tkinter as tk
from tkinter import ttk, messagebox
import imaplib
import email
from email.header import decode_header
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
    "action required", "immediate attention", "disappointment", "unauthorized use","identity", "credentials", "logon", "authentication", "security alert", "policy violation",
    "verify ownership", "terms breach", "compliance required", "device alert", "unrecognized login",
    "unexpected activity", "security incident", "session expired", "validate now", "temporary hold",
    "pending action", "take action", "follow instructions", "account review", "malware alert",
    "virus found", "urgent response", "login attempt", "validate identity", "your details",
    "next steps", "escalated issue", "action needed", "restore access", "process interrupted",
    "alert center", "fraud prevention", "privacy issue", "login portal", "recovery steps",
    "escalation required", "system alert", "detection notice", "pending verification", "forced logout",
    "credentials at risk", "reactivate", "critical alert", "fail-safe", "system detected",
    "device flagged", "document expired", "process failure", "irregular activity", "alert system",
    "attention needed", "access error", "identity confirmation", "system log", "compliance action",
    "form required", "service alert", "identity token", "security key", "restricted content",
    "access verification", "form submission", "authentication error", "update required",
    "network notice", "service change", "continue here", "document required", "re-authenticate"
]

# --- Common Passwords ---
common_passwords = [
    "123456", "password", "123456789", "12345678", "12345", "111111", "123123", "abc123", "qwerty", "letmein", "iloveyou", "admin", "welcome",
    "monkey", "login", "football", "1234", "passw0rd", "starwars", "dragon", "1234567", "1234567890", "000000", "123321", "1q2w3e4r", "654321",
    "7777777", "112233", "qwertyuiop", "qazwsx", "password1", "zaq12wsx", "lovely", "sunshine", "welcome1", "master", "login1", "trustno1",
    "letmein1", "admin123", "hello123", "freedom", "whatever", "123qwe", "baseball", "superman", "harley", "batman", "hottie", "flower",
    "shadow", "pokemon", "cheese", "iloveyou1", "asdfgh", "pass123", "monkey123", "access", "michelle", "princess", "secret", "cookie",
    "blink182", "ninja", "summer", "pepper", "tigger", "jordan23", "hunter", "killer", "soccer", "qwe123", "michael", "charlie", "matrix", 
    "andrea", "angela", "anthony", "arizona", "arthur", "austin", "babyboy", "babygirl", "bachelor", "badger",
    "beagle", "bear123", "beatles", "beauty", "bigred", "billie", "billy", "blazer", "blink", "bobby",
    "brandon", "brazil", "bulldog", "butterfly", "california", "candy", "carter", "casper", "charles", "cherry",
    "chester", "chevy", "cinnamon", "claire", "classic", "clover", "colt45", "cookie1", "copper", "coyote",
    "dakota1", "dancer", "darkness", "daytona", "destiny", "diamond123", "disney", "dolphins", "domino", "donkey",
    "dragonfly", "dreamer", "dylan", "eclipse", "electric", "emily", "empire", "everest", "explorer", "falcon",
    "family", "fantasy", "farmer", "fender", "festival", "fireball", "firebird", "fisher", "flamingo", "florida",
    "flowers", "forest", "forever", "friday", "friendly", "frosty", "garfield", "gemini", "georgia", "gobears",
    "golfing", "gotham", "green123", "guitar", "haley", "happy1", "harley1", "hawaii", "hazel", "hearts",
    "herman", "honey", "horsey", "houston", "iceman", "infinity", "ironman", "isabelle", "island", "italy","jacob", 
    "jasper", "jason1", "jeremy", "jerry", "joanna", "joey123", "johnny", "jonathan", "joseph",
    "joshua1", "junior", "justine", "karate", "karen", "katherine", "katie", "kennedy", "kenneth", "kevin123",
    "khalid", "kimberly", "kitten", "kristen", "lacrosse", "larry", "laura", "lawrence", "legend", "lemonade",
    "leonard", "lexus", "lightning", "lillian", "lincoln", "linda123", "lindsey", "lionel", "lions", "london1",
    "louise", "lucky1", "lunar", "madison", "magicman", "malibu", "mango", "mariah", "marvin", "maxwell",
    "meadow", "melanie", "meredith", "metallica", "mexico", "miami", "midwest", "minnie", "miracle", "misty1",
    "mocha", "monday", "montana", "moose1", "mother", "motorola", "movie123", "musicman", "mybaby", "nashville",
    "natasha", "neptune", "newcastle", "newyork1", "nicolas", "nintendo", "noah123", "norway", "notebook", "october",
    "olivia1", "omega", "ontario", "orange1", "orlando", "oscar1", "painter", "panama", "parker", "parrot",
    "passkey", "passlock", "patrick1", "penguin1", "peppermint", "phoebe", "phoenix1", "picasso", "pilot123", "pirate",
    "planet1", "platinum", "pluto123", "popcorn", "precious", "presley", "pretty1", "princess1", "puzzle1", "python123"
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