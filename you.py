from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print('Abrindo video')
browser = webdriver.Firefox()

browser.get('https://www.youtube.com/watch?v=_XjTGEJ29bA')
time.sleep(4)
browser.find_element_by_id('autoplay-checkbox').click()

while True:
    total = 2
    for x in range(0, total):
        browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        browser.get('https://www.youtube.com/watch?v=_XjTGEJ29bA')

    time.sleep(5)
    print('tempoooo')

    for x in range(0, total):
        print('Fechando aba: ' + str(x +2))
        browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + str(x + 2))
        browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + ('w'))
#
#    browser.refresh()
#    time.sleep(2)
#    print('Fechando navegador')
#    browser.quit()