#!/usr/bin/env python
# coding: utf-8

# In[39]:


import networkx as nx


# In[40]:


G=nx.Graph()
G.add_edges_from([(1,2),(2,3),(1,3),(3,4)])
nx.draw(G,with_labels=True,node_size=2000)


# In[41]:


dict(G.degree())


# In[42]:


nx.to_numpy_matrix(G)


# In[43]:


graph=nx.read_edgelist('Alaa.txt',nodetype=str,create_using=nx.DiGraph())


# In[44]:


nx.draw(graph,with_labels=True,node_size=2000)


# In[45]:


import pandas as pd


# In[46]:


df=pd.read_csv('HomoSapiens_binary_hq (1).txt',nrows=100,sep='\t'
              ,usecols=['Gene_A','Gene_B'])


# In[47]:


df


# In[48]:


G=nx.from_pandas_edgelist(df,'Gene_A','Gene_B',create_using=nx.DiGraph())


# In[49]:


nx.draw(G,with_labels=True)


# In[50]:


import matplotlib.pyplot as plt


# In[51]:


degrees=dict(G.degree)
order=sorted(degrees.items(),key=lambda t :t[1])


# In[52]:


x,y=zip(*order)
plt.plot(x,y)
plt.show()


# In[53]:


import pandas as pd
df=pd.read_csv('SaccharomycesCerevisiaeS288C_binary_hq (1).txt',nrows=100,sep='\t'
              ,usecols=['Uniprot_A','Uniprot_B'])
G=nx.from_pandas_edgelist(df,'Uniprot_A','Uniprot_B',create_using=nx.DiGraph())
nx.draw(G,with_labels=True)


# In[54]:


nx.to_numpy_matrix(G)


# In[55]:


de=dict(G.degree)
sorted(de.items(), key=lambda  t :t[1])

