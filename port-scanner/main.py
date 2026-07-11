import socket
ip = input("enter ipadress ")
port = int(input("port "))
s=socket.socket()

s.settimeout(3)
try:
    s.connect((ip,port))
    print("port is open ")

except TimeoutError:
        print("TIme out")
except ConnectionRefusedError:
      print("port is closedd")
s.close() 