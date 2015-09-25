"""
taking screenshots
"""
import time
from PIL import Image
from splinter.browser import Browser


print('Abrindo navegador Firefox')
browser = Browser('firefox')

######## noticias
def noticias(browser):
    print('RSS de noticias encontrado')
    print('Acionando link de noticias')
    browser.find_by_css("a.cliqueRSS").click()

    with browser.get_iframe('fancybox-frame') as iframe:
        if iframe.find_by_css('a.selecionarCategoriaRSS'):
            print('Ativando noticia')
            iframe.find_by_css('a.selecionarCategoriaRSS').click()

            print('procurando por captcha')
            if iframe.find_by_id('captcha_rss'):
                time.sleep(10)
                print('Screenshot pagina')
                browser.execute_script("$('#fancybox-frame').contents().scrollTop($('#fancybox-frame').height())")
                browser.driver.save_screenshot('captcha.png')

                print('Crop captcha')
                img = Image.open('captcha.png')
                #img2 = img.crop(
                #   # (
                #        600,
                #        370,
                #        790,
                #        420
                #    )
                #)
                img2.save("captcha2.jpg")
            else:
                print('Captcha não encontrado')
        else:
            print('Nenhuma noticia encontrada')
    return

print('acessando o site gostodisso.com')
url = "http://gostodisso.com"
browser.visit(url)

print('acionando login')
browser.find_by_css("#iframeLogin").click()

print('logando no sistema')
with browser.get_iframe('fancybox-frame') as iframe:
    iframe.fill('cadEmail', "glauberkyves@gmail.com")
    iframe.fill('cadSenha', "St0rm100")
    iframe.find_by_id("btnSubmit").click()
print('logado')

print('procurando a existencia de um RSS de noticias')
if browser.is_text_present("Noticias"):
    noticias(browser)
else:
    print("No, it wasn't found... We need to improve our SEO techniques")

#browser.find_by_css("a.home").click()
# faco login
#user = "glauberkyves@gmail.com"
#browser.fill('cadEmail', user)
#browser.driver.save_screenshot('screenshot.png')

#browser.quit()