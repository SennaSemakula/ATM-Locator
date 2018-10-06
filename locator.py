"""This class allows users to enter their location"""
import requests
import json

class Locator():
	"""Class that identifies the nearest ATM for users"""

	def __init__(self, location):
		self.location = location
		self.first_code = ''
		self.second_code = ''
		self.post_code = ''


	def prompt_location(self):
		self.first_code = input("Enter first part of your post code: ")
		self.second_code = input("Enter second part of your post code: ")

		self.postcode = self.first_code + self.second_code

		return self.post_code


	def find_location(self, post_code):
		post_code = self.prompt_location()

		#Look up post code from a list of API's
		url = 'maps.googleapis.com/maps/api/geocode/json?=' + self.first + '+' + self.second_code
		print(url)
		response = request.get(url)

		data = response.json()

test_locator = Locator('test')
post_code = test_locator.prompt_location()
test_locator.find_location(post_code)



