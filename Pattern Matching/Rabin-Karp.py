def RabinKarp(S, W):
    M = len(S)
    N = len(W)
    number_of_checks = 0
    collisions = 0

    d = 256
    q = 101

    def hash(word):
        hw = 0
        for i in range(len(word)):
            hw = (hw * d + ord(word[i])) % q
        return hw

    hW = hash(W)
    indexes = []

    for m in range(M - N + 1):
        hS = hash(S[m:m + N])

        number_of_checks += 1
        if hS == hW:
            if S[m:m + N] == W:
                indexes.append(m)
            else:
                collisions += 1

    occurences = len(indexes)

    return '{};{}'.format(occurences, number_of_checks)
