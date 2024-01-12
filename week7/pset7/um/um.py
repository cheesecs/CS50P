import re

def main():
    print(count(input("Text: ")))

def count(s):
    rex = re.findall(r"\bum\b", s, re.IGNORECASE)
    c = 0
    for _ in rex:
        c += 1
    return c

if __name__ == "__main__":
    main()