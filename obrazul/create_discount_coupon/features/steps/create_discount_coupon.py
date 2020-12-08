from behave import given, when, then
from time import sleep

# Obrazul website
base_url = 'https://dev.obrazul.com.br/'


@given(u'The user is on the home website page')
def step_impl(context):
    context.web.get(base_url)


@given(u'Click on \'Entre\'')
def step_impl(context):
    login_link = context.web.find_element_by_css_selector('[class="navbar-brand"]')
    login_link.click()
    sleep(3)


@when(u'The user logs in')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user logs in')


@when(u'The user should be redirected to their dashboard')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user should be redirected to their dashboard')


@given(u'The user is on dashboard page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The user is on dashboard page')


@then(u'The user should be click on \'Cupons de Desconto\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The user should be click on \'Cupons de Desconto\'')


@then(u'The user should be redirected to discount coupon creation page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The user should be redirected to discount coupon creation page')


@given(u'The user is discount coupon creation page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The user is discount coupon creation page')


@then(u'click on \'Novo Cupom\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then click on \'Novo Cupom\'')


@then(u'insert coupon information')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then insert coupon information')


@then(u'click on \'Criar\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then click on \'Criar\'')
