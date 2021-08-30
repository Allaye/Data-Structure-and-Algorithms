#!/usr/bin/env python
# coding: utf-8

# In[3]:


class BinaryHeap:
    
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0
        
    def perculate_up(self, node):
        
        while (node // 2):
            if (self.heaplist[node] < self.heaplist[node // 2]):
                tmp = self.heaplist[node // 2]
                self.heaplist[node // 2] = self.heaplist[node]
                self.heaplist[node] = tmp
            node = node // 2
            
    def insert(self, node):
        self.heaplist.append(node)
        self.currentsize = self.currentsize + 1
        self.perculate_up(self.currentsize)
        
    def perculate_down(self, node):
        
        while (node * 2) <= self.currentsize:
            mc = self.min_child(node)
            if self.heaplist[node] > self.heaplist[mc]:
                tmp = self.heaplist[node]
                self.heaplist[node] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            node = mc
    
    def min_child(self, node):
        if node * 2 + 1 > self.currentsize:
            return node * 2
        else:
            if self.heaplist[node*2] < self.heaplist[node*2+1]:
                return node * 2
            else:
                return node * 2 + 1
            
    def del_min(self):
        retval = self.heaplist[1]
        self.heaplist[i] = self.heaplist[self.currentsize]
        self.currentsize = self.currentsize - 1
        self.heaplist.pop()
        self.perculate_down(1)
        return retval
        
    def build_head(self, listofnode):
        i = len(listofnode) // 2
        self.currentsize = len(listofnode)
        self.heaplist = [0] + listofnode[:]
        while (i > 0):
            self.perculate_down(i)
            i = i - 1
        


# In[ ]:




