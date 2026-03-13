
import socket

COMMON_PORTS = {
21:"ftp",
22:"ssh",
23:"telnet",
25:"smtp",
53:"dns",
80:"http",
110:"pop3",
143:"imap",
443:"https",
3306:"mysql",
3389:"rdp"
}

def resolve_hostname(host):
    return socket.gethostbyname(host)

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except:
        return False

def get_service(port):
    return COMMON_PORTS.get(port,"unknown")

def risk_level(port):
    if port in [21,23,445,3389]:
        return "HIGH"
    if port in [22,80,443]:
        return "MEDIUM"
    return "LOW"
