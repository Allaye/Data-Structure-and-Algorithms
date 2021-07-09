#!/usr/bin/env python
# coding: utf-8

# In[2]:


def check_cycle(node):
    '''
    check if current node next node points to imediate past node
    '''
    cur_node = node
    if(cur_node.next == None):
        return
    while(True):
        temp = cur_node
        cur_node = cur_node.next
        if(cur_node.next == temp):
            return True
        elif(cur_node.next == None):
            return False

