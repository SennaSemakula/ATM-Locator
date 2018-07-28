#Class that stores all the location details of an ATM
class Location():

	def __init__(self, country, city, latitude, longitude, sea_level):
		self.country = country.title()
		self.city = city.title()
		self.latitude = latitude
		self.longitude = longitude

	def set_latitude(self, latitude):
		try:
			val = input(latitude)
		except: 
			print("Please insert an integer for latitude!")	
		else:
			self.latitude = latitude

	def set_longitude(self, longitude):
		try:
			val = input(longitude)
		except: 
			print("Please insert an integer for longitude!")	
		else:
			self.longitude = longitude

	def set_sea_level(self, level):
		self.sea_level = level

	def return_country(self):
		return self.country

	def return_city(self):
		return self.city

	def return_latitude(self):
		return self.latitude

	def return_longitude(self):
		return self.longitude


