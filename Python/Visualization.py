#libraries
import seaborn as sns
import matplotlib.pyplot as plot

#
##
###
####STRUCTURE BASIC TO PLOT
fig = plt.figure(); ax = fig.add_subplot(1, 1, 1)  #SETTING PLOT
ax.plot(randn(1000).cumsum(), 'k', label='one', color='r')# PLOT1
ax.plot(randn(1000).cumsum(), 'k--', label='two', color= 'b')#PLOT2
ax.plot(randn(1000).cumsum(), 'k.', label='three', color='g')#PLOT 3
ax.set_title('My first matplotlib plot') #TITLE
ax.legend(loc='best')#LENGEND
ax.set_xlabel('Stages')#LABEL X

#
##
###
#####plot correlation from dataset
f,ax = plt.subplots(figsize=(12,12))
sns.heatmap(df.corr(method='spearman'),annot=True,fmt=".1f",linewidths=1,ax=ax)
plt.show()
##
###Histogram with curve of density
sns.distplot(train['Age'], hist=True, kde=True, bins=int(180/5), color = 'darkblue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})
#Boxplot, very useful to see outliers
#boxplot
sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
ax = sns.boxplot(x=train["Age"])

