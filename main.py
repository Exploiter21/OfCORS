#!/bin/env python3
from engine import *
import argparse
import os

def banner():
    banner = f"""{GREEN}
 ░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
                                                                               
    Created with <3 by SARTHAK JOSHI                                                                                                                                                                                                                                                 
    {RESET}"""
    print(banner)

def main():
    parser = argparse.ArgumentParser(description='A CORS misconfiguration finder')
    parser.add_argument('--domain', '-d', type=str,help='Traget Domain')
    parser.add_argument('--dfile', '-df', type=str, help='File containing domains to test')
    arg = parser.parse_args()
    
    domain = arg.domain
    domainFile = arg.dfile
   
    if domain and domainFile:
        parser.error("Only domain or domain file is accepeted at once")
    
    banner()
    if domain:
        cors_object = cors()
        cors_object.scan(domain)

    if domainFile:
        if os.path.isfile(domainFile):
            try:
                with open(domainFile, 'r') as domains:
                    for domain in domains.readlines():
                        scanfile = cors()
                        scanfile.scan(''.join(domain.strip()))
            except Exception as error:
               print(f"Hit Exception {error}")
        
        else:
            print(f"Error while reading {domainFile}")
        


if __name__=='__main__':
    main()