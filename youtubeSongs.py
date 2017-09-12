from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

'''

ffprofile = webdriver.FirefoxProfile()
adblockfile = '/home/bentarman/Downloads/adblock_plus-2.9.1-an+fx+sm+tb.xpi'
ffprofile.add_extension(adblockfile)
ffprofile.set_preference("extensions.adblockplus.currentVersion", "2.4")
browser = webdriver.Firefox(ffprofile)
'''
fp = webdriver.FirefoxProfile('/home/bentarman/.mozilla/firefox/rkvkm76d.default')

browser = webdriver.Firefox(fp)
#browser = webdriver.Firefox(executable_path = r'/usr/bin/geckodriver')
browser.get("https://www.youtube.com/")


#sign in to googlePlus

elem = browser.find_element_by_class_name("style-scope paper-button")

elem.click()

time.sleep(2)
#elem = browser.find_element_by_id("identifierId")
#elem.send_keys("email here", Keys.RETURN)

time.sleep(1)

elem = browser.find_element_by_xpath('//div[@id="password"]')
elem.send_keys(sys.argv[1], Keys.RETURN)

time.sleep(3)
#search for music
elem = browser.find_element_by_id("search-input")
elem.send_keys("my mix", Keys.RETURN)

time.sleep(3)



elem = browser.find_element_by_id("thumbnail")
elem.click()

songDisplayed = False
currUrl = ""

while True:
    if songDisplayed and currUrl == browser.current_url:
        pass

    else:
        currUrl = browser.current_url
        time.sleep(3)
        elem = browser.find_element_by_class_name("style-scope ytd-video-primary-info-renderer")


        songName = ""
        for c in elem.text:
            songName += c
            if c == "\n":
                break
        print(songName)
        songDisplayed = True
