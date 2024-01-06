# Week6/Lines of Code

import sys


def main():
    if len(sys.argv) == 2 and sys.argv[1].endswith('.py'):
        try:
            with open(f'{sys.argv[1]}', 'r') as file:
                lines = file.readlines()
                count = count_lines(lines)
            print(count)
            
        except FileNotFoundError:
            sys.exit('File does not exist')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('Not a Python file')

def count_lines(count_lines):
    strip_lines = []
    for line in count_lines:
        if line.strip() and not line.lstrip().startswith('#'):
            strip_lines.append(line)
    return len(strip_lines)

if __name__ == '__main__':
    main()