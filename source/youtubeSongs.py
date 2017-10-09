from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import memcache



fp = webdriver.FirefoxProfile('/home/bentarman/.mozilla/firefox/rkvkm76d.default')

browser = webdriver.Firefox(fp)
browser.get("https://www.youtube.com/")

def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

@run_once
def initYoutube():
    '''

    ffprofile = webdriver.FirefoxProfile()
    adblockfile = '/home/bentarman/Downloads/adblock_plus-2.9.1-an+fx+sm+tb.xpi'
    ffprofile.add_extension(adblockfile)
    ffprofile.set_preference("extensions.adblockplus.currentVersion", "2.4")
    browser = webdriver.Firefox(ffprofile)
    '''
    global browser
    global fp



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
    time.sleep(5)

    elem = browser.find_element_by_class_name("style-scope ytd-thumbnail-overlay-hover-text-renderer")
    time.sleep(2)
    elem.click()



'''
    session_url = browser.command_executor._url
    session_id = browser.session_id

    print(session_id)
    shared = memcache.Client(['127.0.0.1:11211'], debug=0)
    shared.set('SessionId', session_id)
    shared.set('SessionUrl', session_url)


'''


def nextSong():
    global browser
    elem = browser.find_element_by_xpath("//a[@Title='Next']")
    elem.click()

def previousSong():
    global browser
    elem = browser.find_element_by_xpath("//a[@Title='Replay']")
    elem.click()
    elem.click()

def replaySong():
    global browser
    elem = browser.find_element_by_xpath("//a[@Title='Replay']")
    elem.click()

def displayCurrSong():
    global browser
    currUrl = ""

    if currUrl == browser.current_url:
        pass
    else:
        currUrl = browser.current_url
        time.sleep(1.5)
        elem = browser.find_element_by_class_name("style-scope ytd-video-primary-info-renderer")

        songName = ""
        for c in elem.text:
            songName += c
            if c == "\n":
                break
        print(songName)






















