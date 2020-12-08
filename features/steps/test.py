from selenium.webdriver import Firefox

browser = Firefox()

url = 'https://blog.geekhunter.com.br/automatizando-testes-com-python-selenium-e-behave/'

browser.get(url)

menu = browser.find_element_by_class_name('navbar-brand')

menu.click()
