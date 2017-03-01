def slices(serie, n):
    if n == 0 or len(serie) < n:
        raise ValueError

    result = []
    for i, curr in enumerate(serie):
        substring = []
        substring.append(int(curr))
        for l, nextt in enumerate(serie):
            if len(substring) < n and i < l:
                substring.append(int(nextt))
            elif len(substring) >= n:
                break

        if len(substring) == n:
            result.append(substring)

    return result
