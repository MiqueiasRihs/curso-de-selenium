from selenium.webdriver import Firefox

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

browser = Firefox()
browser.get(url)
browser.implicitly_wait(10)

dict_elements = {}
list_elements = []
x = {}

title = browser.find_element_by_tag_name('h1')
p = browser.find_elements_by_tag_name('p')

for each_element in p:
    x = {each_element.get_attribute('atributo'): each_element.text}
    list_elements.append(x)

if 'h1' in dict_elements.keys():
    dict_elements['h1'] = list_elements

else:
    dict_elements = {
        'h1': list_elements
    }


print(dict_elements)
browser.quit()