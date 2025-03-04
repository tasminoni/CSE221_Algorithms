# -*- coding: utf-8 -*-
"""lab06-221.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Klmb16_B4ayDyklfLZtJTiupdEkYaUWl
"""

from collections import defaultdict
from queue import PriorityQueue

inp = open("/content/input1.txt", "r")
out= open("/content/output1.txt", "w")
x,y= [int(x) for x in inp.readline().split()]
graph= defaultdict(list)

for i in range(y):
  m,n,o=[int(x) for x in inp.readline().split()]
  graph[m].append((o,n))
st_node= int(inp.readline())
#print(graph)
def function(graph,st_node):
  inf= float("inf")
  dis=[inf]*(x+1)
  visited=[False]*(x+1)
  dis[st_node]=0
  pq=PriorityQueue()
  pq.put((0,st_node))

  while not pq.empty():
    node= pq.get()
    visited[node[1]]=True
    if node[0]<dis[node[1]]:
      dis[node[1]]=node[0]
    for neighbour in graph[node[1]]:
      neighbour_w= node[0]+ neighbour[0]
      if not visited[neighbour[1]]:
        pq.put((neighbour_w,neighbour[1]))

  return dis

q= function(graph,st_node)

for i in q[1:]:
  if i==float("inf"):
    out.write("-1")
  else:
    out.write(str(i)+" ")
#print(q)
inp.close()
out.close()

