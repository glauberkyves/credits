from subprocess import check_output
from PIL import Image
import time

class Captcha:
    def __init__(self, browser, left, top, rigth, bottom, input, button):
        xCaptcha = 1
        while xCaptcha <= 10:
            time.sleep(2)

            print('Procurando por captcha')
            print('Screenshot pagina')
            browser.save_screenshot('img/pagina.png')

            print('Redimensionando screenshot para 800')
            basewidth = 800
            img = Image.open('img/pagina.png')
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1] * float(wpercent))))
            img = img.resize((basewidth, hsize))
            img.save('img/captcha.png')

            print('Crop captcha')
            img = Image.open('img/captcha.png')
            img = img.crop((
                left,
                top,
                rigth,
                bottom
             ))
            img.save('img/captcha.png')

            print('Altera os níveis de cores')
            check_output("convert img/captcha.png -level 20000,0,20000 img/captcha.png", shell=True)

            print('Converte para padrão de imagem com cores reduzidas')
            check_output("convert  img/captcha.png  img/captcha.pgm", shell=True)

            print('Transforma os pixels de uma determinada frequencia em pretos')
            check_output("convert  img/captcha.pgm -black-threshold 65000  img/captcha.tif", shell=True)

            print('Inverte as cores da imagem')
            check_output("convert  img/captcha.tif -negate  img/captcha.tif", shell=True)

            print('Traduzir captcha')
            check_output("tesseract img/captcha.tif img/captcha", shell=True)

            with open ("img/captcha.txt", "r") as textCaptcha:
                data = textCaptcha.read().replace('\n', '')

            print('Informando captcha')
            browser.execute_script('document.getElementById("' + input + '").value = ""')
            browser.find_element_by_id(input).send_keys(data)
            browser.find_element_by_id(button).click()

            try:
                WebDriverWait(browser, 5).until(EC.alert_is_present())

                alert = browser.switch_to_alert()
                alert.accept()

                print('Tentativa captcha: ' + str(xCaptcha))
                xCaptcha = xCaptcha + 1

            except:
                print('Captcha validado')
                break