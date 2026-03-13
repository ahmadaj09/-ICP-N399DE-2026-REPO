
from src.core_scanner import NetworkPortScanner

scanner = NetworkPortScanner()
open_ports, duration = scanner.scan_range("scanme.nmap.org",1,100)
print(open_ports)
