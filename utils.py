import os
import time
import shutil
import chromedriver_autoinstaller
from pathlib import Path
from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Screenshot import Screenshot_Clipping

def setup():
    global driver
    global action
    chromedriver_filepath = chromedriver_autoinstaller.install()
    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = {'browser': 'ALL'}
    opt = webdriver.ChromeOptions()
    opt.page_load_strategy = 'normal'
    opt.add_argument('--ignore-certificate-errors')
    opt.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chromedriver_filepath, desired_capabilities=d, options=opt)
    action = ActionChains(driver)
    driver.delete_all_cookies()
    set_window_size(1024, 768)
    refresh_browser()


def maximize_window():
    driver.maximize_window()


def refresh_browser():
    driver.refresh()


def get_page_title():
    console_log('Page title: ' + str(driver.title))


def get_page_title_var():
    return driver.title


def get_page(page):
    driver.get(page)
    #get_page_title()


def get_window_position():
    console_log('Window current position: ' + str(driver.get_window_position()))


def get_window_size():
    console_log('Current window size: ' + str(driver.get_window_size()))


def set_window_size(width, height):
    driver.set_window_size(width, height)
    console_log('Window size set: ' + str(driver.get_window_size()))


def console_log(function):
    print(get_timestamp_usa(), '--- LOG --- ', function)


def console_log_browser(function):
    print(get_timestamp_usa(), '--- LOG BROWSER --- ', function)


def console_error(function):
    print(get_timestamp_usa(), '--- ERROR --- ', function)


def console_debug(function):
    print(get_timestamp_usa(), '--- DEBUG --- ', function)


def print_cookies():
    cookies = driver.get_cookies()
    for cookie in cookies:
        console_log(cookie)


def manage_iframe(css_selector_frame, css_selector_agree_button):
    # iframe management
    wait = WebDriverWait(driver, 5)
    iframe = wait.until(ec.element_to_be_clickable([By.CSS_SELECTOR, css_selector_frame]))
    if iframe is not None:
        driver.switch_to.frame(iframe)
        driver.find_element_by_css_selector(css_selector_agree_button).click()


def click_button_by_id(id_button):
    # get button by id
    button = driver.find_element_by_id(id_button)
    # click the item
    action.click(on_element=button)
    # perform the operation
    action.perform()


def click_button_by_link_text(link_text):
    # get button by id
    link = driver.find_element_by_link_text(link_text)
    # click the item
    action.click(on_element=link)
    # perform the operation
    action.perform()


def click_button_by_css_selector(css_selector):
    # get button by id
    button = driver.find_element_by_css_selector(css_selector)
    # click the item
    action.click(on_element=button)
    # perform the operation
    action.perform()


def click_button_by_css_selector_simple(css_selector):
    # get button by id
    button = driver.find_element_by_css_selector(css_selector)
    # click action
    button.click()


def fill_field_by_name_and_return(name_field, input_value):
    search = driver.find_element_by_name(name_field)
    search.send_keys(input_value)
    search.send_keys(Keys.RETURN)


def fill_field_by_name(name_field, input_value):
    search = driver.find_element_by_name(name_field)
    search.send_keys(input_value)


def fill_field_by_id_and_return(id_field, input_value):
    search = driver.find_element_by_id(id_field)
    search.send_keys(input_value)
    search.send_keys(Keys.RETURN)


def fill_field_by_id(id_field, input_value):
    search = driver.find_element_by_id(id_field)
    search.send_keys(input_value)


def fill_field_by_class(class_name, input_value):
    search = driver.find_elements_by_class_name(class_name)
    search.send_keys(input_value)


def click_link_by_css_selector(css_selector):
    link = driver.find_element_by_css_selector(css_selector)
    link.click()


def click_link_by_xpath(xpath):
    link = driver.find_element_by_xpath(xpath)
    link.click()


def click_link_by_class_name(class_name):
    link = driver.find_element_by_class_name(class_name)
    link.click()


def sleep(time_sec):
    time.sleep(time_sec)


def tear_down():
    driver.close()


def quit_sessions():
    driver.quit()


def search_word_from_google(word):
    get_page("http://www.google.com")
    #manage_iframe('#cnsw > iframe', '#introAgreeButton > span > span')
    window = find_element_by_css_selector('#Sx9Kwc > div.jw8mI > span > div > div')
    if window.is_displayed():
        find_element_by_css_selector('#zV9nZe > div').click()
    fill_field_by_name_and_return('q', word)
    get_page_title()


