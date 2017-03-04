def sum_of_multiples(limit, lst):
    numbers = set()

    for i in lst:
        if i != 0:
            numbers.update(range(i, limit, i))

    return sum(numbers)
