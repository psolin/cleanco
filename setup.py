#!/usr/bin/env python

import setuptools

from setuptools import setup

setup(name='cleanco',
      description='Python library to process company names',
      version='2.0',
      license="MIT",
      classifiers = [
         "Topic :: Office/Business",
         "Development Status :: 4 - Beta",
         "Intended Audience :: Developers",
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python :: 3"
      ],
      url='https://github.com/psolin/cleanco',
      author='Paul Solin',
      author_email='paul@paulsolin.com',
      packages=["cleanco"],
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'tox'],
)
