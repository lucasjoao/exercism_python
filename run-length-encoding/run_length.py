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
    backup = ''
    for curr, nextt in zip(chars, chars[1:]):
        if curr.isdecimal() and nextt.isalpha():
            decoded += int(curr) * nextt
        elif curr.isalpha() and nextt.isalpha():
            decoded += int(backup) * curr + nextt if backup.isdecimal() else curr + nextt
        elif curr.isdecimal() and nextt.isdecimal():
            tmp = curr
            curr = tmp + nextt
        else: # alpha and decimal
            decoded += int(backup) * curr if backup.isdecimal() else curr
            curr = nextt

        backup = curr

    return decoded

