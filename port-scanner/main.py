from concurrent.futures import ThreadPoolExecutor
import time
import threading
import socket
ip = input("enter ipadress ")
port_start = int(input("enter start "))
port_end = int(input("enter end "))

a=0
b=0
c=0
lock = threading.Lock()

def scanner(port):
    global a, b, c
    s=socket.socket()
    
    s.settimeout(3) 
    try:
        s.connect((ip,port))
        print(f"[+] Port {port} OPEN")
        with lock:
            a+=1
    except TimeoutError:
        with lock:
            b+=1
    except ConnectionRefusedError:

        with lock:
            c+=1
    except OSError as e:
        print(e)
    
        
    s.close()
def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        ports = list(range(port_start,port_end+1))
        print(f"Scanning...")
        executor.map(scanner,ports)
    print(f"Ports scanned:  {port_end-port_start}\n" f"ports closed  {c}\n"f"ports did not respond {b}\n" f"ports open {a}") 
        


if __name__=="__main__":
    main()
   
        
