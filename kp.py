
# input
# - [] of weights, ints, > 0
# - [] of values, ints, > 0

# maximize teh value given weight constraint

# greedy approach
# compute weight:value for each item
# add largest ratio item until weight capicity met

# time - O(n)
# space - O(n)

# recrusive approach

weights = [1, 2, 3, 5]
values = [2, 3, 4, 4]


def knapsack(index, capacity):
    if index == len(weights) or capacity == 0:
        return 0
    elif weights[index] > capacity:
        return knapsack(index + 1, capacity)
    else:
        # skip
        temp1 = knapsack(index + 1, capacity)

        # add
        temp2 = values[index] + knapsack(index + 1, capacity - weights[index])
        return max(temp1, temp2)


a = knapsack(0, 5)
print(a)
print(a == 7)
