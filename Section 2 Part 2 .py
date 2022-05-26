#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cobra


# In[2]:


from cobra import Model,Reaction,Metabolite


# In[3]:


model=Model('model_task')


# In[4]:


v0=Reaction('v0')
v0.name='v0'
v0.lower_bound=1
v0.upper_bound=1


# In[5]:


v1=Reaction('v1')
v1.name='v1'
v1.lower_bound=0
v1.upper_bound=1000


# In[6]:


v2=Reaction('v2')
v2.name='v2'
v2.lower_bound=0
v2.upper_bound=1000


# In[7]:


M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000


# In[8]:


glc=Metabolite('glc',compartment='c')
AA=Metabolite('AA',compartment='c')
Biomass=Metabolite('Biomass',compartment='c')


# In[9]:


v0.add_metabolites({glc:1})


# In[10]:


v1.add_metabolites({glc:-1,AA:1})


# In[11]:


v2.add_metabolites({AA:-9.09,Biomass:1})


# In[12]:


M.add_metabolites({Biomass:-1})


# In[13]:


model.add_reactions([v0,v1,v2,M])


# In[14]:


model.objective='M'


# In[15]:


model.optimize()


# In[16]:


model.summary()


# In[17]:


cobra.io.save_json_model(model,"test2.json")


# In[18]:


import escher


# In[19]:


from escher import Builder


# In[20]:


builder=Builder()


# In[21]:


builder


# In[ ]:




