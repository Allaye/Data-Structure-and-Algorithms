#!/usr/bin/env python
# coding: utf-8

# In[32]:


class Stacks2Queue:
    '''
    convert 2 stacks into a queue, here i use python list to represent that stack
    '''
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def isEmpty(self):
        return self.stack1 & self.stack2 == []
    
    def size(self):
        return len(self.stack1 + self.stack2)
    
    def enqueue(self, item):
        return self.stack1.append(item)
    
    def dequeue(self):
        if self.stack2 == []:
            while(self.stack1 != []):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()
    
    def front(self):
        if self.stack2 == []:
            return self.stack1[0]
        return self.stack2[-1]


# In[ ]:




