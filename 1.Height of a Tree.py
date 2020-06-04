#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

class StackWithMax():
    def __init__(self):
        self.main=[]
        self.track=[]

    def Push(self, x):
        self.main.append(x)
        if len(self.main)==1:
            self.track.append(x)
            return
        if(x>self.track[-1]):
            self.track.append(x)
        else:
            self.track.append(self.track[-1])

    def Pop(self):
        self.main.pop()
        self.track.pop()

    def Max(self):
        return self.track[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)

