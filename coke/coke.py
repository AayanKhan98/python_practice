print("Amount Due: 50")
d = 50

while d > 0:
    c = int(input("Insert Coin: "))
    if (c == 5 or c == 10 or c == 25):
        d = d - c
        if d > 0:
            print(f"Amount Due: {d}")
        else:
            print(f"Change Owed: {abs(d)}")
    else:
        print(f"Amount Due: {d}")