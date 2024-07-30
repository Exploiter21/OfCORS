#!/bin/env python3
import requests
import ssl
from urllib.parse import urlparse, urlunparse
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
CYAN   = "\033[36m"
RESET  = "\033[0m"

BRED     = "\033[41m"
BGREEN   = "\033[42m"
BYELLOW  = "\033[43m"
BBLUE    = "\033[44m"
BMAGENTA = "\033[45m"
BCYAN    = "\033[46m"

'''
print("\033[31mThis is red text\033[0m")
print("\033[32mThis is green text\033[0m")
print("\033[33mThis is yellow text\033[0m")
print("\033[34mThis is blue text\033[0m")
'''

class cors():
    def __init__(self):
        pass

    def rectifier(self, domain):
        if domain.startswith("https://") or domain.startswith("http://"):
            return domain
        else:
            return urlunparse(("", "", domain, "", "", ""))

    def strike(self, headers, url):
        try:
            response = requests.get(url, headers=headers, allow_redirects=True, verify=False)
            acao = response.headers.get("Access-Control-Allow-Origin") 
            acac = response.headers.get("Access-Control-Allow-Credentials")
            return acao, acac
        
        except Exception as error:
            print(f"Strik Function Error : {error}")
            return False


    def scan(self, domain):
        url = self.rectifier(domain)
        header = {"Origin":"https://evil.com", "Access-Control-Request-Method":"GET"}
        try:
            response = requests.options(url, headers=header, allow_redirects=True, verify=False)
        

            if "Access-Control-Allow-Origin" in response.headers:
            
                #check-1
                header = {"Origin":"evil.com"}
                acao, acac = self.strike(header, url)
           
                if "evil.com" == acao and acac == 'true':
                    print(f"{BRED}Dynamic Origin  Domain: {url}, Origin : {acao}, Credentials : {acac}{RESET}")
                
                elif "evil.com" == acao and acac == 'false':
                    print(f"{BRED}Dynamic Origin  Domain: {url}, Origin : {acao}, Credentials : {acac}{RESET}")
                
                elif "evil.com" == acao and not acac:
                    print(f"{BRED}Dynamic Origin  Domain: {url}, Origin : {acao}, Credentials : {acac}{RESET}")
                

                #check-2
                header = {"Origin":"evil.com.{url}"}
                acao, acac = self.strike(header, url)
           
                if f"evil.com.{url}" == acao and acac=='true':
                    print(f"{BYELLOW}Dynamic Subdimain  Domain: {url}, Origin : {acao}, Credentials : {acac}{RESET}")
                elif f"evil.com.{url}" == acao and acac=='false':
                    print(f"{BBLUE}Dynamic Subdimain  Domain: {url}, Origin : {acao}, Credentials : {acac}{RESET}")
                elif f"evil.com.{url}" == acao and not acac:
                    print(f"{CYAN}Dynamic Subdimain  Domain: {url}, Origin : {acao}, Credentials : {acac}{RESET}")
                
                #check-3
                header = {"Origin":"evil{url}"}
                acao, acac = self.strike(header, url)
            
                if f"evil{url}" == "acao" and acac=='true':
                    print(f"{BRED}Dynamically Domain  Domain: {url}, Origin : {acao}, Credentials : {acac}{RESET}")
                
                elif f"evil{url}" == "acao" and acac=='false':
                    print(f"{BYELLOW}Dynamically Domain  Domain: {url}, Origin : {acao}, Credentials : {acac}{RESET}")
                
                elif f"evil{url}" == "acao" and not acac:
                    print(f"{BYELLOW}Dynamically Domain  Domain: {url}, Origin : {acao}, Credentials : {acac}{RESET}")
                
                #check-4
                header = {"Origin":"evil.com"}
                acao, acac = self.strike(header, url)
            
                if acao == "*":
                    print(f"{BGREEN}Wild Card  * Domain  Domain: {url}, Origin : {acao}, Credentials : {acac}{RESET}")
        
                #check-5
                header = {"Origin":url}
                acao, acac = self.strike(header, url)

                if acao == url and acac == 'true':
                    print(f"{BGREEN}Same Domain  Domain: {url}, Origin : {acao}, Credentials : {acac}{RESET}")
                elif acao == url and acac == 'false':
                    print(f"{BGREEN}Same Domain  Domain: {url}, Origin : {acao}, Credentials : {acac}{RESET}")
                elif acao == url and not acac:
                    print(f"Same Domain Domain  Domain: {url}, Origin : {acao}, Credentials : {acac}")
        
        except Exception as error:
            pass
            #print(error)
            
            