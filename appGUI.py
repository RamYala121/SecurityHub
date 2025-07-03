import customtkinter as ctk

# App Appearance
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x400")
app.title("ADD TITLE HERE")

tabs = ctk.CTkTabview(app)
tabs.pack(fill="both", expand=True, padx=20, pady=20)

tabs.add("Email Scam Checker")
tabs.add("Password Strength Checker")
tabs.add("Website Blocker")
tabs.add("Firewall")

# === Email Scam Checker Tab ===
email_tab = tabs.tab("Email Scam Checker")

ctk.CTkLabel(email_tab, text="Scan last 10 emails for possible scams").pack(pady=10)

result_label = ctk.CTkLabel(email_tab, text="")
result_label.pack(pady=10)

def scan_emails():
    # TODO: Replace this with the actual email scanning function
    # Below is a placeholder
    result_label.configure(text="Scanning last 10 emails...(placeholder)")
    # scam result here

scan_button = ctk.CTkButton(email_tab, text="Scan Emails", command=scan_emails)
scan_button.pack(pady=10)

# === Password Strength Checker ===
password_tab = tabs.tab("Password Strength Checker")

ctk.CTkLabel(password_tab, text="Input Password to Check Strength").pack(pady=10)

password_entry = ctk.CTkEntry(password_tab, placeholder_text="Enter Password", show="*")
password_entry.pack(pady=5)

password_result_label = ctk.CTkLabel(password_tab, text="")
password_result_label.pack(pady=10)

def check_password_strength():
    password = password_entry.get()
    
    # write actual password checker logic here, below is just a placeholder
    password_result_label.configure(text="password strength")

check_button = ctk.CTkButton(password_tab, text="Check Strength", command=check_password_strength)
check_button.pack(pady=5)


app.mainloop()
