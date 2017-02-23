def detect_anagrams(word, candidates):
    sublist = []
    for w in candidates:
        if word.lower() == w.lower() or len(word) != len(w):
            continue

        can_append = True
        for c in w.lower():
            if c not in word.lower():
                can_append = False


        if can_append:
            sublist.append(w)

    return sublist
