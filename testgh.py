import unittest
from github567 import gb

class Testgh(unittest.TestCase):
	def test_normal(self):
		self.assertEqual(list(gb("vaityshrey")), [('androcrew', 2)])
		# used friends github id for testcase below
		self.assertEqual(list(gb("svaity")), [('567Github', 15), ('Data-Visualization-Based-on-Emails-Day-From-Log', 4), ('Distance-Calculator-Using-Web-APIs-JSON', 3), ('Ecommerce-Framwork', 15), ('PHP-Login-System', 4), ('Portfolio-using-Django-Postgres', 5), ('Reduce-Noise-in-LiDAR-sensor', 8), ('Stevens_Repository', 7), ('Travel_Guide-UI-Wireframe-', 3), ('Triangle567', 8)])

if __name__ == '__main__':
	print('Running unit tests')
	unittest.main()
