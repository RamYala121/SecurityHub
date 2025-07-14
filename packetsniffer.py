from scapy.all import sniff  # type: ignore

def sniff_packets():
    results = sniff(count=10)

    file_path = "/Users/derekyin/Desktop/PacketLogger.txt"

    summaries = []
    for pkt in results:
        summary = pkt.summary()
        summaries.append(summary)

    return summaries
