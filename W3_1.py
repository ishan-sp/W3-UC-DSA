def change_money(money, denominations):
    count = 0
    remaining = money
    while remaining > 0:
        maxdenum = max(denominations)
        if maxdenum <= remaining:
            count += 1
            remaining -= maxdenum
        else:
            denominations.remove(maxdenum)
    return count

amt = int(input())
print(change_money(amt, [1,5,10]))
