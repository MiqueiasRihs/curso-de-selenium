from selenium.webdriver import Firefox

b = Firefox()
url = 'http://selenium.dunossauro.live/aula_06_a.html'

b.get(url)

b.find_elements_by_css_selector('div.form-group')

b.find_elements_by_css_selector('div.form-group + br')[1].get_attribute('id')
b.find_elements_by_css_selector('div.form-group >')[1].get_attribute('id')

# Da tag div com a class form-group pegue o filho com id dentro nome
b.find_element_by_css_selector('div.form-group > #dentro-nome')

# Do form, pegue todas as tag label existentes ignorando a hierartquia
b.find_element_by_css_selector('form label')
