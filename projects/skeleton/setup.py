try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My Project',
	'author': 'Stephen Andrews',
	'url': 'URL to get it at.',
	'download_URL': 'Where to download it',
	'author_email': 'andrews.stephen.7734@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts':[],
	'name': 'projectname'
	}
	
setup(**config)