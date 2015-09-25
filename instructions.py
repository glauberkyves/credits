"""
taking screenshots
"""
import time
from PIL import Image
from selenium import webdriver
from subprocess import check_output

######### noticias
def noticias(browser):
    print('Acionando link de noticias')
    browser.find_element_by_css_selector("a.cliqueRSS").click()

    browser.switch_to.frame(browser.find_element_by_id("fancybox-frame"))
    if browser.find_element_by_css_selector('a.selecionarCategoriaRSS'):
        print('Ativando noticia')
        browser.find_element_by_css_selector('a.selecionarCategoriaRSS').click()

        print('procurando por captcha')
        if browser.find_element_by_id('captcha_rss'):
            time.sleep(10)
            browser.execute_script('$("#fancybox-frame").contents().scrollTop(999999999)')

            print('Screenshot pagina')
            element = browser.find_element_by_css_selector('div.captcha-box')
            location = element.location
            size = element.size
            browser.save_screenshot('pagina.png')

            im = Image.open('pagina.png')
            left = location['x']
            top = location['y']

            right = location['x'] + size['width']
            bottom = location['y'] + size['height']

            print('Crop captcha')
            im = im.crop((left + 200, top + 48, right + 140, bottom + 50))
            im.save('captcha.png')

            print('Altera os níveis de cores')
            check_output("convert captcha.png -level 20000,0,20000 captcha.png", shell=True)

            print('Converte para padrão de imagem com cores reduzidas')
            check_output("convert  captcha.png  captcha.pgm", shell=True)

            print('Transforma os pixels de uma determinada frequencia em pretos')
            check_output("convert  captcha.pgm -black-threshold 65000  captcha.tif", shell=True)

            print('Inverte as cores da imagem')
            check_output("convert  captcha.tif -negate  captcha.tif", shell=True)

            print('Traduzir captcha')
            check_output("tesseract captcha.tif out", shell=True)

            with open ("out.txt", "r") as textCaptcha:
                data = textCaptcha.read().replace('\n', '')

            browser.find_element_by_id("captcha_code_rss").send_keys(data)
            browser.find_element_by_id("btn_confirmar_rss").click()
        else:
            print('Captcha não encontrado')
    else:
        print('Nenhuma noticia encontrada')

    return

browser = webdriver.Firefox()

print('acessando o site gostodisso.com')
browser.get('http://gostodisso.com/')

print('acionando login')
browser.find_element_by_id("iframeLogin").click()

print('logando no sistema')
browser.switch_to.frame(browser.find_element_by_id("fancybox-frame"))
browser.execute_script('$("#cadEmail").val("glauberkyves@gmail.com")')
browser.execute_script('$("#cadSenha").val("St0rm100")')
browser.find_element_by_id("btnSubmit").click()
print('logado')

browser.switch_to_default_content()

print('procurando a existencia de um RSS de noticias')
if browser.find_element_by_css_selector("a.cliqueRSS"):
    noticias(browser)
else:
    print("No, it wasn't found... We need to improve our SEO techniques")