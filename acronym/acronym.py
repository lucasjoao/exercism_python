from itertools import zip_longest


def abbreviate(text):
    acronym = text[0].upper()
    for curr, nextt in zip_longest(text, text[1:]):
        if curr == ':' or nextt is None:
            break

        if curr == ' ' or curr == '-' or nextt.isupper():
            acronym += nextt.upper()

    return acronym
