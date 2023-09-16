from socket import *
import time
import os
import threading

startTime = time.time()

def show_banner():
    os.system("clear")
    print('''
            __
    |)      /__
    |  0 RT  __/C 4NN3R
    ''')

def show_progress(progress_index, t_IP):
    index = (progress_index / 450) * 100
    if int(index) % 2 == 0:
        show_banner()
        print('Starting scan on host:', t_IP)
        print(f"\n\n==========================\nScanning: {100 - index:.1f}% left ")

def get_service(port):
    try:
        service = getservbyport(port, 'tcp')
        return service
    except OSError:
        return 'Unknown Service'

def scan_port(t_IP, port):
    s = socket(AF_INET, SOCK_STREAM)
    conn = s.connect_ex((t_IP, port))
    if conn == 0:
        service = get_service(port)
        port_open.append((port, service))
        print(f'Port {port}: OPEN ({service})')
    else:
        print(f'Port {port}: CLOSED')
    s.close()

if __name__ == '__main__':
    show_banner()
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    print('Starting scan on host:', t_IP)
    port_open = []
    threads = []

    for i in range(50, 500):
        thread = threading.Thread(target=scan_port, args=(t_IP, i))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    show_banner()
    print("Ports found open during scan: ")
    for port, service in port_open:
        print(f'Port {port}: {service}')
    print('Time taken:', time.time() - startTime)
