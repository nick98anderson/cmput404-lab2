#!/usr/bin/env python3
from multiprocessing.dummy import Process
import socket
import time

#define address & buffer size
HOST = ""
PORT = 8002
BUFFER_SIZE = 1024


def handle_request(addr, conn):
    full_data = conn.recv(BUFFER_SIZE)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            p = Process(target=handle_request, args=(addr,conn))
            p.daemon = True
            p.start()

if __name__ == "__main__":
    main()
