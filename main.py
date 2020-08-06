import time
import shutil
import os
from Screenshot import Screenshot_Clipping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# This is a sample Python script.
# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def run_selenium_server(driver):
    driver.get("http://www.python.org")

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Access each dimension individually
    position = driver.get_window_position()
    msg_pos = 'Window position: ' + str(position)
    print(msg_pos)
    x = position.get('x')
    y = position.get('y')

    # Or store the dimensions and query them later
    size = driver.get_window_size()
    width = size.get("width")
    height = size.get("height")
    print('Window size: ' + str(size))
    print('Width: ' + str(width))
    print('Height: ' + str(height))

    driver.set_window_size(1024, 768)

    size = driver.get_window_size()
    width = size.get("width")
    height = size.get("height")

    print('Window size: ' + str(size))
    print('Width: ' + str(width))
    print('Height: ' + str(height))

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    assert "Python" in driver.title
    print("Page: " + driver.title)
    elem = driver.find_element_by_name("q")
    elem.send_keys("selenium")
    elem.send_keys(Keys.RETURN)

    record = driver.find_element_by_xpath('//*[@id="content"]/div/section/form/ul/li[1]/h3/a')
    record.click()

    record2 = driver.find_element_by_xpath('//*[@id="content"]/div/section/article/div[2]/p[2]/span[2]/a')
    record2.click()

    record3 = driver.find_element_by_xpath('//*[@id="top"]/nav/ul/li[3]/a')
    record3.click()

    driver.get("http://www.google.com")
    print("Page: " + driver.title)
    text_search = driver.find_element_by_name("q")
    text_search.send_keys("edit forms")
    text_search.send_keys(Keys.RETURN)
    rec_search = driver.find_element_by_xpath('//*[@id="rso"]/div[9]/div/div[1]/a/h3')
    rec_search.click()
    print("Page: " + driver.title)

    # Open URL
    driver.get("https://seleniumhq.github.io")
    print("Page: " + driver.title)

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # open new blank tab
    driver.execute_script("window.open();")

    # Opens a new tab and switches to new tab
    driver.switch_to.window(driver.window_handles[1])

    driver.get("http://www.msn.it")
    print("Page: " + driver.title)
    driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]/ul/li[7]/a').click()
    time.sleep(5)
    driver.back()
    time.sleep(5)
    driver.forward()
    time.sleep(5)

    driver.get('https://www.almaviva.it/it_IT/Societa-del-gruppo/AlmavivA_Digitaltec')
    print("Page: " + driver.title)
    ob = Screenshot_Clipping.Screenshot()
    element = driver.find_element_by_xpath('/html/body/div/div[8]/a/span')
    if element.is_displayed() == True:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[8]/a/span"))).click()

    elem = driver.find_element_by_xpath('/html/body/div/div[5]/div[1]/picture/img')

    if os.path.isdir('./images') == False:
        os.mkdir('images')
        img_url = ob.get_element(driver,elem,'images')
        #print(img_url)
        os.chdir('images')
        os.remove('clipping_shot.png')
        head_tail = os.path.split(img_url)
        os.rename(head_tail[1],'palace.png')
        print(head_tail[0] + '\\palace.png')
    else:
        shutil.rmtree('images',ignore_errors=True)
        os.mkdir('images')
        img_url = ob.get_element(driver,elem,'images')
        #print(img_url)
        os.chdir('images')
        os.remove('clipping_shot.png')
        head_tail = os.path.split(img_url)
        img = 'palace.png'
        os.rename(head_tail[1],img)
        print(head_tail[0]+'\\'+ img )

# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == '__main__':
    print_hi('Selenium Tester')
    #https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver
    #driver = webdriver.Chrome(r"C:\Users\M.Sabetta\.wdm\drivers\chromedriver\win32\84.0.4147.30/chromedriver.exe")
    opt = Options()
    opt.page_load_strategy = 'normal'
    opt.add_argument('--ignore-certificate-errors')
    opt.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(r"./chromedriver/chromedriver.exe",options=opt)
    run_selenium_server(driver)
    time.sleep(5)
    driver.close()
    driver.quit()