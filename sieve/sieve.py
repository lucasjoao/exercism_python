def sieve(n):
    result = [i for i in range(2, n+1)]
    for x in result:
        has_next = True
        i = 2
        while has_next:
            multiple = x * i
            i += 1

            if multiple in result:
                result.remove(multiple)
            elif multiple > n:
                has_next = False

    return result
