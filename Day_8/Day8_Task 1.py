#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')
C:\Users\rajes\OneDrive\Desktop\Task 2 eda


# In[2]:


df = pd.read_csv(R'C:\Users\rajes\Downloads\data.csv')


# In[3]:


df


# <h1>Descriptive Statistics and Python Implementation<hi>

# <h2>Mean</h2>
#     <p>The mean (average) of a data set is found by adding all numbers in the data set and then dividing by the number of values in the set</p>

# $$\mu = \sum_{i=1}^{N} \frac {x{i}} {N}$$

# In[4]:



count = 0
sum = 0
for x in df['Mthly_HH_Income']:
    count +=1
    sum = sum+x
Mean = sum/count
print("Mean of Mthly_HH_Income is", Mean)


# In[5]:


def mean():

    count = 0
    sum = 0
    for x in df[input()]:
        count +=1
        sum = sum+x
    Mean = sum/count
    return print("Mean : {}".format(Mean))


# <h2>Median</h2>
#  <p>The median is the middle number in a sorted, ascending or descending, list of numbers and can be more descriptive of that data set than the average.<br> The median is sometimes used as opposed to the mean when there are outliers in the sequence that might skew the average of the values.<p>
#     
# * when n is odd $$ median = \frac{n+1} 2$$<br><br>
# * when n is even $$ median = \frac{1}{2}\left\{\frac{n}{2}+  \left( \frac{n}{2} + 1  \right) \right\} $$
# 
#  

# In[6]:


a= []
count = 0
for x in df[input()].sort_values():
    a.append(x)
    count += 1

if count %2 == 0:
    position1  = int(count/2)
    position2 = int(((count)/2)+1)
    median = (a[position1]+a[position2])/2
    print(median)
else:
    position = int((count+1)/2)
    print(a[position])


# ## Mode
# 
# In statistics, the mode is the most commonly observed value in a set of data. For the normal distribution, the mode is also the same value as the mean and median. In many cases, the modal value will differ from the average value in the data

# In[9]:


l1 = [] 
  
i = 0
while i < len(a) : 
    l1.append(a.count(a[i])) 
    i += 1
d1 = dict(zip(a,l1))   
d2={k for (k,v) in d1.items() if v == max(l1) } 
  
print("Mode(s) is/are :" + str(d2))


# ## variance
# 
# In probability theory and statistics, variance is the expectation of the squared deviation of a random variable from its mean. Informally, it measures how far a set of numbers is spread out from their average value
# 
# $$ \sigma^2 = \frac {1}{N}\sum_{i=1}^{N} ({x{i}-\mu})^2     $$
# 
# 

# In[45]:


n= len(results)
sum=0
for i in range(n):
    sum = sum+ results[i]
mean=sum/n


#  calculate the central moment
sum2=0
for i in range(n):
    sum2=sum2+ (results[i]-mean)**2

myvar=sum2/n
print( "variance: ", myvar)


# ## Standard Deviation
# 
# Standard deviation is the measure of dispersion of a set of data from its mean.
# It measures the absolute variability of a distribution; the higher the dispersion or variability, the greater is the standard deviation and greater will be the magnitude of the deviation of the value from their mean.
# 
# 
# $$   \sigma = \sqrt{variance}  $$

# In[51]:


import math
std_div = math.sqrt(myvar)
std_div


# ## Correlation
# 
# Correlation is a term that is a measure of the strength of a linear relationship between two quantitative variables. This post will define positive and negative correlations
# 
# Positive correlation is a relationship between two variables in which both variables move in the same direction. This is when one variable increases while the other increases and visa versa. Whilst negative correlation is a relationship where one variable increases as the other decreases, and vice versa.
# 
# $$r =\frac{\sum\left(x_{i}-\bar{x}\right)\left(y_{i}-\bar{y}\right)}{\sqrt{\sum\left(x_{i}-\bar{x}\right)^{2} \sum\left(y_{i}-\bar{y}\right)^{2}}}$$
# 
# 

