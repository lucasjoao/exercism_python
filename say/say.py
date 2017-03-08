basic = {0: 'zero',
         1: 'one',
         2: 'two',
         3: 'three',
         4: 'four',
         5: 'five',
         6: 'six',
         7: 'seven',
         8: 'eight',
         9: 'nine'}

tens = {10: 'ten',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'}

def say(n):
    result = ''

    if n < 0 or n >= 1e12:
        raise AttributeError
    elif n < 10:
        result = basic[n]
    elif n < 100 and n % 10 == 0:
        result = tens[n]
    elif n < 100:
        last_digit = n % 10
        n -= last_digit
        result = tens[n] + '-' + basic[last_digit]
    # to-do in step1: when 10 < n < 20
    return result
