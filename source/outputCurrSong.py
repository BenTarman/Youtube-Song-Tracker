#!/home/ben/pythonCodes/Youtube-Song-Tracker/venv/bin/python3.5 -u 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import memcache
#sudo apt-get install memcached python-memcache
import multiprocessing as mp
import youtubeSongs as yt



if __name__ == "__main__":
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    userInput = "null"
    while True:
        yt.initYoutube() #only executes once!

        yt.displayCurrSong()

        userInput = mc.get("Value")

        if (userInput == "n"):
            yt.nextSong()
        elif (userInput== "p"):
            yt.previousSong()
        elif (userInput == "r"):
            yt.replaySong()
        else:
            continue
        mc.delete("Value")
        time.sleep(5)



'''
#driver = webdriver.Remote(command_executor=session_url,desired_capabilities={})
#driver.session_id = session_id
shared = memcache.Client(['127.0.0.1:11211'], debug=0)
print(shared.get('SessionId'))

session_id = shared.get('SessionId')
session_url  = shared.get('SessionUrl')

driver = webdriver.Remote(command_executor = session_url, desired_capabilities = {})
driver.session_id = session_id




songDisplayed = False
currUrl = ""

browser = settings.browser

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
'''
