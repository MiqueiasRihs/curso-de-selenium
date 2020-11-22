from selenium.webdriver import Firefox

url = "https://curso-python-selenium.netlify.app/aula_03.html"

browser = Firefox()

browser.get(url)

browser.implicitly_wait(10)

a = browser.find_element_by_tag_name('a')

for click in range(10):
    ps = browser.find_elements_by_tag_name('p')
    a.click()
    print('Valor do ultimo p: %s | Valor do click %s' % (ps[-1].text, click))

    print("Os valores são iguais %s" % bool(ps[-1].text == str(click)))

browser.quit()
