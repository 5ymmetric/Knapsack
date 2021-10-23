# Author: Karthik Reddy Pagilla

import copy
import sys
import re
import time

class Item:
    def __init__(self, weight, value, index):
        self.weight = weight
        self.value = value
        self.index = index

    def toString(self):
        print("(" + str(self.index) + ", " + str(self.weight) + ", " + str(self.value) + ") ", end="")

def tableau_generator(items, W):
    tableau = [[0]*(W+1) for i in range(len(items)+1)]

    for i in range(1, len(items) + 1):
        for j in range(1, W+1):
            if j - items[i - 1].weight >= 0:
                if tableau[i - 1][j] > tableau[i - 1][j - items[i - 1].weight] + items[i - 1].value:
                    tableau[i][j] = tableau[i - 1][j]
                else:
                    tableau[i][j] = tableau[i - 1][j - items[i - 1].weight] + items[i - 1].value
            else:
                tableau[i][j] = tableau[i - 1][j]

    return tableau

def dynamic_knapsack(tableau, items, n, W):
    result = []
    i = n
    j = W
    while i >= 1 and j >= 1:
        while i >= 1 and tableau[i][j] == tableau[i - 1][j]:
            i = i - 1
        if items[i - 1] not in result:
            temp = copy.deepcopy(result)
            temp.append(items[i - 1])
            if find_weight(temp) <= W:
                result.append(items[i - 1])
        j = j - items[i - 1].weight
        i = i - 1

    return result

def find_weight(set):
    total_weight = 0.0
    for element in set:
        total_weight = total_weight + element.weight
    return total_weight

def find_value(set):
    total_value = 0.0
    for element in set:
        total_value = total_value + element.value
    return total_value

# Reading the input file
f = open(sys.argv[1], 'r')

f = open('/content/input', 'r')

tokens = re.split(" ", f.readline())
n = int(tokens[0].strip())
W = int(tokens[1].strip())

items = []

weights = re.split(" ", f.readline().rstrip())
values = re.split(" ", f.readline().rstrip())

f.close()

for a in range(n):
    i = Item(int(float(weights[a])), float(values[a]), a+1)
    items.append(i)

tableau = tableau_generator(items, W)

print("Tableau:")
print()
for i in tableau:
    print("[ ", end="")
    print(i[0], end="")
    for j in i[1:]:
        print("{:>6}".format(j), end="")
    print(" ]")
print()

result = dynamic_knapsack(tableau, items, n, W)

print("Maximum Capacity: W = " + str(W))

print("Original Knapsack Items: [ ", end="")
for i in items:
    i.toString()
print("]")

print("Optimal Knapsack Items: [ ", end="")
for i in result:
    i.toString()
print("]")

print("Optimal Weight: " + str(find_weight(result)))

print("Optimal Value: " + str(find_value(result)))