x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()

match x:
    case "Forty Two" | "forty-two" | "42" | "FoRty TwO" | "forty two" :
        print("Yes")
    case _:
        print("No")