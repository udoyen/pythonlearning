try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = [
    'description': 'My Project',
    'author': 'george udosen',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it',
    'author': 'datameshprojects@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [],
    'name': 'projectname'
]


setup(**config)
