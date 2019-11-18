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
    

    def serverTCP(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self._ip,self._port))
            s.listen()
            
            count = 0
            t1 = time.time()

            print(s)
            conn, addr = s.accept()

            with conn:
                print(">Client Connect by", addr)
                while True:
                    data = conn.recv(1024)
                    count += 1
                    if count == 1:
                        t1 = time.time() 
                    print(">Cloud/Cloudlet: Pakcets Received: {p}, Time in Seconds: {t}".format(p= count, t = '{0:.2f}'.format(time.time()-t1) ))
                    # print(data)
                    if not data:
                        break
                    # conn.sendall(data)
                print(">Client Disconnected ", addr)


# def clientTCP(host, port):
#     HOST = host  # The server's hostname or IP address
#     PORT = port  # The port used by the server

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((HOST, PORT))
#         count = 1
#         while True:
#             s.sendall(b'Hello, world')
#             data = s.recv(1024)
#             count += 1
#             print(data,count)

#     print('Received', repr(data))




#------------------------------------------------------------#
# Prints the instructions
#------------------------------------------------------------#
def usage():
    sys.stdout = sys.stderr
    print ('Usage: -s server')
    print ("or: udpecho -c host [port] <file (client)")
    sys.exit(2)


if __name__ == "__main__":
    port = 8080
    ip = ""

    s = Server(ip = ip, port = port)
    s.serverTCP()

    


