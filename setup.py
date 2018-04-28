#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: uvionics
"""

from setuptools import setup

setup(name="citta",
      version="1.01",
      packages=["citta"],
      description='a data science pip installable package for ocean protocol, under-development by citta',
      license='MIT',
      author='Citta Analytics',
      author_email='sooraj.sudhakaran@citta.ai',
      url='https://github.com/sooraj-citta/ocean-python-lib',
      install_requires=['easygui','Prettytable','pandas','numpy']
)
