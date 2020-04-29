#libraries
import seaborn as sns


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
