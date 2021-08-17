#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Binary tree implementation using OOP


# In[2]:


class BinaryTree:
    '''
    basic implementation of binary tree using oop concepts, 
    we have a root to start each tree
    each tree have a left node
    each tree have a right node
    
    '''
    def __init__(self, root):
        '''
        assign values to the root and both node 
        '''
        self.root = root
        self.left_node = None
        self.right_node = None 
    
    def insert_left_node(self, new_node):
        
        if (self.left_node == None):
            self.left_node = BinaryTree(new_node)
        else:
            bt = BinaryTree(new_node)
            bt.left_node = self.left_node
            self.left_node = bt
    
    def insert_right_node(self, new_node):
        
        if (self.right_node == None):
            self.right_node = BinaryTree(new_node)
        else:
            bt = BinaryTree(new_node)
            bt.right_node = self.right_node
            self.right_node = bt
    
    def get_right_node(self):
        return self.right_node
    
    def get_left_node(self):
        return self.left_node
    
    def set_node(self, value):
        self.root = value
        
    def get_root(self):
        return self.root



