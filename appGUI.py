import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from WebsiteBlocker import block_website, unblock_website
from passwordchecker import check_email_for_spam, check_password_strength, show_help

app = tk.Tk()
app.geometry("500x300")
app.title("Cybersecurity Hub")


tabs = ttk.Notebook(app)
tabs.pack(fill="both", expand=True, padx=20, pady=20)

# Tab 1: Email Scam Scanner
tab_email = ttk.Frame(tabs)
tabs.add(tab_email, text="Email Scam Scanner")

tk.Label(tab_email, text="Enter your email and app password to scan your inbox.").pack(pady=(10, 5))

tk.Label(tab_email, text="Email:").pack()
entry_email = tk.Entry(tab_email, width=50)
entry_email.pack(pady=2)

tk.Label(tab_email, text="App Password:").pack()
entry_password = tk.Entry(tab_email, width=50, show="*")
entry_password.pack(pady=2)

tk.Button(tab_email, text="Check My Email for Scams", 
          command=lambda: check_email_for_spam(entry_email.get(), entry_password.get())).pack(pady=10)

tk.Button(tab_email, text="How to Get App Password", command=show_help).pack(pady=(0, 10))

# Tab 2: Password Checker
tab_password = ttk.Frame(tabs)
tabs.add(tab_password, text="Password Checker")

tk.Label(tab_password, text="Enter a password:").pack(pady=5)
entry_pw = tk.Entry(tab_password, width=50, show="*")
entry_pw.pack(pady=5)

label_pw_result = tk.Label(tab_password, text="", font=("Arial", 16))
label_pw_result.pack(pady=10)

def handle_password_check():
    password = entry_pw.get()
    result = check_password_strength(password)
    label_pw_result.config(text=f"Password Strength: {result}")

tk.Button(tab_password, text="Check Strength", command=handle_password_check).pack(pady=5)

# === Website Blocker Tab ===
blocker_tab = ttk.Frame(tabs)
tabs.add(blocker_tab, text="Website Blocker")

ttk.Label(blocker_tab, text="Select Block or Unblock Website:").pack(pady=10)

button_frame = ttk.Frame(blocker_tab)
button_frame.pack(pady=0)
selected = tk.StringVar(value="")
ttk.Radiobutton(button_frame, text="Block", variable=selected, value="Y").pack(side="left", padx=5)
ttk.Radiobutton(button_frame, text="Unblock", variable=selected, value="N").pack(side="left", padx=5)

ttk.Label(blocker_tab, text="Enter Website URL (without the www.):").pack(pady=10)

website_entry = ttk.Entry(blocker_tab, width=40)
website_entry.pack(pady=0)


def block_handler():
    query = selected.get()
    website = website_entry.get().strip()
    if not website:
        messagebox.showwarning("Input Error", "Please enter a valid website.")
        return
    if query == "Y":
        result = block_website(website)
    elif query == "N":
        result = unblock_website(website)
    if result == "success":
        if query == "Y":
            action="Blocked"
        else:
            action="Unblocked"
        messagebox.showinfo("Success!", f"Website {action.lower()} successfully.")
    elif result == "already_blocked":
        messagebox.showinfo("Already Blocked", "This website has already been blocked.")
    elif result == "not_blocked":
        messagebox.showinfo("Not currently blocked", "This website is not currently blocked.")
    


ttk.Button(blocker_tab, text="Block/Unblock Website", command=block_handler).pack(pady=15)

# === Firewall Tab ===
firewall_tab = ttk.Frame(tabs)
tabs.add(firewall_tab, text="Firewall")
is_on = False

def toggle():
    global is_on
    is_on = not is_on
    if is_on:
        toggle_btn.config(text="ON")
    else:
        toggle_btn.config(text="OFF")

toggle_btn = ttk.Button(firewall_tab, text="OFF", width=10, command=toggle)
toggle_btn.pack(pady=80)
app.mainloop()
