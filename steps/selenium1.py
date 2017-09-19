from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://rawgit.com/dotsbb/html5-css3-js-calculator/master/")

browser.find_element_by_css_selector("#calculator-button-9").click()
browser.find_element_by_css_selector("button[id='calculator-button-\+']").click()
browser.find_element_by_xpath("//button[@id='calculator-button-3']").click()
browser.find_element_by_css_selector("#calculator-button-\=").click()
#element = browser.find_element_by_class_name("display-text").text
#element.clear()
#element.send_keys("13")


assert browser.find_element_by_class_name("display-text").text == "12"

browser.close()