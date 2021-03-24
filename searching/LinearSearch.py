# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:41:31 2021

@author: Abeg
"""

#Linear Search
def LinearSearch(arr,k):
    global value
    for i in range(len(arr)):
        if(arr[i]==k):
            value=i
    return value
    

n,k=map(int,input().split())
arr=list(map(int,input().strip().split()))
print(LinearSearch(arr,k))
