def kmp(S, W):
    M = len(S)
    N = len(W)
    number_of_checks = 0

    def kmp_table(W):
        pos = 1
        cnd = 0
        T = []

        T.append(-1)

        while pos < N:
            if pos > len(T) - 1:
                T.append(None)

            if W[pos] == W[cnd]:
                T[pos] = T[cnd]
            else:
                T[pos] = cnd
                while cnd >= 0 and W[pos] != W[cnd]:
                    cnd = T[cnd]

            pos += 1
            cnd += 1
        T.append(None)
        T[pos] = cnd
        return T

    m = 0
    i = 0
    T = kmp_table(W)
    P = []
    nP = 0

    while m < M:
        number_of_checks += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == N:
                P.append(m - i)
                nP += 1
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1

    occurences = len(P)
    return '{}; {}; {}'.format(occurences, number_of_checks, T)