def print_window_handles():
    handles = driver.window_handles
    size = len(handles)
    i = 1
    for x in range(size):
        driver.switch_to.window(handles[x])
        """console_log(driver.title)"""
        console_log('Window handle ' + str(i) + ' : ' + driver.title)
        i = i + 1


def switch_window_and_close_parent():
    curr_handle = driver.current_window_handle
    console_log('Current handle: ' + curr_handle.title())
    handles = driver.window_handles
    curr_title = driver.title
    i = 1
    for handle in handles:
        driver.switch_to.window(handle)
        console_log('Window handle ' + str(i) + ' : ' + driver.title)
        i = i + 1
        if driver.title == curr_title:
            console_log('Closed parent handle: ' + driver.title)
            driver.close()


def open_link_in_new_tab(link):
    action.key_down(Keys.CONTROL)
    action.click_and_hold(on_element=link)
    action.release(on_element=link)
    action.key_up(Keys.CONTROL)
    action.perform()


def insert_word_to_search():
    word = input("Inserisci parola da cercare: ")
    search_word_from_google(word)


def search_element(element, click=True, type="name"):
    if element is not None:
        if type == "name":
            if click is True:
                driver.find_element_by_name(element).click()
            else:
                return driver.find_element_by_name(element)
        elif type == "id":
            if click is True:
                driver.find_element_by_id(element).click()
            else:
                return driver.find_element_by_id(element)
        elif type == "xpath":
            if click is True:
                driver.find_element_by_xpath(element).click()
            else:
                return driver.find_element_by_xpath(element)
        elif type == "link_text":
            if click is True:
                driver.find_element_by_link_text(element).click()
            else:
                return driver.find_element_by_link_text(element)
        elif type == "partial_link_text":
            if click is True:
                driver.find_element_by_partial_link_text(element).click()
            else:
                return driver.find_element_by_partial_link_text(element)
        elif type == "tag_name":
            if click is True:
                driver.find_element_by_tag_name(element).click()
            else:
                return driver.find_element_by_tag_name(element)
        elif type == "class_name":
            if click is True:
                driver.find_element_by_class_name(element).click()
            else:
                return driver.find_element_by_class_name(element)
        elif type == "css_selector":
            if click is True:
                driver.find_element_by_css_selector(element).click()
            else:
                return driver.find_element_by_css_selector(element)
    else:
        console_error('Object not found')


def select_value_from_drop_menu_by_id(id_item, option_value):
    x = driver.find_element_by_id(id_item)
    drop = Select(x)
    drop.select_by_value(option_value)


def select_value_from_drop_menu_by_class(class_name, option_value):
    x = driver.find_element_by_class_name(class_name)
    drop = Select(x)
    drop.select_by_value(option_value)


def execute_script_string(script):
    driver.execute_script(script)


def backward_page():
    driver.back()


def forward_page():
    driver.forward()


def select_values_from_drop_menu_by_id(id_item, option_value_0, option_value_1, option_value_2):
    x = driver.find_elements_by_id(id_item)
    str0 = x[0].text.split("\n")
    str1 = x[1].text.split("\n")
    str2 = x[2].text.split("\n")
    if str0[0] == "Giorno":
        select_value_by_web_element(x[0], option_value_0)
        if str1[0] == "Mese":
            select_value_by_web_element(x[1], option_value_1)
            if str2[0] == "Anno":
                select_value_by_web_element(x[2], option_value_2)


def select_value_by_web_element(web_element, value):
    select = Select(web_element)
    select.select_by_value(value)


def click_button_by_class_name(class_name):
    # get button by class name
    button = driver.find_element_by_class_name(class_name)
    # click action
    button.click()


def select_tags(sel_xpath, tag="option", attr="value"):
    element = driver.find_element_by_xpath(sel_xpath)
    all_options = element.find_elements_by_tag_name(tag)
    for option in all_options:
        console_log("Value is: %s" % option.get_attribute(attr))
        option.click()


def select_by_index(elem_name, index):
    x = driver.find_element_by_name(elem_name)
    select = Select(x)
    select.select_by_index(index)


