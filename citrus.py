
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


# import modules

import socket
import os
import argparse
import sys


def usage():
    global title
    title = print("""

    ▄████▄      |     
    ▒██▀ ▀█     | Welcome to Citrus
    ▒██    ▄    | Author: Zenqi
    ▒██▄ ▄██    | 
    ▒ ████▀     | https://github.com/zenqiwp/citrus
    ░ ░▒ ▒      |               
    ░  ▒                               
                                        
    
    Usage:

    <host>: Target host to perfom attack

    -p, --port: Target port, usually 80
    -m, -- mode: HTTP, Slowloris, TCP, UDP
    -t, --thread: Number of threads 

    Example: citrus 192.168.1.1 -p 80 -m <method> -t 500
    """)
    sys.exit()

def get_parameters():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("host", nargs="?")
    parser.add_argument(
        "-p", "--port", default=80, type=int
    )
    parser.add_argument("-m", "--mode")
    parser.add_argument("-t", "--thread", default=500, type=int)

    args = parser.parse_args()

    flood_mode = [

        "TCP",
        "UDP",
        "HTTP",
        "SLOWLORIS"
    ]

    global threads
    global port 
    global host
    global mode
    threads = args.thread
    port = args.port
    host = args.host
    mode = args.mode

    if not host:
        if sys.platform == "win32" or sys.platform == "win64":
            os.system('cls')
        elif sys.platform == "linux" or sys.platform == "linux2":
            os.system('clear')
        usage()

    if len(sys.argv) <= 1:
        if sys.platform == "win32" or sys.platform == "win64":
            os.system('cls')
        elif sys.platform == "linux" or sys.platform == "linux2":
            os.system('clear')
        usage()    

    if not mode:
        if sys.platform == "win32" or sys.platform == "win64":
            os.system('cls')
        elif sys.platform == "linux" or sys.platform == "linux2":
            os.system('clear')
        
        print("\nMode is not define")
        usage()
        

def main():
    
    if mode == "TCP" or mode == "TCP FLOOD" or mode == "tcp" or mode == "tcpflood":
        from method.tcpflood import TCP
        TCP(threads, host, port, mode)
        
    elif mode == "UDP" or mode == "UDP FLOOD"or mode == "udp" or mode == "ucpflood":
        from method.udpflood import UDP
        UDP(threads, host, port, mode)
    elif mode == "HTTP" or mode == "HTTP FLOOD"or mode == "http" or mode == "httpflood":
        from method.httpflood import HTTP
        HTTP(threads, host, port, mode)
    elif mode == "SLOWLORIS" or mode == "slowloris":
        from method.slowloris import SLOWLORIS
        flood = SLOWLORIS(threads, host, port, mode)
        
    else:
        if sys.platform == "win32" or sys.platform == "win64":
            os.system('cls')
        elif sys.platform == "linux" or sys.platform == "linux2":
            os.system('clear')
        print("\nMethod is not define")
        usage()

if __name__ == "__main__":
    get_parameters()
    main()
        