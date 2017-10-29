
# coding: utf-8

# In[1]:


print('hello world')


# In[2]:




# In[3]:


import pylab
import numpy

x = numpy.linspace(-15,15,100) # 100 linearly spaced numbers
y = numpy.sin(x)/x # computing the values of sin(x)/x


# In[14]:


# compose plot
pylab.plot(x,y) # sin(x)/x
#pylab.plot(x,y,'co') # same function with cyan dots
for i in range(1, 20):
    pylab.plot(x,i*y) # 2*sin(x)/x and 3*sin(x)/x
pylab.show() # show the plot


# In[ ]:




