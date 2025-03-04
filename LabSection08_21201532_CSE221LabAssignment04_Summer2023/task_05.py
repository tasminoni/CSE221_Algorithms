# -*- coding: utf-8 -*-
"""Task-05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jC3wEEuwiNF9VMrWNKiiYvKED6pFkmYO
"""

#task 5
def bfs(root, destination, graph, visit_arr, distance_arr, pred_arr):
    q1 = []
    visit_arr[root] = 1
    distance_arr[root] = 0
    q1.append(root)
    while(len(q1) != 0):
        visit = q1.pop(0)
        for i in range(len(graph[visit])):
            if(visit_arr[graph[visit][i]] == 0):
                q1.append(graph[visit][i])
                distance_arr[graph[visit][i]] = distance_arr[visit] + 1
                visit_arr[graph[visit][i]] = 1
                pred_arr[graph[visit][i]] = visit

                if(graph[visit][i] == destination):
                    return True
    return False

def shortDistance(root, destination, graph, visit_arr):
    times = ""
    paths = ""
    if(root == destination):
        times += "Time: 0"
        paths += f"Shortest Path: {root}"

    else:
        distance_arr = [1000] * len(visit_arr)
        pred_arr = [-1] * len(visit_arr)

        if(bfs(root, destination, graph, visit_arr, distance_arr, pred_arr)):
            path = []
            temp = destination
            path.append(temp)

            while(pred_arr[temp] != -1):
                path.append(pred_arr[temp])
                temp = pred_arr[temp]


            times += f"Time: {distance_arr[destination]}"
            paths += "Shortest Path: "
            for i in range(len(path)-1, -1, -1):
                paths += str(path[i]) + " "

    return (times, paths)

def ad_matrix(inp, out):
    n,m,d = inp.readline().split()
    n = int(n)
    m = int(m)
    d = int(d) #destination
    matrix = []
    visit_arr = [0] * (n+1)

    for i in range(n + 1):
        matrix.append([])

    for i in range(m):
        lst = [int(x) for x in inp.readline().split()]
        matrix[lst[0]].append(lst[1])
        matrix[lst[1]].append(lst[0])

    times, paths = shortDistance(1, d, matrix, visit_arr)
    print(times)
    print(paths)
    out.write(times + "\n")
    out.write(paths + "\n")

    inp.close()
    out.close()

inp = open("/content/input5.txt", "r")
out = open("/content/output5.txt", "w")
ad_matrix(inp, out)