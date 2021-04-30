# -*- coding: utf-8 -*-
"""Quick-Sort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lSZpYubwiW4XbMlyJP7Xl8pA0602EoGs
"""

def quick_sort(arr):
  quick_sort_help(arr,0,len(arr)-1)
  return arr


def quick_sort_help(arr,first,last):
  if first<last:

    splitout=partition(arr,first,last)
    
    quick_sort_help(arr,first,splitout-1)
    
    quick_sort_help(arr,splitout+1,last)


def partition(arr,first,last):
  
  Pivot=arr[first]
  leftmark=first+1
  rightmark=last
  Exit=False
  
  while not Exit:
    while leftmark<=rightmark and arr[leftmark]<=Pivot:
      leftmark=leftmark+1
    while rightmark>=leftmark and arr[rightmark]>=Pivot:
      rightmark=rightmark-1
    if rightmark<leftmark:
      Exit=True
    else:
      temp=arr[leftmark]
      arr[leftmark]=arr[rightmark]
      arr[rightmark]=temp
    
    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark

quick_sort([10,2011,1212,1234,19929])