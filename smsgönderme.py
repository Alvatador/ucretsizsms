#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s
import os
import time
from colorama import Fore, Back, Style





banner = print(Fore.YELLOW+"""
    ___    __            __            __          
   /   |  / /   ______ _/ /_____ _____/ /___  _____
  / /| | / / | / / __ `/ __/ __ `/ __  / __ \/ ___/
 / ___ |/ /| |/ / /_/ / /_/ /_/ / /_/ / /_/ / /    
/_/  |_/_/ |___/\__,_/\__/\__,_/\__,_/\____/_/     
                                                   

| Hergün 1 Tane Mesaj Atma Hakkınız Vardır (Vpnle İstediğiniz Kadar Atabilirsiniz)
| Mesajınız Karakter Sayısı Sınırlı Bunu Mesajınızı Yazdıktan Sonra Görüceksiniz.
| Telefon Numarasını Doğru Girmezseniz Hata Alabilirsiniz.

""")

print(banner)

sor = input("Tel adresi Örnek:+905404212233 >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:70]

print("\n| Mesajınızın Gönderilebilecek kısmı aşagıdaki gibidir.\n"+arlk)

drlm = input("\n| Mesajınız Gönderilsinmi?[Y/N] >>> ")

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
print("Bizi Tercih Ettiğiniz İçin Teşekkürler")
print("Bizi Tercih Ettiğiniz İçin Teşekkürler")
print("Bizi Tercih Ettiğiniz İçin Teşekkürler")
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
print("İletişim Adresleri")
banner = print(Fore.RED+"""
  ______   __                        __                      __                     
 /      \ /  |                      /  |                    /  |                    
/$$$$$$  |$$ | __     __  ______   _$$ |_     ______    ____$$ |  ______    ______  
$$ |__$$ |$$ |/  \   /  |/      \ / $$   |   /      \  /    $$ | /      \  /      \ 
$$    $$ |$$ |$$  \ /$$/ $$$$$$  |$$$$$$/    $$$$$$  |/$$$$$$$ |/$$$$$$  |/$$$$$$  |
$$$$$$$$ |$$ | $$  /$$/  /    $$ |  $$ | __  /    $$ |$$ |  $$ |$$ |  $$ |$$ |  $$/ 
$$ |  $$ |$$ |  $$ $$/  /$$$$$$$ |  $$ |/  |/$$$$$$$ |$$ \__$$ |$$ \__$$ |$$ |      
$$ |  $$ |$$ |   $$$/   $$    $$ |  $$  $$/ $$    $$ |$$    $$ |$$    $$/ $$ |      
$$/   $$/ $$/     $/     $$$$$$$/    $$$$/   $$$$$$$/  $$$$$$$/  $$$$$$/  $$/                                                                                      
""")
print(banner)
banner = print(Fore.GREEN+"""
Discord: ibriska#6788
""")




