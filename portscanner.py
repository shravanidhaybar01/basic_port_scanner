import sys
import socket
import threading

if len(sys.argv) == 1:
    print(f'{sys.argv[0]} ip START END', file=sys.stderr)
    exit(1)

ip = sys.argv[1]
start=1
end=100

if len(sys.argv) >= 3:
    start = int(sys.argv[2])
if len(sys.argv) >= 4:
    end = int(sys.argv[3])

open_ports = []
lock = threading.Lock()

def check_port_status(port: int) -> bool:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        s.close()
        return True
    except (ConnectionRefusedError, socket.timeout, OSError):
        return False 
print(f"scanning {ip} from port {start} to {end}")    
for port in range(start, end):
    response = check_port_status(port)
    if response:
        print(f"open port : {port}")
    else:
        print(f"close port : {port}")
    input("press enter to exit...")







