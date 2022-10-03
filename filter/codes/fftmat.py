#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


#def rectification(A):
 #   for i in range(0,len(A))


# In[4]:


def I(N):
    return np.identity(N)


# In[5]:


def w(N):
    return np.exp(-1j*2*np.pi/N)


# In[6]:


def D(N):
    list=[]
    for i in range(0,N):
        list.append(pow(w(2*N),i))
    return np.diag(list)


# In[7]:


def e(k,N):
    e=np.zeros([N,len(k)])
    for i in range(0,len(k)):
                e[k[i]-1,i]=1
    return e
e([2,4],4)


# In[8]:


def P(N):
    evenlist=[]
    oddlist=[]
    for i in range(1,N+1):
        if(i%2==0):
            oddlist.append(int(i))
        else:
            evenlist.append(int(i))
        print(evenlist,oddlist)
    return np.concatenate((e(evenlist,int(N)),e(oddlist,int(N))),axis=1)
P(4)


# In[9]:


def F(N):
    if N==1:
        return np.ones(1)
    else:
        A1=np.concatenate((I(int(N/2)),D(int(N/2))),axis=1)
        A2=np.concatenate((I(int(N/2)),-D(int(N/2))),axis=1)
        A=np.concatenate((A1,A2))
        if N==2:
            B1=np.array(1,0)
            B2=np.array(0,1)
        else:
            B1=np.concatenate((F(int(N/2)),np.zeros(((int(N/2),int(N/2)),dtype=int))),axis=1)
            B2=np.concatenate(((np.zeros(((int(N/2),int(N/2))),dtype=int),(F(int(N/2))))),axis=1)
        B=np.concatenate((B1,B2))
        A=np.matmul(A,B)
        A=np.matmul(A,P(N))
        return A


# In[ ]:


F(int(4))

