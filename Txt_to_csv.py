#! /usr/bin/python

##--------------------------------------------------------------------
##
##                code writen on 21 Nov. 2019, by Qing W
##                        qing.wang@outlook.fr
##
## Hint: This code can transfert a txt file (with white space to seprate
##       values) into csv file
##--------------------------------------------------------------------
##
##       \   ,__,
##        \  (oo)____
##           (__)    )\
##              ||--||
##
##--------------------------------------------------------------------


import numpy as np
import pandas as pd


###enter file name here###
data = pd.read_csv('file name', sep="\s+", header = 0)

## choose to modify/add header name 
#data.columns = ["a", "b", "c", "etc.","ettt"]

data.to_csv('new_file_name.csv',index=False)
