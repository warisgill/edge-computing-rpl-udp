import sys
from socket import *
from socket import error
import time

BUFSIZE = 1024

class Gateway:
    
    def __init__(self, contiki_ipv6_ip="fd00::1",  contiki_ipv6_port = 5678, server_ip= None, server_port = None):
        super().__init__()
        self._port = contiki_ipv6_port # gateway port 
        self._contiki_ipv6_ip = contiki_ipv6_ip # gateway ip
        
        self._server_ip = server_ip # ip of cloud or edge server
        self._server_port = server_port # port of cloud or edge server

    
    def startGateway(self):
        with socket(AF_INET6, SOCK_DGRAM) as s: # ipv6 udp socket 
            s.bind((self._contiki_ipv6_ip, self._port))
            print("UDP Gateway-server ready: {p}".format(p=self._port))
            count = 0    
            while 1:
                t1 = time.time()
                data, addr = s.recvfrom(BUFSIZE)
                print ('server received {d}, from, {a}'.format(d=data, a=addr))
                count += 1
                # if count == 1:
                     
                print(">Gateway: # of Pakcets Received: {p}, Time in Seconds: {t}".format(p= count, t = '{0:.2f}'.format(time.time()-t1) ))

                # s.sendto(data, addr) # send packet to the mote

    def startGatewayWithEdegeServer(self):
        with socket(AF_INET6, SOCK_DGRAM) as s:
            s.bind((self._contiki_ipv6_ip, self._port))
            print(">UDP Gateway-server ready: {p}".format(p=self._port))
        
        # connecting gateway to the server 
        with socket(AF_INET, SOCK_STREAM) as client_sock:
            client_sock.connect((self._server_ip, self._server_port))
            count = 0
            t1 = time.time()
            while 1:
                data, addr = s.recvfrom(BUFSIZE)
                # print ('server received {d}, from, {a}'.format(d=data, a=addr))
                count += 1
                if count == 1:
                    t1 = time.time() 
                print(">Gateway: # of Pakcets Received: {p}, Time in Seconds: {t}".format(p= count, t = '{0:.2f}'.format(time.time()-t1)))

                # s.sendto(data, addr) # send packet to the mote
                client_sock.sendall(data) # send packet to the cloud


# #------------------------------------------------------------#
# # Prints the instructions
# #------------------------------------------------------------#
# def usage():
#     sys.stdout = sys.stderr
#     print ('Usage: udpecho -s [port] (server)')
#     print ("or: udpecho -c host [port] <file (client)")
#     sys.exit(2)

if __name__ == "__main__":

    g = Gateway(contiki_ipv6_ip="fd00::1",  contiki_ipv6_port = 5678)
    g.startGateway()

    
