from utils import *

setup()

search_word_from_google("subito")

sleep(5)

click_link_by_class_name('yuRUbf')

sleep(5)

click_button_by_css_selector('#didomi-notice-agree-button')

sleep(5)

#search auto in campania

fill_field_by_name('main-keyword-field', "auto")

sleep(5)

find_element_by_id('main-category-selection').click()

sleep(5)

find_element_by_css_selector('#anchor-motori > ul > li:nth-child(1) > button').click()

sleep(5)

find_element_by_name('geo-search-field').click()
fill_field_by_name_and_return('geo-search-field','Campania')

sleep(5)

find_element_by_class_name('button-icon-lens').click()

sleep(20)

tear_down()

quit_sessions()