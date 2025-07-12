from scapy.all import sniff

results = sniff(count=10)

file_path = r"C:\Users\15613\Desktop\PacketLogger.txt"

with open(file_path, "w") as f:
    for pkt in results:
        summary = pkt.summary()
        print(summary)
        f.write(summary + "\n")