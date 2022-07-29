from selenium import webdriver
from os import system, name
import chromedriver_binary
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title TIKTOK BOT')

print(pyfiglet.figlet_format("TIKTIK BOT", font="slant"))
print("WEBSITE : https://channel-monifire-website.netlify.app\nGITHUB : https://github.com/MONIFIRE\nFACEBOOK : https://www.facebook.com/toey.monifire")

auto = input("\nคุณต้องการเพิ่มยอดวิวหรือไม่ y/n ? : ")

if auto == 'Y' or auto == 'y':
    vidUrl = input("\n\nกรุณาใสลิ้งวิดีโอของคุณ : ")
    clear()

    start = time()
    time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome( options=chrome_options)
    driver.set_window_size(1024, 650)

    Views = 0

def beautify(arg):
    return format(arg, ',d').replace(',', '.')

def title1(): # Update the title IF option 1 was picked.
    global Views
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title TIKTOK BOT ^| Views Sent: {beautify(Views)} ^| Elapsed Time: {time_elapsed}')

    
def loop1():
    global Views
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
        
    except:
        print("[x] เกิดข้อผิดพลาด")
        driver.refresh()
        loop1()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        
        driver.refresh()
        Views += 1000
        print("\n[/] ได้ส่งยอดวิวให้คุณเรียบร้อย !")
        
        sleep(300)
        loop1()
        
    except:
        print("\n[x] ทำงานล้มเหลวเกิดข้อผิดพลาด !") 
        driver.refresh()
        loop1()





if auto == 'Y' or auto == 'y':
    print(pyfiglet.figlet_format("TIKTOK BOT", font="slant"))
    print("\nกำลังทำงาน ! ( กรุณาใสรหัสยืนยัน / ห้ามทำอะไรบอทจะทำงานอัตโนมัต )")

    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title1)
    b = threading.Thread(target=loop1)
    
    a.start()
    b.start()
    
else:
    print(f"\n[ {auto} ] เกิดข้อผิดพลาดกรุณาใสให้ถูกต้อง !")
