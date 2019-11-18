import sys
import socket
import time

class Server:
    def __init__(self, ip = None, port = None):
        super().__init__()
        self._ip = ip
        self._port = port

        if ip is None:
            raise Exception("Please enter correct ip and port of the server.")
    
    # initiate a TCP connection
    def serverTCP(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            count = 0
            t1 = time.time()

            s.bind((self._ip,self._port))
            s.listen()
            
            print(">Gateway/Cloud: IP ", s)
            conn, addr = s.accept()

            with conn:
                print(">Client Connected with IP", addr)
                while True:
                    data = conn.recv(1024)
                    count += 1
                    if count == 1:
                        t1 = time.time() 
                    print(">Cloud/Cloudlet: # of Pakcets Received: {p}, Time in Seconds: {t}".format(p= count, t = '{0:.2f}'.format(time.time()-t1)))
                    # if client disconnect break the connection
                    if not data:
                        break
                print(">Client Disconnected ", addr)


if __name__ == "__main__":
    port = 8080
    ip = ""

    s = Server(ip = ip, port = port)
    s.serverTCP()

    


