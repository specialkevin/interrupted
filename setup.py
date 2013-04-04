import os
from setuptools import setup

setup(
    name = "interrupted",
    version = "0.0.1",
    author = "Kevin Harriss",
    author_email = "special.kevin@gmail.com",
    description = ("A command-line tool to track your interruptions via StatHat"),
    license = "BSD",
    keywords = "commandline",
    url = "http://github.com/specialkevin/interrupted",
    packages=['interrupted',],
    scripts=['bin/interrupted'],
    classifiers=[
                    "Development Status :: 2 - Pre-Alpha",
                    "Topic :: Utilities",
                    "License :: OSI Approved :: BSD License",
                ],
    install_requires = ['stathat>=0.0.3'],
    dependency_links = ['https://github.com/kennethreitz/stathat.py/tarball/master#egg=stathat-0.0.3']
)
