import csv
import sys

def main():
    # if len(sys.argv) == 3 and sys.argv[1].strip().endswith('.csv') and sys.argv[2].strip().endswith('.csv'):
    if len(sys.argv) == 3 and all(arg.strip().endswith('.csv') for arg in sys.argv[1:]):
        try:
            newcsv(sys.argv[1], sys.argv[2])
        except FileNotFoundError:
            sys.exit(f'Could not read {sys.argv[1]}')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

def newcsv(old, new):
    with open(old, 'r') as file:
        reader = csv.DictReader(file)

        with open(new, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for row in reader:
                name, house = row['name'], row['house']
                first_name, last_name = name.strip().split(', ')
                writer.writerow({'first': last_name, 'last': first_name, 'house': house})

if __name__ == '__main__':
    main()