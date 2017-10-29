
# coding: utf-8

# In[5]:


import numpy as np
from timeit import default_timer as timer
from numbapro import vectorize


# In[2]:


"""
def vectorAdd(a, b, c):
    for i in range(a.size):
        c[i] = a[i] + b[i]
"""


# In[2]:


@vectorize([float32, float32], target='gpu')
def vectorAdd(a, b):
    for i in range(a.size):
        return a + b


# In[3]:


def main():
    N = 32000000  # number of elements per Array
    
    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.zeros(N, dtype=np.float32)
    
    start = timer()
    C = vectorAdd(A, B)
    vectorAdd_time = timer() - start
    
    print("C[5] = " + str(C[5]))
    print("C[-5] = " + str(C[-5]))
    
    print("vectorAdd took %f seconds" % vectorAdd_time)


# In[4]:


if __name__ == "__main__":
    main()


# In[ ]:




