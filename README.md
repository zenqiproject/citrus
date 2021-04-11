

# Citrus
> moved to -> zenqiproject/citrus

A multi-tool for flooding http, udp, tcp and more. Under development might add another features.

## Usage
```
 ▄████▄     
▒██▀ ▀█      |Welcome to Citrus
▒██    ▄      
▒██▄ ▄██     
▒ ████▀      |https://github.com/zenqiwp/citrus
░ ░▒ ▒      
░  ▒


Usage:

<host>: Target host to perfom attack

-p, --port: Target port, usually 80
-m, -- mode: HTTP, Slowloris, TCP, UDP
-t, --thread: Number of threads

Example: citrus 192.168.1.1 -p 80 -m <method> -t 500
```
```
py citrus.py <host> -p 80 -t 100 -m TCP
```
