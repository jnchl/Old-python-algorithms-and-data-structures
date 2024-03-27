def naive_template(S, W):
    m = 0
    i = 0

    number_of_checks = 0
    indexes = []

    text_length = len(S)
    template_length = len(W)

    while (m < text_length):
        current_index = m
        i = 0
        while (i < template_length):
            template_char = W[i]
            text_char = S[m + i]
            number_of_checks += 1
            if text_char != template_char:
                break

            if i == template_length - 1:
                indexes.append(current_index)

            i += 1
        m += 1

    occurences = len(indexes)

    return '{}; {}'.format(occurences, number_of_checks)