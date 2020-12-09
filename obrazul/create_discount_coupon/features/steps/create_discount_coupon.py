from behave import given, when, then
from time import sleep

# Obrazul website
base_url = 'http://localhost/'

# Variables with discount coupon data
coupon_name = 'Teste-Selenium'
valid_date = '07/12/2020 00:00 até 03/11/2021 23:59'
code = 'SELENIU'
minimum_value = '50.00'
discount = '10.00'


@given(u'The user is on the home website page')
def step_impl(context):
    context.web.get(base_url)


@then(u'Click on \'Entre\'')
def step_impl(context):
    login_link = context.web.find_element_by_css_selector('[href="/login/"]')
    login_link.click()
    sleep(0.5)


@then(u'The user logs in')
def step_impl(context):
    email_address = context.web.find_element_by_css_selector('[name="login"]')
    password = context.web.find_element_by_css_selector('[name="password"]')
    submit_btn = context.web.find_element_by_css_selector('[type="submit"]')

    email_address.send_keys("desenvolvimento@obrazul.com.br")
    password.send_keys("Obr@zul2020")
    submit_btn.click()
    sleep(0.5)


@given(u'The user is on dashboard page')
def step_impl(context):
    menu_item = context.web.find_element_by_css_selector('[href="#menu-products-and-stores"]')
    menu_item.click()
    sleep(0.5)


@then(u'click on \'Cupons de Desconto\'')
def step_impl(context):
    menu_item = context.web.find_element_by_css_selector('[href="/dashboard/cupons-de-desconto/"]')
    menu_item.click()
    sleep(0.5)


@given(u'The user is discount coupon creation page')
def step_impl(context):
    new_coupon_btn = context.web.find_element_by_css_selector('[id="btn-coupon"]')
    new_coupon_btn.click()
    sleep(2)


@then(u'insert coupon information')
def step_impl(context):
    context.web.find_element_by_css_selector('[name="cupon_name"]').send_keys(coupon_name)
    context.web.find_element_by_css_selector('[name="valid_date"]').send_keys(valid_date)
    context.web.find_element_by_css_selector('[name="cupon_code"]').send_keys(code)
    context.web.find_element_by_css_selector('[name="min_price"]').send_keys(minimum_value)
    context.web.find_element_by_css_selector('[name="discount_value"]').send_keys(discount)


@then(u'click on \'Criar\'')
def step_impl(context):
    create_btn = context.web.find_element_by_css_selector('[type="submit"]')
    create_btn.click()
    sleep(4)
