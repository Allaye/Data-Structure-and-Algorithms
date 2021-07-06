#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


# In[22]:


class DoublyLinkedList:
    
    def __init__(self):
        self.head = Node()
        
    def append(self, data):
        new_node = Node(data)
        cur = self.head
        print(cur)
        print(self.head)
        cur = 10
        print(cur)
        print(self.head)
        if(cur.data is None):
            print('head')
            cur = new_node
            return
        while(cur.next != None):
            cur = cur.next
        new_node.prev = cur
        new_node.next = None
        cur.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        if(cur is None):
            cur = new_node
            return
            
    def erase(self, index):
        pass
    
    def length(self):
        pass
    
    def display(self, display='P'):
        if(self.head.data is None):
            return None
        enum, cur = [], self.head
        while(cur.next is not None):
            cur = cur.next
            enum.append(cur.data)
        if(display=='P'): print(enum)
        else: return enum
        
    
    def get(self, index):
        pass
    

