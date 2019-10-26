from setuptools import setup

setup(
    name = 'mkjunk',
    version = '1.0.0',
    packages = ['mkjunk'],
    install_requires = [
        'humanfriendly >= 4.8',
        'click > 6.7'
    ],
    entry_points = {
        'console_scripts': [
            'mkjunk = mkjunk.__main__:main'
        ]
    })
