from behave import given, when, then
from time  import sleep

# Variavel com a URL do site que iremos interagir.
base_url = 'https://globoesporte.globo.com'

# Variaveis com os elementos que iremos interagir na pagina
element_menu = 'menu-button'
element_link_brasileirao = 'menu-item-title'
get_primeiro = '//*[@id="classificacao_wrapper"]/article/section[1]/div/table/[1]/tbody/tr[1]/td[2]/strong'


@given(u'acesso a pagina inicial do globo esporte')
def step_impl(context):
    context.web.get(base_url)


@when(u'clico no menu do brasileirao')
def step_impl(context):
    element_menu = context.web.find_element_by_class_name(element_menu)
    element_menu.click()
    element_link_brasileirao = context.web.find_element_by_class_name(element_link_brasileirao)
    element_link_brasileirao.click()


@when(u'classificacao e exibida')
def step_impl(context):
    context.get_primeiro = context.web.find_element_by_xpath(get_primeiro)


@then(u'devo saber quem e o primeiro colocado')
def step_impl(context):
    primeiro = context.get_primeiro.text()
    print(primeiro)

    # Salvar o resultado da variavel primeiro em um arquivo txt
    file = open("features/results/results.txt", "r")
    content = file.readlines()
    content.append("\n" + primeiro)
    file = open("fetures/results/results.txt", "w")
    file.writelines(content)
