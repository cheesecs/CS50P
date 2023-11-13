vowels = ['a', 'e', 'i', 'o', 'u']

s = input('Input: ')
o = ''
for c in s:
    if c.lower() not in vowels:
        o += c
print('Output: ', o)