def neg_pos(*args):
    neg = []
    pos = []
    for num in args:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)
    return sorted(neg, reverse=True), sorted(pos)
print(neg_pos(1, 2, 3, 4, 5, 6, 7, 8, 9, -7, -45, 0))