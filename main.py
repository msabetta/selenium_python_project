import time
import shutil
import os
from utils import *
from Screenshot import Screenshot_Clipping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import traceback


# This is a sample Python script.
# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def somma_interi_infinita():
    while True:
        a = input('Inserire primo numero: ')
        b = input('Inserire secondo numero: ')
        res = int(a) + int(b)
        print('Risultato: ', res)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def run_selenium_server(driver):
    driver.get("http://www.python.org")

    # Store the ID of the original window
    original_window = driver.current_window_handle

    check_window_size(driver)

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
    time.sleep(5)
    driver.find_element_by_id("onetrust-accept-btn-handler").click()
    time.sleep(5)
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
        print(head_tail[0]+'\\'+ img)

        #login_into_facebook(driver,"mariorossi@gmail.com", "AlfaRomeo")


def check_window_size(driver):
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
    driver.maximize_window()


def login_into_facebook(driver, user_name_value, pass_value):
    driver.get("https://www.facebook.com")
    print("Page: " + driver.title)
    time.sleep(1)
    username = driver.find_element_by_id("email")
    time.sleep(1)
    password = driver.find_element_by_id("pass")
    time.sleep(1)
    submit = driver.find_element_by_name("login")
    time.sleep(1)

    username.send_keys(user_name_value)
    time.sleep(2)
    password.send_keys(pass_value)
    time.sleep(2)
    submit.click()
    time.sleep(2)

    wait = WebDriverWait(driver, 5)
    page_title = driver.title

    assert page_title == "Facebook"


def login_into_facebook_second(user_name_value,pass_value):
    get_page("https://www.facebook.com")
    get_page_title()
    sleep(1)
    username = find_element_by_id("email")
    sleep(1)
    password = find_element_by_id("pass")
    sleep(1)
    submit = find_element_by_name("login")
    sleep(1)
    username.send_keys(user_name_value)
    sleep(2)
    password.send_keys(pass_value)
    sleep(2)
    submit.click()
    sleep(2)
    wait = wait_web_driver(5)
    assert get_page_title_var() == "Facebook"


def run_selenium_server_second():
    try:
        get_page("http://www.python.org")

        # Store the ID of the original window
        original_window = get_current_window_handle()

        get_window_size()

        # Check we don't have other windows open already
        assert len(get_window_handles()) == 1

        #assert "Python" in driver.title
        assert "Python" in get_page_title_var()

        get_page_title()

        fill_field_by_name("q", "selenium")

        sleep(5)

        # click_link_by_xpath('//*[@id="content"]/div/section/form/ul/li[1]/h3/a')
        #
        # click_link_by_xpath('//*[@id="content"]/div/section/article/div[2]/p[2]/span[2]/a')
        #
        # click_link_by_xpath('//*[@id="top"]/nav/ul/li[3]/a')

        get_page("http://www.google.com")

        get_page_title()

        sleep(5)

        fill_field_by_name_and_return("q", "edit forms")

        #click_link_by_xpath('//*[@id="rso"]/div[9]/div/div[1]/a/h3')

        # Open URL
        get_page("https://seleniumhq.github.io")

        get_page_title()

        # Loop through until we find a new window handle
        switch_window_handle()

        # open new blank tab
        execute_script_string("window.open();")


        # Opens a new tab and switches to new tab
        switch_to_window(1)

        get_page("http://www.msn.it")

        get_page_title()

        sleep(5)

        click_button_by_id("onetrust-accept-btn-handler")

        sleep(5)

        click_link_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]/ul/li[7]/a')

        sleep(5)

        backward_page()

        sleep(5)

        forward_page()

        sleep(5)

        get_page('https://www.almaviva.it/it_IT/Societa-del-gruppo/AlmavivA_Digitaltec')

        get_page_title()

        get_screenshot_img()

        element = find_element_by_xpath('/html/body/div/div[8]/a/span')

        wait_elem_to_be_clickable(element, "/html/body/div/div[8]/a/span", 20)

        elem = find_element_by_xpath('/html/body/div/div[5]/div[1]/picture/img')

        if is_directory('./images') is False:
            create_dir('images')
            img_url = get_img_url(elem, 'images')
            change_working_dir('images')
            remove_file('clipping_shot.png')
            head_tail = split_file_url(img_url)
            rename_file(head_tail[1], 'palace.png')
            console_log(head_tail[0] + '\\palace.png')
        else:
            delete_directory_tree('images')
            create_dir('images')
            img_url = get_img_url(elem, 'images')
            change_working_dir('images')
            remove_file('clipping_shot.png')
            head_tail = split_file_url(img_url)
            img = 'palace.png'
            rename_file(head_tail[1], img)
            console_log(head_tail[0] + '\\' + img)

        #login_into_facebook(driver,"mariorossi@gmail.com", "AlfaRomeo")
        #login_into_facebook_second(driver,"mariorossi@gmail.com", "AlfaRomeo")

    except:
        traceback.print_exception()
        tear_down()
        quit_sessions()



# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == '__main__':
    print_hi('Selenium Tester')

    #https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver
    #driver = webdriver.Chrome(r"C:\Users\M.Sabetta\.wdm\drivers\chromedriver\win32\84.0.4147.30/chromedriver.exe")
    # opt = webdriver.ChromeOptions()
    # opt.page_load_strategy = 'normal'
    # opt.add_argument('--ignore-certificate-errors')
    # opt.add_argument('--ignore-ssl-errors')
    # driver = webdriver.Chrome(r"./chromedriver/chromedriver.exe", options=opt)

    setup()

    #run_selenium_server(driver)

    run_selenium_server_second()

    #time.sleep(5)
    sleep(5)

    #driver.close()
    #driver.quit()

    tear_down()
    quit_sessions()

