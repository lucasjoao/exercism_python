import string

alpha = {c: i for i, c in enumerate(string.ascii_lowercase)}
alpha_backwards = {i: c for i, c in enumerate(string.ascii_lowercase[::-1])}


def decode(text):
    decoded = ''
    for c in text:
        if c == ' ':
            continue

        decoded += c if c.isdigit() else alpha_backwards[alpha[c]]

    return decoded


def encode(text):
    encoded = ''
    final_text = text.lower().replace(" ", "")
    gambi = 0

    for c in final_text:
        if c in string.punctuation:
            continue

        if gambi == 5:
            encoded += ' '
            gambi = 0

        encoded += c if c.isdigit() else alpha_backwards[alpha[c]]
        gambi += 1

    return encoded
