#!/usr/bin/env python
# coding: utf-8

# In[1]:


# making tress from python list 
# this is a binary tree,
# the idea is to use python tree data structure to represent a trivial binary tree structure 


# In[2]:


def binary_tree(r):
    '''
    a function that accepts a root and return a binary tree
    '''
    return [r, [], []]


# In[9]:


def insert_left(root, newbranch):
    '''
    a function to insert new brach to the tree left part
    '''
    target_node = root.pop(1)
    
    if (len(target_node) > 1):
        root.insert(1, [newbranch, target_node, []])
    else:
        root.insert(1, [newbranch, [], []])
    return root
    


# In[10]:


def insert_right(root, newbranch):
    target_node = root.pop(2)
    
    if (len(target_node) > 1):
        root.insert(2, [newbranch, [], target_node])
    else:
        root.insert(2, [newbranch, [], []])


# In[11]:


def getroot(tree):
    return tree[0]


# In[13]:


def set_root_value(tree, value):
    tree[0] = value
    return tree[0]


# In[14]:


def get_left_value(tree):
    return tree[1]


# In[15]:


def get_right_value(tree):
    return tree[2]

