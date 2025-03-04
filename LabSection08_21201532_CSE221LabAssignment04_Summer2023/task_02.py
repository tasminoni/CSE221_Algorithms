# -*- coding: utf-8 -*-
"""Task-02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TkcbA4W2357f9SiPssMEaooMjDkB5Hnq
"""

from queue import Queue

def adjacency_matrix(inp, out):
    n, m =  inp.readline().split()
    n=int(n)
    m=int(m)
    matrix = []

    visit_arr = [0] * (n + 1)

    for i in range(n + 1):
        matrix.append([])

    for i in range(m):
        lst = [int(x) for x in inp.readline().split()]
        matrix[lst[0]].append(lst[1])
        matrix[lst[1]].append(lst[0])

    s = bfs(1, visit_arr, matrix)
    print(s)
    out.write(s)

    inp.close()
    out.close()

def bfs(root, visit_arr, graph):
    q1 = Queue()
    q1.put(root)
    visit_arr[root] = 1
    s = ""
    while not q1.empty():
        visit = q1.get()
        s += str(visit) + " "
        for i in range(len(graph[visit])):
            if visit_arr[graph[visit][i]] == 0:
                q1.put(graph[visit][i])
                visit_arr[graph[visit][i]] = 1

    return s

inp = open("/content/input2.txt", "r")
out = open("/content/output2.txt", "w")
adjacency_matrix(inp, out)