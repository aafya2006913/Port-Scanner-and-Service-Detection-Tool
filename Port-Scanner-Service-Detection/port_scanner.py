import socket
from datetime import datetime

COMMON_SERVICES = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            service = COMMON_SERVICES.get(port, "Unknown Service")
            return True, service
        else:
            return False, None

    except:
        return False, None

def main():
    print("=" * 50)
    print("   PORT SCANNER & SERVICE DETECTION TOOL")
    print("=" * 50)

    target = input("Enter Target IP Address: ")

    try:
        start_port = int(input("Enter Start Port (Example: 1): "))
        end_port = int(input("Enter End Port (Example: 1000): "))
    except:
        print("Invalid port input!")
        return

    print("\nScanning Target:", target)
    print("Port Range:", start_port, "to", end_port)
    print("Scanning started...\n")

    start_time = datetime.now()

    open_ports = []

    for port in range(start_port, end_port + 1):
        status, service = scan_port(target, port)
        if status:
            print(f"[OPEN] Port {port}  |  Service: {service}")
            open_ports.append((port, service))

    end_time = datetime.now()

    print("\n" + "=" * 50)
    print("SCAN COMPLETED")
    print("=" * 50)

    if open_ports:
        print("\nOpen Ports Found:")
        for p, s in open_ports:
            print(f"Port {p}  -->  {s}")
    else:
        print("\nNo open ports found in this range.")

    print("\nScan Duration:", end_time - start_time)

if __name__ == "__main__":
    main()
