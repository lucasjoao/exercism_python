from itertools import zip_longest

def encode(chars):
    encoded = ''
    n = 1
    for curr, nextt in zip_longest(chars, chars[1:]):
        if curr == nextt:
            n += 1
        else:
            encoded += curr if n is 1 else str(n) + curr
            n = 1

    return encoded

def decode(chars):
    decoded = ''
    number = ''
    for c in chars:
        if c.isdigit():
            number += c
        else:
            decoded += int(number) * c if number != '' else c
            number = ''

    return decoded

