#!/usr/bin/python3

import nmap

class scanner:

    def __init__(self):
        
        self.ip=""
        self.ports = 0
        self.scan_type="0"

    def get_ip(self):

        ip= input("Enter the IP address that you want to scan: ")
        self.ip=ip
        print (f"ip address set to {ip}")
        print("----------------------------")


    def get_scan_type(self):
        opt = input("""\nWhat type of scan would you like to run:
                        1) TCP scan
                        2) UDP scan
                        3) Agressive scan\n""")
        self.scan_type = opt

    
    def scan(self):
        scanner = nmap.PortScanner()
        arg = ''
        protocol ='tcp'
        open_ports=''

        if self.scan_type=="2":
            arg=' -sU'
            protocol = 'udp'

        print(f"starting {protocol} scan..")
        scanner.scan(self.ip,'-','-T4'+arg)
        print(f"Host {self.ip} is {scanner[self.ip].state()}")
        try:
            open_ports = str((list(scanner[self.ip]['tcp'].keys()))).strip('[]')
            print(f"Open Ports: {open_ports}")
            
            if self.scan_type=="3":
                arg ='-A'
                print("starting aggressive scan... be patient")
                scanner.scan(self.ip,open_ports,f'-T4 {arg}')
                print(scanner[self.ip][protocol])

           
        except(KeyError):
            print("currently no open ports")
        
        




    def start(self):
        self.get_ip()
        self.get_scan_type()
        self.scan()

test = scanner()
test.start()