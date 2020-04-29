#libraries 
from numpy import  mean 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlibt.pyplot as plt


#
##
###
####
#####Separate column Sex in two columns of genders
df['female'] = df['Sex'] == 0
df['male'] = df['Sex'] == 1
#convert columns gender in values binary
df['male'] = df['male'].map(lambda x: 1 if x == True else 0)
df['female'] = df['female'].map(lambda x: 1 if x == True else 0)



