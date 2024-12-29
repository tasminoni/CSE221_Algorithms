# -*- coding: utf-8 -*-
"""task-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dXDkHPBAbrPy3iAlWvr756wmOJ5r_rdR
"""

#task03
def quickSort(arr, low, high):
    if (low < high):
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = (low - 1)
    for j in range(low, high):
        if (arr[j] < pivot):
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


inp = open("input3.txt", "r")
out = open("output3.txt", "w")
n= int(inp.readline())
arr=[int(x) for x in inp.readline().split()]
r=quickSort(arr, 0, n-1)
s=""
for i in range(n):
  s = s + " " + str(arr[i])
out.write(s)
print(arr)
inp.close()
out.close()