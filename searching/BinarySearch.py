# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:13:28 2021

@author: Abeg
"""

#Binary Search
def bsearch(arr,x,l,r):
  #if r-l==0:
    #return False
  mid=(r+l)//2
  if x==arr[mid]:
    return mid
  elif x<arr[mid]:
    return bsearch(arr,x,l,mid-1)
  else:
    return bsearch(arr,x,mid+1,r)
x=int(input())
n=int(input())
arr=[int(input()) for i in range(n)]
print(bsearch(arr,x,0,n))