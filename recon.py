import socket
import os
import requests
import platform
from os import sys
import urllib
import re
import time
import sys
import subprocess

def back():
    print()
    back = input('Do you want to continue? [Yes/No]: ')
    if back[0].upper() == 'Y':
        print()
        clear()
        dedsec()
        iseeverything()
    elif back[0].upper() == 'N':
        clear()
        dedsec()
        exit
    else:
        print('?')
        exit

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def dedsec():
    clear()
    print("""
██╗   ██╗ ██████╗ ██████╗ ██╗  ██╗
██║   ██║██╔═══██╗██╔══██╗██║ ██╔╝
██║   ██║██║   ██║██║  ██║█████╔╝ 
╚██╗ ██╔╝██║   ██║██║  ██║██╔═██╗ 
 ╚████╔╝ ╚██████╔╝██████╔╝██║  ██╗
  ╚═══╝   ╚═════╝ ╚═════╝ ╚═╝  ╚═╝
                                  """)
    print()

def banner():
    print("""
[1] DNS Lookup
[2] Whois Lookup
[3] GeoIP Lookup
[4] Port Scanner
[5] HTTP Header
[6] IP-Locator
[7] Host DNS Finder
[8] Extract Links
[9] Find Robots.txt
[10] Slow comprehensive scan
[11] Vuln Finder
[12] Intense Scan
[99] Exit """)
    print()

def iseeverything():
    try:
        what = input('Do you want to collect information of a website or IP address? [website/IP]: ')
        if what[0].upper() == 'W':
            victim = input('Enter the website address: ')
            banner()
        elif what[0].upper() == 'I':
            victim = input('Enter the IP address (or domain to get IP address of that domain): ')
            victim = socket.gethostbyname(victim)
            print('The IP address of target is:',victim)
            banner()
        else:
            print('?')
            iseeverything()

        choose = input('What information would you like to collect?: ')

        if choose == '1':
            dnslook = 'https://api.hackertarget.com/dnslookup/?q='+victim
            info = requests.get(dnslook)
            print(info.text)
            back()

        elif choose == '2':
            whois = 'https://api.hackertarget.com/whois/?q='+victim
            info = requests.get(whois)
            print(info.text)
            back()

        elif choose == '3':
            ipgeo = 'https://api.hackertarget.com/geoip/?q='+victim
            info = requests.get(ipgeo)
            print(info.text)
            back()

        elif choose == '4':
            port = 'https://api.hackertarget.com/nmap/?q='+victim
            info = requests.get(port)
            print(info.text)
            back()

        elif choose == '5':
            header = 'https://api.hackertarget.com/httpheaders/?q='+victim
            info = requests.get(header)
            print(info.text)
            back()

        elif choose == '6':
            host = 'https://api.hackertarget.com/hostsearch/?q='+victim
            info = requests.get(host)
            print(info.text)
            back()

        elif choose == '7':
            hostdns = 'https://api.hackertarget.com/mtr/?q='+victim
            info = requests.get(hostdns)
            print(info.text)
            back()

        elif choose == '8':
            pagelink = 'https://api.hackertarget.com/pagelinks/?q='+victim
            info = requests.get(pagelink)
            print(info.text)
            back()

        elif choose == '9':
            robots ='http://'+victim+'/robots.txt'
            info = requests.get(robots)
            print(info.text)
            back()

        elif choose == '10':
            subprocess.call('nmap -sS -sU -T3 -A -v -Pn -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)" '+victim)
            back()

        elif choose == '11':
            subprocess.call('nmap -sC -sS -Pn --script vuln '+victim)
            back()   
        
        elif choose == '12':
            subprocess.call('nmap -p 1-65535 -T4 -A -v -Pn '+victim)
            back()                 

        elif choose == '99':
            exit

        else:
            print('?')
            iseeverything()
            
    except socket.gaierror:
        print('Name or service unknown!')
        print()
        iseeverything()
    except UnboundLocalError:
        print('The information you entered is incorrect')
        print()
        iseeverything()
    except requests.exceptions.ConnectionError:
        print('Your Internet Offline')
        exit
    except IndexError:
        print('?')
        print()
        iseeverything()
    except KeyboardInterrupt:
        dedsec()
        print('\nAté Logo.\n')

dedsec()
iseeverything()