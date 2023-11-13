def main():
    camel = input('camelCase: ').strip()
    snake = convert(camel)
    print("snake_case: ", snake)

def convert(camel):
    result = ''
    for c in camel:
        if c.isupper():
            result += '_' + c.lower()
        else:
            result += c
    return result
main()