from selenium.webdriver import Firefox

firefox = Firefox()

firefox.get('http://selenium.dunossauro.live/aula_05_a.html')

div_1 = firefox.find_element_by_id('lisp')
