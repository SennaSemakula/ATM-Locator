import unittest
from location import Location

class TestLocation(unittest.TestCase):
	def setUp(self):
		self.location = Location('united kingdom', 'croydon')


	def test_set_latitude(self):
		lat = self.location.set_latitude(-0.100594)

		self.assertEqual(-0.100594, self.location.return_latitude())

	def test_set_longitude(self):
		longitude = self.location.set_longitude(51.376495)

		self.assertEqual(51.376495, self.location.return_longitude())

	def test_sea_level(self):
		sea_level = self.location.set_sea_level('85m')

		self.assertEqual('85m', self.location.return_sea_level())

	



unittest.main()
