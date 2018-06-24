
# input
# - [] of weights, ints, > 0
# - [] of values, ints, > 0

# maximize the value given weight constraint

# recursive approach
weights = [1, 2, 3, 5]
values = [2, 3, 4, 4]


def knapsack(capacity, index=0):
    "recursive solution to knapsack"
    if index == len(weights) or capacity == 0:
        return 0
    elif weights[index] > capacity:
        return knapsack(capacity, index + 1)
    else:
        # skip item
        temp1 = knapsack(capacity, index + 1)

        # add item
        temp2 = values[index] + knapsack(capacity - weights[index], index + 1)
        return max(temp1, temp2)


a = knapsack(5)
print(a)
print(a == 7)
