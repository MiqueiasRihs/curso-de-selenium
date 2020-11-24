from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import sleep
from pprint import pprint

browser = Firefox()

browser.get("http://selenium.dunossauro.live/aula_04.html")


def get_links(browser, elemento):
    resultado = {}
    elemento = browser.find_element_by_tag_name(elemento)
    ancoras = elemento.find_elements_by_tag_name('a')

    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')

    return resultado

sleep(2)

aulas = get_links(browser, 'aside')
pprint(aulas)


exercicio = get_links(browser, 'main')
pprint(exercicio)

browser.get(exercicio['Exercício 3'])