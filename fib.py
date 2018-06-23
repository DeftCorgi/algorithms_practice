# fib

# 1, 1, 2, 3, 5, 8, 13, 21
# fib(1) = 1
# fib(3) = 2
# fib(5) = 5

# iterative

# O(N)
# O(1)
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a

# recursive
# O(2^N)


def fib(n):
    n = n - 1
    return fibr(n)


checked = {}


def fibr(n):
    if n <= 1:
        return 1
    if n in checked:
        return checked[n]
    else:
        checked[n] = fibr(n-1) + fibr(n-2)
        return checked[n]


print(fib(900))
