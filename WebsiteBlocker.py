query = input("Type Y to block a website and N to unblock a website: ")
bool = True
backup = []
count = 0

if query == "Y":
    website = input("Type in the website you wish to block (dont add www before): ")
    host = r"C:\Windows\System32\drivers\etc\hosts"

    with open(host,"rt") as f:
        for x in f:
            if x.find(website)>=0:
                print("This website has already been blocked. Please try again.")
                break
        if bool:
            with open(host, "a") as f:
                f.write("\n127.0.0.1  " + website)
                f.write("\n127.0.0.1  " + "www." + website)
if query == "N":
    website = input("Type in the website you wish to unblock (dont add www before): ")
    host = r"C:\Windows\System32\drivers\etc\hosts"

    with open(host,"rt") as f:
        for x in f:
            backup.append(x)
            if x.find(website)>0:
                count += 1
        if count == 0:
            print("This website has already been unblocked or it was never blocked. Please try again.")
            bool = False
        if bool:
            filtered_lines = [line for line in backup if website not in line]
            with open(host, "w") as f:
                for y in filtered_lines:
                    f.write(y)
