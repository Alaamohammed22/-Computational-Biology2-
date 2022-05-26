#!/usr/bin/env python
# coding: utf-8

# In[47]:


from cobra import Model,Reaction,Metabolite


# In[48]:


import cobra


# In[49]:


model=Model('first_model')


# In[50]:


v1=Reaction('v1')
v1.name='v1'
v1.lower_bound=0
v1.upper_bound=1000


# In[51]:


v2=Reaction('v2')
v2.name='v2'
v2.lower_bound=0
v2.upper_bound=1000


# In[52]:


M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000


# In[53]:


v0=Reaction('v0')
v0.name='v0'
v0.lower_bound=1
v0.upper_bound=1


# In[54]:


v3=Reaction('v3')
v3.name='v3'
v3.lower_bound=.9
v3.upper_bound=.9


# In[55]:


v4=Reaction('v4')
v4.name='v4'
v4.lower_bound=0
v4.upper_bound=1000


# In[56]:


A=Metabolite('A',compartment='c')
B=Metabolite('B',compartment='c')
C=Metabolite('C',compartment='c')
ATP=Metabolite('ATP',compartment='c')


# In[57]:


v1.add_metabolites({A:-1,B:1})
v2.add_metabolites({B:-1,C:1})
v0.add_metabolites({A:1})
M.add_metabolites({C:-1})
v3.add_metabolites({A:-1,ATP:1})
v4.add_metabolites({ATP:-1})


# In[58]:


model.add_reactions([v0,v1,v2,v3,v4,M])


# In[59]:


model.objective='M'


# In[60]:


model.optimize()


# In[61]:


model.summary()


# In[62]:


cobra.io.save_json_model(model,"test.json")


# In[63]:


get_ipython().system('pip install escher')


# In[64]:


import escher


# In[65]:


from escher import Builder


# In[66]:


cobra.io.load_json_model("test.json")


# In[67]:


builder=Builder()


# In[68]:


builder


# In[ ]:




