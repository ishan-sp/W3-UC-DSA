def change_money(money, denominations):
    result = []
    remaining = money
    while remaining > 0:
        maxdenum = max(denominations)
        if maxdenum <= remaining:
            result.append(maxdenum)
            remaining -= maxdenum
        else:
            denominations.remove(maxdenum)
    return result

print("The denominations available are 2000, 1000, 500, 100, 50, 20, 10, 5, 2, 1")
amt = int(input("Enter the total amount: "))
print(change_money(amt, [1,4,6]))
