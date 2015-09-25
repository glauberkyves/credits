"""
taking screenshots
"""
from splinter.browser import Browser

browser = Browser('firefox')

# adsfa
url = "http://gostodisso.com"
browser.visit(url)

browser.find_by_css("#iframeLogin").click()

with browser.get_iframe('fancybox-frame') as iframe:
    iframe.fill('cadEmail', "glauberkyves@gmail.com")
    iframe.fill('cadSenha', "St0rm100")
    iframe.find_by_id("btnSubmit").click()

browser.find_by_css("a.home").click()
# faco login
#user = "glauberkyves@gmail.com"
#browser.fill('cadEmail', user)
#browser.driver.save_screenshot('screenshot.png')

#browser.quit()