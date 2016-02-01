import src.Captcha as captcha
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Midia:
    def init(self, browser):
        print('Acionando link de midias')
        browser.get('http://gostodisso.com/usuario-playlist')

#        try:
        print('Procurando links patrocinado')
        browser.find_element_by_css_selector('[title="#linkpatrocinado"]').click()
        browser.find_element_by_css_selector('a[class="cliqueLP"]').click()

        time.sleep(21)

        #try:
        WebDriverWait(browser, 5).until(EC.alert_is_present())

        alert = browser.switch_to_alert()
        alert.accept()

        time.sleep(2)
        browser.find_element_by_id('fancybox-close').click()
        browser.execute_script('$("#linkpatrocinado input[type=radio]:first").click()')
        browser.find_element_by_id('enquete_linkpatrocinado_proximo').click()

        captcha.Captcha(browser,  560, 365, 780, 408, 'captcha_code_linkpatrocinado', 'btn_confirmar_linkpatrocinado')

        #except:
        #    print('Captcha validado')

#        except:
#            print('d')ss").click()