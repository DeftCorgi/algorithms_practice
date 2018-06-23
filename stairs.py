
# current_step: num_keys

saved = dict()


def stairs(current, target):
    # base case
    if current == target:
        return 1
    elif current in saved:
        return saved[current]
    else:
        step1 = stairs(current + 1, target)
        step2 = stairs(current + 2, target) if current + 2 <= target else 0
        saved[current] = step1 + step2
        return step1 + step2

# time - O(2^n)
# space - O(n)


print(stairs(0, 60))
