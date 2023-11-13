# Fuel Gauge

def main():
    x = get_fraction()
    print(x)

def get_fraction():
    while True:
        try:
            x,y = input('Fraction: ').split('/')
            if 0 <= int(x)/int(y) <= 0.1:
                return ('E')
            elif 0.9 <= int(x)/int(y) <= 1:
                return ('F')
            else:
                return (str(round((int(x)/int(y)) * 100))) + '%'
        except (ValueError, ZeroDivisionError):
            pass

main()