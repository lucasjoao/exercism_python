def detect_anagrams(word, candidates):
    sublist = []
    for w in candidates:
        if word.lower() != w.lower() and \
        len(word) == len(w) and \
        sorted(word.lower()) == sorted(w.lower()):
            sublist.append(w)

    return sublist
