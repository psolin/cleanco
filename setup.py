#!/usr/bin/env python

from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='cleanco',
      description='Python library to process company names',
      long_description=long_description,
      long_description_content_type='text/markdown',
      version='2.3',
      license="MIT",
      license_files=('LICENSE.txt',),
      classifiers=[
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
