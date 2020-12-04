from selenium.webdriver import Firefox
from urllib.parse import urlparse


url = ('https://dev.obrazul.com.br/')

browser = Firefox()
browser.get(url)


def login(browser, email, password):
    # get login form
    login_form = browser.find_element_by_css_selector('form')

    # get each field from form
    email_field = login_form.find_element_by_css_selector('[name="login"]')
    password_field = login_form.find_element_by_css_selector('[name="password"]')
    submit_btn = login_form.find_element_by_css_selector('[type="submit"]')

    # Filling in the login fields and submit
    email_field.send_keys(email)
    password_field.send_keys(password)
    submit_btn.click()


def find_by_href(browser, link):
    elementos = browser.find_elements_by_tag_name('a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento


#  ========== init ==========
find_by_href(browser, '/login/').click()
login(browser, 'Miqueias@obrazul.com.br', '88589862Mq')
