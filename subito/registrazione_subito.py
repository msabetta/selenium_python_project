from utils import *

setup()

sleep(5)

get_page('https://www.subito.it/')

sleep(5)

click_link_by_css_selector('#header > header > div > div.index-module_top-menu-container__3_8EF > div > a:nth-child(2) > p')

sleep(5)

fill_field_by_name("username","yourname@test.it")
fill_field_by_name("password","password1")
click_button_by_css_selector_simple('#layout > main > div > div > div > form > div:nth-child(2) > div > div.Tooltip_text-field-wrapper__3r2h6 > div > button')

select_values_from_drop_menu_by_id("birthdate", "20", "06", "1957")

#select_all_by_class_name("classes_select-first-run__2KtoT")

#click male
click_button_by_class_name('styles_radio__1odZa')

#fill municipality name
fill_field_by_name_and_return('town', "Cava de' Tirreni (SA)")

#click three agree conditions

radioboxes = find_elements_by_class_name('styles_checkmark__-wBvL')

for box in radioboxes:
    box.click()

#click_button_by_css_selector_simple('#layout > main > div > div > div > form > div.Form_input-wrapper-button__3xGdd > button')

click_button_by_class_name('classes_sbt-button__2kL5p classes_solid__2CpI2 classes_medium__NcoSo')

sleep(20)

tear_down()

quit_sessions()