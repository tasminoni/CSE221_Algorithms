# -*- coding: utf-8 -*-
"""task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yzoMmZfbriqcawq16lXTEk_LCLHWom6j
"""

#Task4:
task_input = open("input4.txt", "r")
task_output = open("output4.txt", "w")
size = int(task_input.readline())
train_arr = [None] * size
for i in range(size):
    temp = task_input.readline().split()
    train_arr[i] = [temp[0], temp[4], temp[6]]

for i in range(size - 1):
    min = i
    for j in range(i+1, size):
        if(train_arr[j][0] < train_arr[min][0]):
            min = j

        elif(train_arr[j][0] == train_arr[min][0]):
            if(train_arr[j][2] > train_arr[min][2]):
                min = j

    temp = train_arr[min]
    train_arr[min] = train_arr[i]
    train_arr[i] = temp

for i in range(size):
    print(f"{train_arr[i][0]} will departure for {train_arr[i][1]} at {train_arr[i][2]}")
    task_output.write(f"{train_arr[i][0]} will departure for {train_arr[i][1]} at {train_arr[i][2]}\n")

task_input.close()
task_output.close()