from selenium import webdriver
import PAGE_OBJECTS

def before_scenario(context, scenario):
	context.browser = webdriver.Firefox()
	context.browser.get("https://rawgit.com/dotsbb/html5-css3-js-calculator/master/")
	context.page_object = PAGE_OBJECTS.Calculator(context.browser)
	
def after_scenario(context, scenario):
	context.browser.close()
	