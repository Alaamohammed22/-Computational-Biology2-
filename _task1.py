#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cobra


# In[2]:


from cobra import Model,Reaction,Metabolite


# In[3]:


model=Model('first model')


# In[12]:


v0=Reaction('v0')
v0.name='v0'
v0.lower_bound=1
v0.upper_bound=1


# In[13]:


v1=Reaction('v1')
v1.name='V1'
v1.lower_bound=0
v1.upper_bound=1000


# In[14]:


v2=Reaction('v2')
v2.name='V2'
v2.lower_bound=0
v2.upper_bound=1000


# In[15]:


v3=Reaction('v3')
v3.name='v3'
v3.lower_bound=0.9
v3.upper_bound=0.9


# In[16]:


ATP_R=Reaction('ATP')
ATP_R.name='ATP'
ATP_R.lower_bound=0
ATP_R.upper_bound=1000


# In[17]:


M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000


# In[18]:


A=Metabolite('A',compartment='c')
B=Metabolite('B',compartment='c')
C=Metabolite('C',compartment='c')
ATP=Metabolite('ATP',compartment='c')


# In[19]:


v0.add_metabolites({A:1})


# In[20]:


v1.add_metabolites({A:-1,B:1})


# In[21]:


v2.add_metabolites({B:-1,C:1})


# In[22]:


v3.add_metabolites({ATP:-1})


# In[23]:


M.add_metabolites({C:-1})


# In[24]:


ATP_R.add_metabolites({A:-1,ATP:1})


# In[25]:


model.add_reactions([v0,v1,v2,v3,M,ATP_R])


# In[26]:


model.objective='M'


# In[27]:


model.optimize()


# In[ ]:




