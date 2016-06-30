#!/usr/bin/env python

import setuptools

from setuptools import setup

setup(name='cleanco',
      description='Python library to process company names',
      version='1.36',
      license="MIT",
      classifiers = [
         "Topic :: Office/Business",
         "Development Status :: 4 - Beta",
         "Intended Audience :: Developers",
         "License :: OSI Approved :: MIT License",
      ],
      url='https://github.com/psolin/cleanco',
      author='Paul Solin',
      author_email='paul@paulsolin.com',
      py_modules=['cleanco', 'termdata'],
      )
