from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://rawgit.com/dotsbb/html5-css3-js-calculator/master/")

browser.find_element_by_css("#calculator-button-8").click()
browser.find_element_by_css("#calculator-button-+").click()
browser.find_element_by_css("#calculator-button-3").click()
browser.find_element_by_css("#calculator-button-=").click()

