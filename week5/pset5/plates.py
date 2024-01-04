def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalpha():
        return True
    elif s.isalnum() and s[0:2].isalpha():
        for c in s:
            if c.isdigit():
                # 获取第一个数字的下标
                position = s.index(c)

                # 判断下标后面是否为数字 判断首个数字是否为0
                if s[position:].isdigit() and int (c) != 0:
                # if s[position:].isdigit() and int(s[position]) != 0:
                    return True
                else:
                    return False
    else:
        return False


if __name__ == "__main__":
    main()