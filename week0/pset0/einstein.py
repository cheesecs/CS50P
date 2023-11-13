# E = mc^2

def main():
    m = int(input('m:'))
    print("E:" + str(E(m)))

def E(m):
    c = 300000000
    E = m * pow(c, 2)
    
    return E

main()