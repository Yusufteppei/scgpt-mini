#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import scanpy as sc


# In[3]:


special_tokens = ['<PAD>', '<CLS>', '<MASK>']


# ## GENES VOCAB GENERATOR


# In[6]:


adata = sc.datasets.pbmc3k()
with open("data/gene-id-vocab.json", "w") as f:
    gene_ids_ = dict( enumerate(list(adata.var['gene_ids']) + special_tokens ))
    gene_ids = dict([ i[::-1] for i in gene_ids_.items() ])
    json.dump(gene_ids, f)


# In[10]:


#special_tokens + list(adata.var['gene_ids'])


# ## CONDITIONS VOCAB GENERATOR

# In[11]:

"""
with open("condition-vocab.json", "w") as f:
    conditions = ["sick", "healthy"]
    conditions_ = enumerate(conditions)
   
    conditions = dict([ i[::-1] for i in conditions_ ])

    json.dump(conditions, f)
    
"""
