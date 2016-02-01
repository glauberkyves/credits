import src.Captcha as captcha
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Noticia:
    def init(self, browser):
        try:
            print('Acionando link de noticias')
            browser.find_element_by_css_selector("a.cliqueRSS").click()
            browser.switch_to.frame(browser.find_element_by_id("fancybox-frame"))

            print('Ativando noticia')
            browser.find_element_by_css_selector('a.selecionarCategoriaRSS').click()

        except:
            raise Exception('Noticia nao encontrada')

        while True:
            browser.execute_script('$("div.rssNoticiaMeio").html($("#captchashow"))')
            captcha.Captcha(browser, 50, 119, 240, 161, 'captcha_code_rss', 'btn_confirmar_rss')
#            self.closeModal(browser)

    def closeModal(self, browser):
        try:
            print('Fechando modal')
            browser.switch_to_default_content()
            browser.find_element_by_id('fancybox-close').click()

        except:
            print('Modal ja esta fechada')

        self.init(browser)
