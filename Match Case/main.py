a=int(input("Enter an Integer: "))
match a:
    case 1:
        print("one")
    case 2:
        print("two")
    case _:
        print("No match found")