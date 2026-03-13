import socket
import threading
import argparse
import time

from colorama import Fore, Style, init
from src.utils import resolve_hostname, validate_ip, get_service, risk_level
from src.report_generator import ReportGenerator

init(autoreset=True)


class NetworkPortScanner:

    def __init__(self):
        self.open_ports = []
        self.lock = threading.Lock()

    def print_banner(self):
        """Display tool banner with credits"""
        banner = f"""
{Fore.CYAN}╔════════════════════════════════════════════════════════════╗
║                    {Fore.YELLOW}PortSleuth Pro v1.0{Fore.CYAN}                    ║
║                {Fore.GREEN}Advanced Network Port Scanner{Fore.CYAN}              ║
║                       {Fore.MAGENTA}By AJ{Fore.CYAN}                              ║
╚════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
        print(banner)

    def grab_banner(self, target, port):
        """Attempt to grab service banner"""
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((target, port))
            s.send(b"\r\n")
            banner = s.recv(1024).decode(errors="ignore").strip()
            s.close()
            return banner[:60]
        except:
            return ""

    def scan_port(self, target, port):
        """Scan a single port"""
        try:
            s = socket.socket()
            s.settimeout(1)

            if s.connect_ex((target, port)) == 0:
                service = get_service(port)
                banner = self.grab_banner(target, port)
                risk = risk_level(port)

                with self.lock:
                    self.open_ports.append({
                        "port": port,
                        "service": service,
                        "banner": banner,
                        "risk": risk
                    })

                    print(f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} {port} {service} ({risk})")

            s.close()

        except:
            pass

    def scan_range(self, target, start, end, threads=100):
        """Scan port range using multithreading"""
        start_time = time.time()
        jobs = []

        for port in range(start, end + 1):

            t = threading.Thread(target=self.scan_port, args=(target, port))
            jobs.append(t)
            t.start()

            if len(jobs) >= threads:
                for j in jobs:
                    j.join()
                jobs = []

        for j in jobs:
            j.join()

        duration = time.time() - start_time
        return self.open_ports, duration


def main():

    parser = argparse.ArgumentParser(description="PortSleuth Pro v1.0 - Advanced Network Port Scanner")

    parser.add_argument("target", help="Target domain or IP")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
    parser.add_argument("--report", choices=["txt", "json", "csv", "html"], help="Generate report")

    args = parser.parse_args()

    scanner = NetworkPortScanner()

    # Show Banner
    scanner.print_banner()

    ip = resolve_hostname(args.target)

    if not validate_ip(ip):
        print(f"{Fore.RED}Invalid target{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}Target:{Style.RESET_ALL} {args.target}")
    print(f"{Fore.CYAN}Resolved IP:{Style.RESET_ALL} {ip}")
    print(f"{Fore.CYAN}Port Range:{Style.RESET_ALL} {args.start}-{args.end}")
    print(f"{Fore.CYAN}Threads:{Style.RESET_ALL} {args.threads}")
    print()

    print(f"{Fore.YELLOW}Scanning {ip}...\n{Style.RESET_ALL}")

    data, duration = scanner.scan_range(ip, args.start, args.end, args.threads)

    print(f"\n{Fore.GREEN}Scan finished in {duration:.2f}s{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Open ports found:{Style.RESET_ALL} {len(data)}")

    if args.report:
        r = ReportGenerator(ip)
        method = getattr(r, args.report)
        path = method(data, duration)

        print(f"{Fore.CYAN}Report saved:{Style.RESET_ALL} {path}")


if __name__ == "__main__":
    main()