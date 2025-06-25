website = input("Type in the website you wish to block (dont add www before): ")
bool = True
host = r"C:\Windows\System32\drivers\etc\hosts"

with open(host,"rt") as f:
    for x in f:
        if x.find(website)>=0:
            print("This website has already been blocked. Please try again.")
            bool = False
    if bool:
        with open(host, "a") as f:
            f.write("127.0.0.1  " + website)
            f.write("127.0.0.1  " + "www." + website)
