"""Class to simulate ATM's"""
from location import Location
class ATM():
	"""Class that stores properties of each ATM"""

	def __init__(self, bank, location, chargeable=False):
		self.chargeable = chargeable
		self.bank = bank
		self.location = location

	def atm_details(self):
		"""This method will print out the main details of the nearest ATM"""
		location = self.location
		print("ATM details are as follows: ")
		print("Location: " + "\n\tLatitude: " + str(location.return_latitude()) +
			"\n\tLongitude: " + str(location.return_longitude()) + 
			"\n\tCountry: " + str(location.return_country()) + 
			"\n\tCity: " + str(location.return_city()) +
			"\n\tSea Level: " + str(location.return_sea_level()) + "\n"
			"\n" + self.charge_details()) 

	def charge_details(self):
		"""Method to validate whether user is elligble for ATM charges"""
		if self.chargeable:
			charge_text =  "This ATM is not chargeable"
		else:
			charge_text =  "Unfortunately, you'll have to pay a withdrawal fee to use this ATM"

		return charge_text


croydon_coord = {'latitude': -0.100594, 'longitude': 51.376495, 'sea_level': '85m'}

croydon_loc = Location('united kingdom', 'london')
croydon_loc.set_latitude(croydon_coord['latitude'])
croydon_loc.set_longitude(croydon_coord['longitude'])
croydon_loc.set_sea_level(croydon_coord['sea_level'])


croydon_atm = ATM('Barclays', croydon_loc)

croydon_atm.atm_details()
