from splinter import Browser
from selenium.webdriver.common.keys import Keys

browser = Browser('firefox')

browser.visit("https://rawgit.com/dotsbb/html5-css3-js-calculator/master/")

browser.find_by_css("#calculator-button-9").click()
browser.find_by_css("button[id='calculator-button-\+']").click()
browser.find_by_xpath("//button[@id='calculator-button-3']").click()
browser.find_by_css("#calculator-button-\=").click()
#element = browser.find_by_css(".display-text").fill("13")

assert browser.find_by_css(".display-text").text.is_text_present("13")