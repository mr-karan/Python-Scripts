from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

def get_random(list):
    return random.choice(list)


browser = webdriver.Firefox()

browser.get('http://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')
movekeys=[Keys.LEFT,Keys.DOWN,Keys.UP,Keys.RIGHT]

while(True):
    htmlElem.send_keys(get_random(movekeys))








