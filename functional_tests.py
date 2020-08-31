from selenium import webdriver
import unittest
from django.urls import reverse

class NewVisitorTest(unittest.TestCase):  

	def setUp(self):  
		self.browser = webdriver.Firefox()

	def tearDown(self):  
		self.browser.quit()

	# Edith has heard about a cool new online page where she can create a cv and get inspiration from other people as well. She goes
	# to check out its homepage
	def test_title_works(self):
		self.browser.get('http://localhost:8000')
		# She notices the browser title is a french word éphémère
		self.assertIn('éphémère', self.browser.title)

	def test_home_page_is_displayed(self):
		self.browser.get('http://localhost:8000')	
		#Edith visits the site and views the home page for the first time
		alert = self.browser.find_element_by_class_name('media-body')
		self.assertEquals(alert.find_element_by_tag_name('h2').text, 'Breaking Bad')

	#Edith clicks on resumes right next to the home to have a look at rhe resumes available 
	def test_resume_page_is_displayed(self):
		self.browser.get('http://localhost:8000/resume/')
		self.assertIn('About Me',self.browser.page_source)

	#she is intrigued and proceed to register to create one for herself
	def test_register_page_is_displayed(self):
		self.browser.get('http://localhost:8000/register/')
		self.assertIn('Become part of the family today!',self.browser.page_source)

	#she then decides to login to have a try
	def test_login_page_is_displayed(self):
		self.browser.get('http://localhost:8000/login/')
		self.assertIn('Log In!',self.browser.page_source)

	#She has a look at her watch and logs out as she realises she is going to be late for work
	def test_logout_page_is_displayed(self):
		self.browser.get('http://localhost:8000/logout/')
		self.assertIn('You have been logged out :/',self.browser.page_source)


if __name__ == '__main__':  
    unittest.main(warnings='ignore')  
