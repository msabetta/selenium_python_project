from utils import *
import traceback

try:
    setup()

    maximize_window()

    get_page('https://www.tim.it/')

    sleep(5)

    #click conferma cookie
    click_button_by_css_selector('#cookie-policy-bar > div > div > div.to-cookie-bar__buttons > a')

    sleep(5)

    #click su "Fisso e Mobile"
    click_link_by_css_selector('body > div.tl-page > div.to-header > div.to-header__main-header > div > div > div > div.to-main-header__menu > div:nth-child(1) > a')

    sleep(5)

    #click su "Mobile
    click_link_by_css_selector('body > div.tl-page > div.to-header.-is-active > div.to-menu.-is-active > div > div.to-menu__level-2.-is-active > div.to-menu__level-2__lists > ul > li:nth-child(2) > a')

    sleep(5)

    #click su scopri offerta 11 euro
    click_button_by_css_selector_simple('#c--108131180 > div.to-listing-longlist__body > div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > a')

    scroll_to_end_page()
    element = find_element_by_css_selector('#c--254383989 > div.to-faqaccordion__header.tl-col-3 > div.ta-heading.ta-heading--h1-small')
    element.location_once_scrolled_into_view

    find_element_by_css_and_compare(
        '#c--254383989 > div.to-faqaccordion__header.tl-col-3 > div.ta-heading.ta-heading--h1-small',
        'Hai bisogno di altre informazioni?')


    find_element_by_css_and_compare(
        '#c--254383989 > div.to-faqaccordion__header.tl-col-3 > div.tm-tab-navigation.swiper-container.tm-tab-navigation--vertical.swiper-container-initialized.swiper-container-horizontal.swiper-container-free-mode > div.swiper-wrapper > div > div > a',
        'Info e supporto')

    find_element_by_css_and_compare('#c-20177849 > div:nth-child(1)', 'Come si attiva')

    find_element_by_css_and_compare('#c-20177849 > div:nth-child(2)',
                                    'È possibile attivare la TIM Young Senza Limiti per i minori di 18 anni?')

    find_element_by_css_and_compare('#c-20177849 > div:nth-child(3)', 'Ulteriori informazioni')

    sleep(30)

    tear_down()

except:
    traceback.print_exception()
    tear_down()
    quit_sessions()
