#!/usr/bin/env python
# coding: utf-8

# In[24]:


import networkx as nx


# In[25]:


g =nx.Graph()


# In[26]:


g.add_nodes_from(['a','b','c','d','e'])


# In[27]:


g.add_edges_from([('a','c'),('c','d'),('b','d'),('c','e')])


# In[28]:


nx.draw(g,with_labels=True,node_color='red',node_size=2000,font_size=20,font_color='white')


# In[29]:


g.nodes()


# In[30]:


g.edges()


# In[31]:


g.number_of_nodes()


# In[32]:


g.number_of_edges()


# In[33]:


for i in g.neighbors('a'):
    print(i)


# In[34]:


g.has_node('a')


# In[35]:


g.has_edge('a','d')


# In[36]:


list(g.neighbors('a'))


# In[37]:


nx.is_tree(g)


# In[38]:


nx.is_connected(g)


# In[39]:


g.degree('a')


# In[40]:


d=nx.DiGraph()


# In[41]:


d.add_edges_from([('a','c'),('c','d'),('b','d'),('c','e')])


# In[42]:


nx.is_tree(d)


# In[43]:


nx.draw(d,with_labels=True,node_color='red',node_size=2000,font_size=20,font_color='white')

