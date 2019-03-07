from github567 import *
from unittest import mock


def changed_links(url):
	if url == 'https://api.github.com/users/svaity/repos':
		return call('repos.json')
	elif url == "https://api.github.com/repos/svaity/567Github/commits":
		return call('ShreyCommits567Github.json')
	elif url == "https://api.github.com/repos/svaity/Data-Visualization-Based-on-Emails-Day-From-Log/commits":
		return call('ShreyCommitsData-Visualization-Based-on-Emails-Day-Fr.json')
	elif url == "https://api.github.com/repos/svaity/Distance-Calculator-Using-Web-APIs-JSON/commits":
		return call('ShreyCommitsDi.json')
	elif url == "https://api.github.com/repos/svaity/Ecommerce-Framwork/commits":
		return call('ShreyCommitsEcommerce-Framwork.json')
	elif url == "https://api.github.com/repos/svaity/PHP-Login-System/commits":
		return call('ShreyCommitsPHP-Login-System.json')
	elif url == "https://api.github.com/repos/svaity/Portfolio-using-Django-Postgres/commits":
		return call('ShreyCommitsPortfolio-using-Django-Postgres.json')
	elif url == "https://api.github.com/repos/svaity/Reduce-Noise-in-LiDAR-sensor/commits":
		return call('ShreyCommitsReduce-Noise-in-LiDAR-sensor.json')
	elif url == "https://api.github.com/repos/svaity/Stevens_Repository/commits":
		return call('ShreyCommitsStevens_Repository.json')
	elif url == "https://api.github.com/repos/svaity/Travel_Guide-UI-Wireframe-/commits":
		return call('ShreyCommitsTravel_Guide-UI-Wirefram.json')
	elif url == "https://api.github.com/repos/svaity/Triangle567/commits":
		return call('ShreyCommitsTriangle567.json')


def call(path):
	with open(path) as f:
		return Response(f.read())


class Response:
	def __init__(self, content):
		self.content = content

	def json(self):
		return json.loads(self.content)


class testrepos(unittest.TestCase):
	@mock.patch('requests.get')
	def testrepos(self, mocked_request):
		mocked_request.side_effect = changed_links
		self.assertEqual(list(gb("svaity")),
						 [('567Github', 15), ('Data-Visualization-Based-on-Emails-Day-From-Log', 2), ('Distance-Calculator-Using-Web-APIs-JSON', 2), ('Ecommerce-Framwork', 15), ('PHP-Login-System', 4), ('Portfolio-using-Django-Postgres', 5), ('Reduce-Noise-in-LiDAR-sensor', 8), \
						  ('Stevens_Repository', 7), ('Travel_Guide-UI-Wireframe-', 2), ('Triangle567', 8)])


if __name__ == '__main__':
	unittest.main(exit=False, verbosity=2)