# In[54]:


for i in df.columns:
    for j in df.columns:
        if (df[i].dtypes!='O') and (df[j].dtypes!='O'):
            x=np.corrcoef(df[i],df[j])[0,1]
        print("c of ",i,'and ',j,x)


# In[ ]:





# In[ ]:





# ## Normal Distribution
# 
# Normal distribution, also known as the Gaussian distribution, is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean.
# In graph form, normal distribution will appear as a bell curve.
# 
# $$f(x)= {\frac{1}{\sigma\sqrt{2\pi}}}e^{- {\frac {1}{2}} (\frac {x-\mu}{\sigma})^2}$$
# 
# $$f(x)	=	probability density function$$
# $$\sigma	=	standard deviation$$
# $$\mu	=	mean$$

# In[ ]:





# In[ ]:





# 
# ## Feature of Normal Distribution
# ### 1. It is symmetric
# A normal distribution comes with a perfectly symmetrical shape. This means that the distribution curve can be divided in the middle to produce two equal halves. The symmetric shape occurs when one-half of the observations fall on each side of the curve.
# 
#  
# 
# ### 2. The mean, median, and mode are equal
# The middle point of a normal distribution is the point with the maximum frequency, which means that it possesses the most observations of the variable. The midpoint is also the point where these three measures fall. The measures are usually equal in a perfectly (normal) distribution.
# 
#  
# 
# ### 3. Empirical rule
# In normally distributed data, there is a constant proportion of distance lying under the curve between the mean and specific number of standard deviations from the mean. For example, 68.25% of all cases fall within +/- one standard deviation from the mean. 95% of all cases fall within +/- two standard deviations from the mean, while 99% of all cases fall within +/- three standard deviations from the mean.
# 
#  
# 
# ### 4. Skewness and kurtosis
# Skewness and kurtosis are coefficients that measure how different a distribution is from a normal distribution. Skewness measures the symmetry of a normal distribution while kurtosis measures the thickness of the tail ends relative to the tails of a normal distribution.

# In[ ]:





# ## Positively Skewed & Negatively Skewed Normal Distribution
# 
# #### Skewed Left (Negative Skew)
# A left skewed distribution is sometimes called a negatively skewed distribution because it’s long tail is on the negative direction on a number line.
# 
# 
# 
# A common misconception is that the peak of distribution is what defines “peakness.” In other words, a peak that tends to the left is left skewed distribution. This is incorrect. There are two main things that make a distribution skewed left:
# 
# The mean is to the left of the peak. This is the main definition behind “skewness”, which is technically a measure of the distribution of values around the mean.
# The tail is longer on the left.
# In most cases, the mean is to the left of the median. This isn’t a reliable test for skewness though, as some distributions (i.e. many multimodal distributions) violate this rule. You should think of this as a “general idea” kind of rule, and not a set-in-stone one.
# 
# <p><a href="https://towardsdatascience.com/skewed-data-a-problem-to-your-statistical-model-9a6b5bb74e37"><img src="https://miro.medium.com/max/1152/1*zMSuf2Y_DFjdQzMrKU-oGQ.jpeg" alt="Alt Text" title="Positively Skewed & Negatively Skewed Normal Distribution"></a></p>
# 
# 
# #### Right Skewed or Postive Skewed
# So, the distribution which is right skewed have a long tail that extends to the right or positive side of the x axis.
# 
# - mean greater than the mode
# - median greater than the mode
# - mean greater than median
# - The first and second always hold in case of right skewed distribution but third one may not be valid sometimes.

# ## Effect on Mean, Median and Mode due to Skewness
# 
# - In a positively skewed distribution
# the outliers will be pulling the mean down the scale a great deal. The median might be
# slightly lower due to the outlier, but the mode will be unaffected. Thus, with a negatively
# skewed distribution the mean is numerically lower than the median or mode
