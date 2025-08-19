def matchword(words):
    ctr = 0
    list = []
    for i in words:
        if len(i) > 1 and i[0] == i[-1]:
            ctr += 1
            list.append(i)

    print(list)
    return ctr

word = matchword(['abd', 'aba', 'wed', '121', 'bsb', 'low'])

print(word)

        