x,y,z = input('Expression: ').strip().split(" ")

x = float(x)
z = float(z)

if y == '+':
    print(x+z)
elif y == '-':
    print(x-z)
elif y == '*':
    print(x*z)
elif y == '/':
    print(x/z)
else:
    print('请勿输入四则运算以外的符号')