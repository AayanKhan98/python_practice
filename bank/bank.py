greet = input("Greeting: ").strip()

first = greet.split(maxsplit = 1)[0]

match first:
    case "Hello" | "Hello," :
      print("$0")
    case  "Hey" | "How" | "Hi" | "Hi," | "Hey," :
        print("$20")
    case _:
       print("$100")
