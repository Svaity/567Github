import requests
import json
import re
import unittest

def gb(ID):
	a = requests.get("https://api.github.com/users/" + ID + "/repos")
	repo_list = []
	for i in a:
		i = str(i)
		j = i.split(",")
		for i in j:
			if "full_name" in i:
				start = i.find("/")
				repo_list.append(i[start + 1:-1])

	for i in repo_list:
		i = i.strip('"')
		commit = 0
		a = requests.get("https://api.github.com/repos/" + ID + "/" + i + "/commits")
		for j in a:
			j = str(j)
			if '"commit":' in j:
				commit += 1
		yield ("Repo: " + i + " commit: " + str(commit) + ".")

def main():
	"""Please enetr a name"""
	ID = "vaityshrey"
	if len(list(gb(ID))) is 0:
		print("Wromg input or empty repo")
	print(list(gb(ID)))


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
	main()
	unittest.main(exit=False, verbosity=2)