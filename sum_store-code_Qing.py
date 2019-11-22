#! /usr/bin/python

import numpy as np
import pandas as pd

df = pd.read_csv("file_to_sum.csv")

df['sum_new_col'] = df.groupby(['group_col_to_aime'])['targeted_to_sum_col'].transform('sum')
df2 = df.drop_duplicates(subset=['group_col_to_aime'])
df2.to_csv("summed_data.csv")
