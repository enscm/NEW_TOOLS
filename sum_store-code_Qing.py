#! /usr/bin/python

import numpy as np
import pandas as pd

df = pd.read_csv("XUECHENGRONG.csv")

df['sum_of_Service_Fee'] = df.groupby(['Store Code'])['Service Fee'].transform('sum')
df2 = df.drop_duplicates(subset=['Store Code'])
df2.to_csv("summed_data.csv")
