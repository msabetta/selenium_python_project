from utils import *

setup()

try:
    # open Amazon Homepage
    get_page("http://www.amazon.com")
    input_search = find_element_by_css_selector('#twotabsearchtextbox')

    input_search.send_keys("notebook hp")
    input_search.submit()
    console_log("ricerca effettuata con successo....")

    print_cookies()

    handles = get_window_handles()

    sleep(5)
    find_element_by_name('field-keywords').clear()

    select_value_from_drop_menu_by_id('searchDropdownBox', 'search-alias=aps')

    input_search_2 = fill_field_by_name('field-keywords', "auto")
    submit = find_element_by_id('nav-search-submit-button')
    submit.click()
    console_log("ricerca effettuata con successo....")

    sleep(10)
    tear_down()

except Exception as e:
    print(e)
    quit_sessions()