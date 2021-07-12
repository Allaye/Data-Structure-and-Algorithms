#!/usr/bin/env python
# coding: utf-8

# In[1]:


from linked_list import LinkedList

L = LinkedList(10)

def reverse(L):
    lenght = L.length()
    if(lenght == 0):
        raise IndexError('The list is an empty list, please append to the list and try reversing again')
        return 
    nodes, cur = [], L.head
    while(cur.next !=None):
        cur = cur.next
        nodes.append(cur)
    cur = L.head
    nodes.reverse()
    for node in nodes:
        cur = L.next = node
    return cur

