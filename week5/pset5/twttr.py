def main():
    s = input('Input: ')
    o = shorten(s)
    print('Output: ', o)

def shorten(word):
    o = ""
    for c in word:
        if c.lower() not in 'aeiou':
            o += c
    return o


if __name__ == "__main__":
    main()