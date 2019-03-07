
import requests
import json
import re
import unittest


def gb(ID):
	repos = requests.get("https://api.github.com/users/" + ID + "/repos").json()

	for repo in repos:
		commits = requests.get("https://api.github.com/repos/" + ID + "/" + repo['name'] + "/commits").json()
		yield repo['name'], len(commits)


def main():
	"""Please enter a name"""
	print(list(gb("svaity")))


def call_repo(url):
	if url == 'https://api.github.com/users/svaity/repos':
		return call('repos.json')


def call(path):
	with open(path, 'r') as f:
		data = json.load(f)
	return data


if __name__ == '__main__':
	main()
	unittest.main(exit=False, verbosity=2)