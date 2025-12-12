import socket
import sys

def scan_ports(target, ports):
    print(f"Sky Team – Port Scanner 🔍")
    print(f"Scanning {target}...\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            sock.close()
        except KeyboardInterrupt:
            print("Scan stopped by user.")
            sys.exit()
        except socket.error:
            print("Couldn't connect to server.")
            sys.exit()

if __name__ == "__main__":
    target_host = input("Enter target host (IP or domain): ")
    ports_to_scan = [21, 22, 23, 25, 53, 80, 443, 8080]  # common ports
    scan_ports(target_host, ports_to_scan)
