#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Stack import Stack # personal implementation of stack using python list 


# In[12]:


def check_balance(string, opening='('):
    '''
    a function to check if parenthesis used in a statement is balanced
    this solution used a custom implementation of a stack using python list.
    the below steps was used:
    a: check if the length of the string to be checked is even, if yes:
        c: loop through the string, if the any item there is == to the opening variable:
        d: push then into the stack, else:
        e: check if the length is not zero, if it is not pop the stack, else:
        f: return false:
        g: if we reach the end of the loop, return True if the size of the stack is zero else return False
    b:
    '''
    s = Stack()
    if len(string) % 2 == 0:
        for w in string:
            if w == opening:
                s.push(w)
            else:
                if s.size() > 0:
                    s.pop()
                else:
                    return False
        return s.size() == 0
    else:
        return False


# In[2]:


def double_balance(string, openings=['[', '{', '(']):
    '''
    a function to check if the 3 types of parenthesis used in a statement is balanced
    this solution used a custom implementation of a stack using python list.
    the below steps was used:
    a: check if the length of the string to be checked is even, if yes:
        c: loop through the string, if the item matches openings:
        d: push then into the stack, else:
        e: check if the top element in the stack and item matches any tuple in our matches and pop the stack else:
        f: return false:
        g: if we reach the end of the loop, return True if the size of the stack is zero else return False
    b: return False since the parenthesis can only be balance if the have a corresponding closing one
    '''
    s = Stack()
    matches = [('{', '}'), ('(', ')'), ('[', ']')]
    if len(string) % 2 == 0:
        for w in string:
            if w in openings:
                s.push(w)
            else:
                if (s.peek(), w) in matches:
                    s.pop()
                else:
                    return False
        return s.size() == 0
    else:
<<<<<<< HEAD
        return False
=======
        return False



>>>>>>> 34dd19a4c05ecb4cd984fb078a578c1934859c39
