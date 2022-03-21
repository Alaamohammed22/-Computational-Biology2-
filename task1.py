#!/usr/bin/env python
# coding: utf-8

# In[8]:


from cobra import Model,Reaction,Metabolite


# In[9]:


model=Model('First_model')


# In[10]:


r1=Reaction('r1')
r1.name='r1'
r1.lower_bound=0
r1.upper_bound=1000

r2=Reaction('r2')
r2.name='r2'
r2.lower_bound=0
r2.upper_bound=1000

M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000

r0=Reaction('r0')
r0.name='r0'
r0.lower_bound=1
r0.upper_bound=1


r3=Reaction('r3')
r3.name='r3'
r3.lower_bound=.9
r3.upper_bound=.9

r4=Reaction('r4')
r4.name='r4'
r4.lower_bound=0
r4.upper_bound=1000


# In[11]:


A=Metabolite('A',compartment='c')
B=Metabolite('B',compartment='c')
C=Metabolite('C',compartment='c')
ATP=Metabolite('ATP',compartment='c')

r1.add_metabolites({A:-1,B:1})
r2.add_metabolites({B:-1,C:1})
r0.add_metabolites({A:1})
M.add_metabolites({C:-1})
r3.add_metabolites({A:-1,ATP:1})
r4.add_metabolites({ATP:-1})

model.add_reactions([r0,r1,r2,r3,r4,M])

model.objective='M'

model.optimize()






