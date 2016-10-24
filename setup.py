from setuptools import setup, find_packages

with open('README') as f:
	readme = f.read()

with open('License') as f:
	license = f.read()

setup(
	name = 'Pedestrian simulator',
	version = '0.0.1',
	description = 'Package for cse 6730',
	long_description = readme,
	author = 'Yuying Liu, Sen Yang, Xiao Wang',
	author_email = 'xiaowang@gatech.edu',
	license = license,
	scripts = ['bin/simulation'],
	packages = find_packages(exclude=('tests','docs'))
)
