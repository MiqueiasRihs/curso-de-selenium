from selenium.webdriver import Firefox

b = Firefox()
url = 'http://selenium.dunossauro.live/aula_06_a.html'

b.get(url)

# ===== Usando a atributo 'type' [att=valor] =====
tag_type_nome = b.find_element_by_css_selector('[type="text"]')
tag_type_senha = b.find_element_by_css_selector('[type="password"]')
tag_type_btn = b.find_element_by_css_selector('[type="submit"]')

# ===== Usando a atributo 'name' [att=valor] =====
tag_name_nome = b.find_element_by_css_selector('[name="nome"]')
tag_name_senha = b.find_element_by_css_selector('[name="senha"]')
tag_name_btn = b.find_element_by_css_selector('[name="l0c0"]')

# ===== Usando a atributo [att*=valor] =====
"""
nome = b.find_element_by_css_selector('[name*="ome"]')
senha = b.find_element_by_css_selector('[name*="nha"]')
btn = b.find_element_by_css_selector('[name*="l0"]')
"""

# ===== Usando a atributo [att|=valor] =====
"""
nome = b.find_element_by_css_selector('[name|="nome"]')
senha = b.find_element_by_css_selector('[name|="senha"]')
btn = b.find_element_by_css_selector('[name|="l0c0"]')
"""

# ===== Usando a atributo [att^=valor] =====
nome = b.find_element_by_css_selector('[name^="n"]')
senha = b.find_element_by_css_selector('[name^="s"]')
btn = b.find_element_by_css_selector('[name^="l"]')

nome.send_keys('Miqueias')
senha.send_keys('123')
# btn.click()
