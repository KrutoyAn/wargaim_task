def controls(word):
    set_len_world = len(set(word))

    if (set_len_world >= 3 and set_len_world < 107):
        return print_result(word.lower())
    else:
        return 'Слово не проходит по-условию.'


def count_chars(word):
    chars = {}
    for j in word:
        sums = word.count(j)
        if sums > 1:
            chars.setdefault(j, sums)
        chars = dict(sorted(chars.items(), key=lambda x: x[1], reverse=True))
    return chars


def print_result(word):
    a = count_chars(word)
    i = 0
    for k, v in a.items():
        if i < 3:
            i +=1
            print(k, v)
        else:
            pass
    return ''


# print(print_result(input()))
if __name__ == "__main__":
    print(controls('AAWarggggggaaimingsssss'))