def select_by_visible_text(elem_name, visible_text):
    x = driver.find_element_by_name(elem_name)
    select = Select(x)
    select.select_by_visible_text(visible_text)


def select_by_value(elem_name, value):
    x = driver.find_element_by_name(elem_name)
    select = Select(x)
    select.select_by_value(value)


def deselect_all_by_id(elem_id):
    x = driver.find_element_by_id(elem_id)
    select = Select(x)
    select.deselect_all()


def select_all_by_id(elem_id):
    x = driver.find_element_by_id(elem_id)
    select = Select(x)
    options = select.options
    for opt in options:
        if not opt.is_selected():
            opt.click()


def select_all_by_class_name(class_name):
    x = driver.find_element_by_class_name(class_name)
    select = Select(x)
    options = select.options
    for opt in options:
        """print('Option Current: ' + str(opt.text))"""
        if not opt.is_selected():
            opt.click()
            console_log('Option Selected: ' + str(opt.text) + ' Index: ' + str(opt.get_attribute("index")))


def clear_field_elem(element):
    element.clear()


def is_displayed_element(elem):
    return elem.is_displayed()


def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    original_style = element.get_attribute('style')
    """apply_style(element, "background: green; border: 2px solid yellow;")"""
    apply_style(element, "border: 2px solid violet;")
    sleep(10)
    apply_style(element, original_style)


def apply_style(element, s):
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)


def highlight_all_elements(elements):
    for elem in elements:
        highlight(elem)


def drag_and_drop(id_drag="draggable", id_drop="droppable"):
    refresh_browser()
    # identifying the source and target elements
    source = driver.find_element_by_id(id_drag)
    target = driver.find_element_by_id(id_drop)
    # drag and drop operation and the perform
    action.drag_and_drop(source, target).perform()


def screenshot(element, file_png='screen.png'):
    original_style = element.get_attribute('style')
    apply_style(element, "background: green; border: 2px solid yellow;")
    change_working_dir(create_dir('screenshot'))
    driver.save_screenshot(file_png)
    console_log('Screenshot created!')
    apply_style(element, original_style)


def current_working_dir():
    return os.getcwd()


def change_working_dir(path):
    os.chdir(path)


def create_dir(folder, curr_dir=current_working_dir()):
    directory = str(curr_dir) + '\\' + str(folder)
    path_dir = Path(directory)
    if not path_dir.exists():
        path_dir.mkdir(parents=True, exist_ok=True)
        console_log('Created the folder ' + str(folder) + ' in the working directory!')
        return directory
    else:
        console_log('The path directory ' + str(path_dir) + ' already exists!')
        return directory


def copy_text():
    action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()


def paste_text():
    action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()


def select_all_text():
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()


def insert_text_into_element(element, text):
    element.send_keys(text)


def click_and_hold_on_target_element(target_element):
    action.click_and_hold(on_element=target_element).perform()


def scroll_down_page_by_pixel(pixel):
    """execute_script_string('window.scrollBy(0,500)')"""
    if pixel > 0:
        execute_script_string('window.scrollBy(0,'+str(pixel)+')')
    else:
        console_error('The inserted value of pixel is not valid')


def scroll_up_page_by_pixel(pixel):
    """execute_script_string('window.scrollBy(0,500);')"""
    if pixel < 0:
        execute_script_string('window.scrollBy(0,'+str(pixel)+');')
    else:
        console_error('The inserted value of pixel is not valid')


def scroll_down_page_till_element_found(element):
    driver.execute_script('argument[0].scrollIntoView();', element)


def scroll_to_end_page():
    execute_script_string('window.scrollBy(0,document.body.scrollHeight);')


def get_color_resolution_of_screen():
    execute_script_string('console.log("Color resolution: " + screen.pixelDepth + " bits per pixel");')
    print_console_log_browser()


def get_screen_width():
    execute_script_string('console.log("Total Width: " + screen.width + ".");')
    print_console_log_browser()


def get_screen_height():
    execute_script_string('console.log("Total Height: " + screen.height + ".");')
    print_console_log_browser()


def print_console_log_browser():
    for entry in driver.get_log('browser'):
        message = entry["message"].split('"')
        console_log_browser(message[1])


def get_timestamp_ita():
    ts = time.gmtime()
    return time.strftime("%x %X", ts)


def get_timestamp_usa():
    ts = time.gmtime()
    return time.strftime("%Y-%m-%d %H:%M:%S", ts)


