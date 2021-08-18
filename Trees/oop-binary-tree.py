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
        '''
        insert new node into the tree, check if the current node is empty or not and proceed
        '''
        if (self.left_node == None):
            self.left_node = BinaryTree(new_node)
        else:
            bt = BinaryTree(new_node)
            bt.left_node = self.left_node
            self.left_node = bt
    
    def insert_right_node(self, new_node):
        '''
        inser new node to the right side of the tree, check if the node is empty or not and proceed
        '''
        if (self.right_node == None):
            self.right_node = BinaryTree(new_node)
        else:
            bt = BinaryTree(new_node)
            bt.right_node = self.right_node
            self.right_node = bt
    
    def get_right_node(self):
        '''
        return the values of the right side of the tree, beware, 
        you will be getting memory addresses most of the time
        '''
        return self.right_node
    
    def get_left_node(self):
        '''
        return the values of the right side of the tree, beware, 
        you will be getting memory addresses most of the time
        '''
        return self.left_node
    
    def set_root(self, value):
        '''
        set the parent root value of the tree
        '''
        self.root = value
        
    def get_root(self):
        '''
        return the root of the root of the tree
        '''
        return self.root
    
    def preorder(self):
        
        print(self.root)
        if (self.left_node):
            self.left_node.preorder()
        elif (self.right_node):
            self.right_node.preorder()
            
    def postorder(self):
        
        if (self.left_node):
            #self.left_node.postorder()
        elif (self.right_node):
            self.right_node.postorder()
        print(self.root)

    
        

