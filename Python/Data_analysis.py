#libraries 
from numpy import  mean 
from numpy import std
from scipy.stats import norm

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

####OUTLIERS
##
##
###
####
#Method traditional ( with desviation standard) 
# Identify outliers
train_mean, train_std = mean(train['Age']), std(train['Age'])
# calculate desviation standart with value 3 for take only values very extrem
cut_off = train_std * 3
lower, upper = train_mean - cut_off, train_mean + cut_off
# identify outliers
outliers = [x for x in train['Age'] if x < lower or x > upper]
outliers_removed = [x for x in train['Age'] if x > lower and x < upper]
print('lower:' , lower, '   upper:', upper)
print(' No outliers:', len(outliers_removed),'\n outliers: ', len(outliers))
#
## identify outlier with calculate interquartile range
from numpy import percentile
q25, q75 = percentile(train['Age'], 25), percentile(train['Age'], 75)
iqr = q75 - q25
# calculate the outlier cutoff
cut_off = (iqr) * 3
lower_1, upper_1 = q25 - cut_off, q75 + cut_off
outliers_1 = [x for x in train['Age']if x < lower_1 or x > upper_1]
outliers_removed_1 = [x for x in train['Age'] if x > lower_1 and x < upper_1]
print('lower:' , lower_1, '   upper:', upper_1)
print(' No outliers:', len(outliers_removed_1),'\n outliers: ', len(outliers_1))

#remove outliers
#  here I used method of interquartile range  
train = train.drop(train[(train['Age'] > upper_1) | (train['Age'] < lower_1)].index)
print('Number of Instances after outliers removal: {}'.format(len(train)))
