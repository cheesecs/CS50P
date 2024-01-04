def main():
    fraction = input('Fraction: ')
    percentage = convert(fraction)
    result = gauge(percentage)

    print(result)


def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split('/'))
            if x > y:
                raise ValueError
            elif y == 0:
                raise ZeroDivisionError
            return round(x / y * 100)
        except (ValueError, ZeroDivisionError):
            pass



def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'




if __name__ == "__main__":
    main()