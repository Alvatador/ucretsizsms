#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s
import os
import time
from colorama import Fore, Back, Style


print("[ENG] Welcome To Free Sms Tool")
time.sleep(3)

os.system("clear")

print("[TR] Hoşgeldin Ücretsiz Sms Aracına ")
time.sleep(3)

os.system("clear")


banner = print(Fore.YELLOW+
"""
    ___    __            __            __          
   /   |  / /   ______ _/ /_____ _____/ /___  _____
  / /| | / / | / / __ `/ __/ __ `/ __  / __ \/ ___/
 / ___ |/ /| |/ / /_/ / /_/ /_/ / /_/ / /_/ / /    
/_/  |_/_/ |___/\__,_/\__/\__,_/\__,_/\____/_/     
                                                   
[TR] Hergün 1 Tane Mesaj Atma Hakkınız Vardır.
[ENG] You Have The Right To Send 1 Message a Day.
------------------------------------------------------------------------------------
[TR] Mesajınız Karakter Sayısı Sınırlı Bunu Mesajınızı Yazdıktan Sonra Görüceksiniz.
[ENG] Your Message is Limited Number of Characters You Will See This After You Write Your Message.
------------------------------------------------------------------------------------
[TR] Telefon Numarasını Doğru Girmezseniz Hata Alabilirsiniz.
[ENG] If You Don't Enter The Phone Number Correctly, You May Get An Error.
""")

print(banner)

sor = input("Telefon Numarası Örnek: +905404212233 >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:70]

print("\n| Mesajınızın Gönderilebilecek kısmı aşağıdaki gibidir.\n"+arlk)

drlm = input("\n| Mesajınız Gönderilsinmi? [Y/N] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|Hata!")
os.system("clear")
print("Bizi Tercih Ettiğiniz İçin Teşekkürler")
time.sleep(1)
print("Bizi Tercih Ettiğiniz İçin Teşekkürler")
time.sleep(1)
print("Bizi Tercih Ettiğiniz İçin Teşekkürler")
time.sleep(1)
os.system("clear")
print("          ___    __            __            __           ")
print("         /   |  / /   ______ _/ /_____ _____/ /___  _____ ")
print("        / /| | / / | / / __ `/ __/ __ `/ __  / __ \/ ___/ ")
print("       / ___ |/ /| |/ / /_/ / /_/ /_/ / /_/ / /_/ / /     ")
print("      /_/  |_/_/ |___/\__,_/\__/\__,_/\__,_/\____/_/      ")
time.sleep(1)
print(" ")
print("Alvatador Ücretsiz Sms Gönderme")
time.sleep(1)
os.system("clear")
print(" ")
banner = print(Fore.RED+"""

 █████╗ ██╗    ██╗   ██╗ █████╗ ████████╗ █████╗ ██████╗  ██████╗ ██████╗ 
██╔══██╗██║    ██║   ██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
███████║██║    ██║   ██║███████║   ██║   ███████║██║  ██║██║   ██║██████╔╝
██╔══██║██║    ╚██╗ ██╔╝██╔══██║   ██║   ██╔══██║██║  ██║██║   ██║██╔══██╗
██║  ██║███████╗╚████╔╝ ██║  ██║   ██║   ██║  ██║██████╔╝╚██████╔╝██║  ██║
╚═╝  ╚═╝╚══════╝ ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                                             
""")
time.sleep(1)
os.system("clear")
print(banner)
print("İletişim Adresleri")
banner = print(Fore.GREEN+"""
Discord: Alvatador#1000
İnstagram: boranpxrd
""")
