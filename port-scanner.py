from socket import *
import time,os,math
startTime = time.time()

#### design
def show_banner():
   os.system("clear")
   print(f'''
                __
|)             /__
|  0 RT        __/C 4NN3R
''')

def show_progress(progress_index,t_IP):
    index = (progress_index/500)*100
    if (index%2)==0:
        show_banner()
        print ('Starting scan on host: ', t_IP)
        print(f"\n\n==========================\nScanning: {100-index}% left ")
    else:
      return 0

## config
port_open = []
# code
if __name__ == '__main__':
   show_banner()
   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)
   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         port_open.append(str(i))
         print ('Port %d: OPEN' % (i,))
      else:
         print(f"[PORT {i} FOUND INACTIVE ]")
      s.close()
      show_progress(i,t_IP)
show_banner()
print("Ports found open during scan: ")
for port in port_open:
   print(port_open(port))
print('Time taken:', time.time() - startTime)