def find_element_by_name(name):
    return driver.find_element_by_name(name)


def find_elements_by_name(name):
    return driver.find_elements_by_name(name)


def find_elements_by_xpath(xpath):
    return driver.find_elements_by_xpath(xpath)


def find_element_by_xpath(xpath):
    return driver.find_element_by_xpath(xpath)


def find_elements_by_class_name(class_name):
    return driver.find_elements_by_class_name(class_name)


def find_element_by_class_name(class_name):
    return driver.find_element_by_class_name(class_name)


def find_element_by_css_selector(css_sel):
    return driver.find_element_by_css_selector(css_sel)


def find_elements_by_css_selector(css_sel):
    return driver.find_elements_by_css_selector(css_sel)


def find_element_by_id(id):
    return driver.find_element_by_id(id)


def find_elements_by_id(id):
    return driver.find_elements_by_id(id)


def find_element_by_css_and_compare(css_sel, string_to_compare):
    f = find_element_by_css_selector(css_sel)
    if f.text == string_to_compare:
        console_log('The item \"' + string_to_compare + '\" is present on the page')
        highlight(f)
    else:
        console_log('The item \"' + string_to_compare + '\" is not present on the page')


def find_element_by_id_and_compare(id, string_to_compare):
    f = find_element_by_id(id)
    if f.text == string_to_compare:
        console_log('The item \"' + string_to_compare + '\" is present on the page')
        highlight(f)
    else:
        console_log('The item \"' + string_to_compare + '\" is not present on the page')


def find_element_by_class_name_and_compare(class_name, string_to_compare):
    f = find_element_by_class_name(class_name)
    if f.text == string_to_compare:
        console_log('The item \"' + string_to_compare + '\" is present on the page')
        highlight(f)
    else:
        console_log('The item \"' + string_to_compare + '\" is not present on the page')


def find_elements_by_css_and_compare(css_sel, list_to_compare):
    f = find_elements_by_css_selector(css_sel)
    for el in f:
        for string_to_compare in list_to_compare:
            if el.text == string_to_compare:
                console_log('The item \"' + string_to_compare + '\" is present on the page')
                highlight(el)
            else:
                console_log('The item \"' + string_to_compare + '\" is not present on the page')


def find_elements_by_id_and_compare(id, list_to_compare):
    f = find_elements_by_id(id)
    for el in f:
        for string_to_compare in list_to_compare:
            if el.text == string_to_compare:
                console_log('The item \"' + string_to_compare + '\" is present on the page')
                highlight(el)
            else:
                console_log('The item \"' + string_to_compare + '\" is not present on the page')


def find_elements_by_class_name_and_compare(class_name, list_to_compare):
    f = find_elements_by_class_name(id)
    for el in f:
        for string_to_compare in list_to_compare:
            if el.text == string_to_compare:
                console_log('The item \"' + string_to_compare + '\" is present on the page')
                highlight(el)
            else:
                console_log('The item \"' + string_to_compare + '\" is not present on the page')


def print_strings_not_empty(str):
    for word in str:
        if word != '':
            console_log(word)


def split_text_web_element(elem):
    return elem.text.split('\n')


def split_file_url(file_url):
    return os.path.split(file_url)


def get_current_window_handle():
    return driver.current_window_handle


def get_window_handles():
    return driver.window_handles


def switch_window_handle():
    original_window = get_current_window_handle()
    for window_handle in get_window_handles():
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break


def get_specific_handle(num):
    return driver.window_handles[num]


def switch_to_window(num):
    driver.switch_to.window(get_specific_handle(num))


def wait_elem_to_be_clickable(element, xpath, time):
    if is_displayed_element(element) is True:
        WebDriverWait(driver, time).until(ec.element_to_be_clickable((By.XPATH, xpath))).click()


def is_directory(path):
    return os.path.isdir(path)


def get_screenshot_img():
    global ob
    ob = Screenshot_Clipping.Screenshot()


def get_img_url(elem, folder):
    return ob.get_element(driver, elem, folder)


def remove_file(file):
    os.remove(file)


def rename_file(file_name, new_file_name):
    os.rename(file_name, new_file_name)


def delete_directory_tree(dir):
    shutil.rmtree(dir, ignore_errors=True)


def wait_web_driver(time):
    return WebDriverWait(driver, time)
