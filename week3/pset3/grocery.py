def grocery_list():
    grocery = {}
    try:
        while True:
            item = input().upper().strip()

            grocery[item] = grocery.get(item, 0) + 1
    except EOFError:
        pass
    
    for item, count in sorted(grocery.items()):
        print(f"{count} {item}")

if __name__ == "__main__":
    grocery_list()