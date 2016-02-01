from selenium import webdriver
import src.Noticia as noticia
import src.Midia as midia

print('Acessando o site gostodisso.com')
browser = webdriver.Firefox()
browser.get('http://gostodisso.com/')

print('Acionando login')
browser.find_element_by_id("iframeLogin").click()

print('Logando no sistema')
browser.switch_to.frame(browser.find_element_by_id("fancybox-frame"))
browser.execute_script('$("#cadEmail").val("glauberkyves@gmail.com")')
browser.execute_script('$("#cadSenha").val("St0rm100")')
browser.find_element_by_id("btnSubmit").click()
print('Logado :)')

browser.switch_to_default_content()

try:
    print('Procurando a existencia de um RSS de noticias')
    noticia.Noticia().init(browser)

except:
    print("Procurando outro item")
    midia.Midia().init(browser)