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
        print("Item [weight = " + str(self.weight) + ", value = " + str(self.value) + "]")

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

def knapsack(items, subset, j, n, W):
    if j == n:
        return subset
    s_best = copy.deepcopy(subset)
    
    for k in range(j+1, n):
        s_new = copy.deepcopy(subset)
        s_new.append(items[k])
        if find_weight(s_new) <= W:
            temp = knapsack(items, s_new, k, n, W)
            if find_value(temp) > find_value(s_best):
                s_best = temp

    return s_best

start = time.time()

# Reading the input file
#f = open(sys.argv[1], 'r')
f = open('/content/input2', 'r')

tokens = re.split(" ", f.readline())
n = int(tokens[0].strip())
W = float(tokens[1].strip())

items = []

weights = re.split(" ", f.readline())
values = re.split(" ", f.readline())

f.close()

for a in range(n):
    i = Item(float(weights[a]), float(values[a]), a)
    items.append(i)

s = [items[0]]
j = 0
result = knapsack(items, s, j, n, W)

index_solution = []
for r in result:
    index_solution.append(r.index)

end = time.time()

print("Optimal knapsack:" + " " + str(index_solution))

print("Runtime: " + str(end - start) + " seconds")

print("Capacity:" + " " + str(W))

print("Weight:" + " " + str(find_weight(result)))

print("Value:" + " " + str(find_value(result)))