from selenium import webdriver
import PAGE_OBJECTS
from behave import given, when, then


	
@when(u'I click 9 button')
def step_impl(context):
	context.page_object = context.page_object.click_button(context.page_object.button9)

@when(u'I click plus button')
def step_impl(context):
	context.page_object = context.page_object.click_plus()
	
@when(u'I click 3 button')
def step_impl(context):
	context.page_object = context.page_object.click_button(context.page_object.button3)
	
@when(u'I click = button')
def step_impl(context):
	context.page_object = context.page_object.click_equals()
	
@then(u'the result is 13')
def step_impl(context):
	context.page_object = context.page_object.assertion()
	