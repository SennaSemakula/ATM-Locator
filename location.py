#Class that stores all the location details of an ATM
class Location():

	def __init__(self, country, city):
		self.country = country.title()
		self.city = city.title()
		self.latitude = 0
		self.longitude = 0
		self.sea_level = 0

	def set_latitude(self, latitude):
		try:
			val = int(latitude)
		except: 
			print("Please insert an integer for latitude!")	
		else:
			self.latitude = latitude

	def set_longitude(self, longitude):
		try:
			val = int(longitude)
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

	def return_sea_level(self):
		return self.sea_level


