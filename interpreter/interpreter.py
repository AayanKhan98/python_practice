a = input("input number").strip()
x, y, z = a.split(" ")
x = float(x)
z = float(z)
if y == "+":
    print(x+z)
elif y == "*":
    print(x*z)
elif y == "-":
    print(x-z)
elif y == "/":
    print(x/z)
else:
    print(yooo)