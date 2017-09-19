from selenium import webdriver

class BasePageObject:	
	def __init__(self, browser):
		self.browser = browser
		
		
class Calculator(BasePageObject):
	button9 = "#calculator-button-9"
	button3 = "#calculator-button-3"
		
	def click_button(self, button):
		self.browser.find_element_by_css_selector(button).click()
		return self
		
	def click_plus(self):
		self.browser.find_element_by_id("calculator-button-\+").click()
		return self
		
	def click_equals(self):
		self.browser.find_element_by_css_selector("#calculator-button-\=").click()
		return self
		
	def assertion(self):
		self.browser.find_element_by_class_name("display-text").text == "12"
		return self
		
	def browser_close(self):
		self.browser.close()
		return self
		
if __name__ == "__main__":
	browser = webdriver.Firefox()
	browser.get("https://rawgit.com/dotsbb/html5-css3-js-calculator/master/")
		

	page = Calculator(browser)
	page.click_button(button9).click_plus().click_button(button3).click_equals().assertion().browser_close()
		
		
		
