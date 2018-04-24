#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:42:29 2018

@author: uvionics
"""
import csv
from prettytable import from_csv

class check:
    def name(self):
        """Returns the file name."""
        return self.__name

    def summary(filename):
        with open(filename,"r") as f:
            x=from_csv(f)
        print x
        return x
