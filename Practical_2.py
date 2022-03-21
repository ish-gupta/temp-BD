# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 10:44:06 2022

@author: arund
"""
#MAP REDUCE

import sys
import os
import pandas as pd

def reducer(words):
    count = {}
    for i in words:
        count[i] = count.get(i, 0)+1 
    return count

def mapper(filename):
    try:
        f = open(filename, "r")
    except:
        print('Check File name')
        quit()
        
    lines= [line.strip().split() for line in f.readlines()] 
    words = [j.lower() for i in lines for j in i]  
    
    count = reducer(words)
    
    return pd.DataFrame.from_dict(count, orient ='index', columns=['Count'])

print(mapper(input('Filename : ')))