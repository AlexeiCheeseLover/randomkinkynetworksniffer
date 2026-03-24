#!/usr/bin/python

import subprocess
import socket

try:
    stuff = [80,443,22,21,25,23,53,110,143,445,139,3306,3389,389,161,5060,554,5900,2049,1900,7777]
    
    with open('afile', 'r') as ball:
        hi_lol = ball.read()
        hi = hi_lol.split('\n')
        hosts = [h for h in hi if h]
        for host in hosts:  
            print(host)
            for port in stuff:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                isopen = s.connect_ex((host, port))
                socket.setdefaulttimeout(1)
                if(isopen == 0):
                    print(port)
                    s.close()

    #| tr -d '\\' | tr -d 'n'
    
except KeyboardInterrupt:
    exit()
#top 20
#HTTP (80) – World Wide Web
#HTTPS (443) – Secure HTTP (SSL/TLS)
#SSH (22) – Secure Shell
#FTP (21) – File Transfer Protocol
#SMTP (25) – Simple Mail Transfer Protocol
#Telnet (23) – Remote terminal protocol
#DNS (53) – Domain Name System
#POP3 (110) – Post Office Protocol v3
#IMAP (143) – Internet Message Access Protocol
#SMB (445) – Server Message Block (file sharing)
#NetBIOS (139) – NetBIOS Session Service
#MySQL (3306) – Database service
#RDP (3389) – Remote Desktop Protocol
#LDAP (389) – Lightweight Directory Access Protocol
#SNMP (161) – Simple Network Management Protocol
#SIP (5060) – Session Initiation Protocol
#RTSP (554) – Real-Time Streaming Protocol
#VNC (5900) – Virtual Network Computing
#NFS (2049) – Network File System
#UPnP (1900) – Universal Plug and Play 

