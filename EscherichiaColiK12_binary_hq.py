#!/usr/bin/env python
# coding: utf-8

# In[49]:


import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("EscherichiaColiK12_binary_hq.txt",sep="\t",usecols=["Gene_A","Gene_B"])


# In[50]:


G=nx.from_pandas_edgelist(df,"Gene_A","Gene_B",create_using=nx.DiGraph())


# In[51]:


degrees=dict(G.degree())
order=sorted(degrees.items(),key=lambda t:t[1])
x,y=zip(*order)
plt.plot(x,y)
plt.show()


# In[52]:


from collections import Counter
degree_sequence = [G.degree(n) for n in G.nodes]
degree_counts = Counter(degree_sequence)
min_degree, max_degree = min(degree_counts.keys()), max(degree_counts.keys())
plt.xlabel("Degree", fontsize=20)
plt.ylabel("Frequancy", fontsize=20)
plot_x = list(range(min_degree, max_degree + 1))
plot_y = [degree_counts.get(x, 0) for x in plot_x]
plt.bar(plot_x, plot_y)


# In[53]:


import math
def plot_degree_dist(G):
    
    degrees = G.degree()
    degrees = dict(degrees)
    values = sorted(set(degrees.values()))
   
    histo = [list(degrees.values()).count(x) for x in values]
    P_k = [x / G.order() for x in histo]
   
    
    plt.figure()
    plt.bar(values, P_k)
    plt.xlabel("k",fontsize=20)
    plt.ylabel("p(k)", fontsize=20)
    plt.title("Degree Distribution", fontsize=20)
    
    plt.show()
    plt.figure()
    plt.grid(False)
    plt.loglog(values, P_k, "bo")
    plt.xlabel("k", fontsize=20)
    plt.ylabel("log p(k)", fontsize=20)
    plt.title("log Degree Distribution")
    plt.show()
    plt.show()  


# In[54]:


plot_degree_dist(G)


# In[56]:


def degree_distribution(G):
    vk = dict(G.degree())
    vk = list(vk.values()) 
    maxk = np.max(vk)
    mink = np.min(min)
    kvalues= arange(0,maxk+1) 
    Pk = np.zeros(maxk+1) 
    for k in vk:
        Pk[k] = Pk[k] + 1
    Pk = Pk/sum(Pk)
    return kvalues,Pk


# In[57]:


from numpy  import *
import numpy as np
ks, Pk = degree_distribution(G)


# In[58]:


plt.figure()
plt.bar(ks,Pk)
plt.xlabel("k", fontsize=20)
plt.ylabel("P(k)", fontsize=20)
plt.title("Degree distribution", fontsize=20)
plt.savefig('degree_dist.eps')  
plt.show(True)
plt.figure()
plt.loglog(ks,Pk,'bo')
plt.xlabel("k", fontsize=20)
plt.ylabel("log P(k)", fontsize=20)
plt.title("Degree distribution", fontsize=20)
plt.savefig('degree_dist.eps')  
plt.show(True)

