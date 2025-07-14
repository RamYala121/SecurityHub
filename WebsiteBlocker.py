def block_website(website):
    query = "Y"
    bool = True
    backup = []
    count = 0
    host = "/etc/hosts"

    if query == "Y":
        try:
            with open(host, "rt") as f:
                for x in f:
                    if x.find(website) >= 0:
                        return "already_blocked"
                        break
            if bool:
                with open(host, "a") as f:
                    f.write("\n127.0.0.1  " + website)
                    f.write("\n127.0.0.1  " + "www." + website)
                return "success"
        except PermissionError:
            return "permission_error"

def unblock_website(website):
    query = "N"
    bool = True
    backup = []
    count = 0
    host = "/etc/hosts"


    if query == "N":
        try:
            with open(host, "rt") as f:
                for x in f:
                    backup.append(x)
                    if x.find(website) > 0:
                        count += 1
            if count == 0:
                bool = False
                return "not_blocked"
            if bool:
                filtered_lines = [line for line in backup if website not in line]
                with open(host, "w") as f:
                    for y in filtered_lines:
                        f.write(y)
                return "success"
        except PermissionError:
            return "permission_error"
        

