amount_due = 50
inserted = 0

while inserted < amount_due:
    print("Amount Due:", amount_due - inserted)
    insert_coin = int(input('Insert Coin: '))
    if insert_coin in [25, 10, 5]:
        inserted += insert_coin
print("Change Owed:", inserted - amount_due)