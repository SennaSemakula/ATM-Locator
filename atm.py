"""Class to simulate ATM's"""
from location import Location
class ATM():

	def __init__(self, bank, location, chargeable=False):
		self.chargeable = chargeable
		self.bank = bank
		self.location = location

	def atm_details(self):
		location = self.location
		print(self.location.return_latitude)
		print("ATM details are as follows: ")
		print("Location: " + "\n\tLatitude: " + str(location.return_latitude()) +
			"\n\tLongitude: " + str(location.return_longitude()) + 
			"\n\tCountry: " + str(location.return_country()) + 
			"\n\tCity: " + str(location.return_city()) + "\n" +
			"\n" + self.charge_details()) 

	def charge_details(self):
		if self.chargeable:
			charge_text =  "This ATM is not chargeable"
		else:
			charge_text =  "Unfortunately, you'll have to pay a withdrawal fee to use this ATM"

		return charge_text


croydon_coord = {'latitude': -0.100594, 'longitude': 51.376495}
croydon_loc = Location('united kingdom', 'london', croydon_coord['latitude'], croydon_coord['longitude'], '85m')
croydon_atm = ATM('Barclays', croydon_loc)

croydon_atm.atm_details()
