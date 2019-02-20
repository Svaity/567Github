import unittest
from github567 import gb
import requests
class Testgh(unittest.TestCase):
	def test_normal(self):
		self.assertEqual(list(gb("vaityshrey")), ['Repo: androcrew commit: 0.'])
		# used friends github id for testcase below
		self.assertEqual(list(gb("AdityaMunot")), ['Repo: Anagram-Variety commit: 12.', 'Repo: RepoFetch commit: 14.',
												   'Repo: full_name": commit: 0.',
												   'Repo: SSW-555-Group-Project commit: 13.',
												   'Repo: full_name":"AdityaMuno commit: 0.',
												   'Repo: Triangle567 commit: 6.'])
		# name not available
		self.assertEqual(list(gb("hasdgfjas")), [])

if __name__ == '__main__':
	print('Running unit tests')
	unittest.main()
