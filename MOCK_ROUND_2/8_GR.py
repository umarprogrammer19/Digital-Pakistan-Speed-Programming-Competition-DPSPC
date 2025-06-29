def win_in_2_rounds(n, d):
    if d == 1:
        for p in range(n + 1, n + 101):
            naan, plate = n, p
            eat = min(naan, plate)
            naan -= eat
            plate -= eat
            if naan == 0:
                naan = n // 2
            elif plate == 0:
                plate = p // 2
            else:
                continue
            eat = min(naan, plate)
            naan -= eat
            plate -= eat
            if naan == 0 and plate == 0:
                return p
    else:
        for p in range(n - 1, 0, -1):
            naan, plate = n, p
            eat = min(naan, plate)
            naan -= eat
            plate -= eat
            if naan == 0:
                naan = n // 2
            elif plate == 0:
                plate = p // 2
            else:
                continue
            eat = min(naan, plate)
            naan -= eat
            plate -= eat
            if naan == 0 and plate == 0:
                return p
    return -1
n, d = map(int, input().split())
print(win_in_2_rounds(n, d))
