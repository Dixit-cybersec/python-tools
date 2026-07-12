import socket
ip = input("enter ipadress ")
port = int(input("enter start "))
porto = int(input("enter end "))

while(port<=porto):
    s=socket.socket()

    s.settimeout(3)
    try:
        s.connect((ip,port))
        print(f"[+] Port {port} OPEN")

    except TimeoutError:
        print(f"[+] Port {port} TIMEOUT")
    except ConnectionRefusedError:
        print(f"[+] Port {port} CLOSE")
    except OSError as e:
        print(e)
    port=port+1
    s.close() 
