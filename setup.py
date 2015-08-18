#!/usr/bin/env python

from distutils.core import setup
setup(name='cleanco',
      description='Python library to process company names',
      version='1.0',
      classifiers = [
         "Topic :: Office/Business",
         "Development Status :: 4 - Beta",
         "Intended Audience :: Developers"
      ],
      url='https://github.com/psolin/cleanco',
      author='Paul Solin',
      author_email='paul@paulsolin.com',
      py_modules=['cleanco', 'termdata'],
      )
