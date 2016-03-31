import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "patelib",
    version = "0.0.1",
    author = "Maharsh Patel",
    author_email = "maharsh@live.ca",
    description = ("A Library of Useful Stuff "),
    license = "MIT",
    keywords = "maharsh patel library",
    url = "https://github.com/maharshmellow/patelib",
    packages=['numbers', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
    ],
)
