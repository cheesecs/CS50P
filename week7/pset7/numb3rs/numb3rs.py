import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^(\d{1,3}\.){3}\d{1,3}$", ip):
        for num in ip.split('.'):
            if not (0 <= int(num) <= 255):
                return False
        return True
    else:
        return False
    

if __name__ == "__main__":
    main()