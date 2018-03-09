#!/usr/bin/env python2
try:
	from setuptools import setup
	import os
except ImportError:
	from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name='classical_cipher',
	version='1.1',
	author='15520599',
	author_email='15520599@gm.uit.edu.vn',
	description='Some script for classcial cipher like Caesar, Vigenere, Affine, etc.',
	long_description=read('README.md'),
	license='GPL2',
	keywords="python2 python2.7 classical-cipher",
	url='https://github.com/lzutao/classical_cipher',
	packages=['classical_cipher'], # same as @name
	zip_safe=False,
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Topic :: Utilities",
		"License :: OSI Approved :: GPL2 License",
	],
)
