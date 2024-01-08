from tabulate import tabulate
import csv
import sys

def main():
    if len(sys.argv) == 2 and sys.argv[1].strip().endswith('.csv'):
        try:
            csv_table = ASCII_ART_TABLE(sys.argv[1])
            print(csv_table)
        except FileNotFoundError:
            sys.exit('File does not exist')
            
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')

    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    
    else:
        sys.exit('Not a CSV file')

def ASCII_ART_TABLE(csv_file):
    table = []
    with open(f"{csv_file}") as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
    return tabulate(table, headers='firstrow', tablefmt='grid')


if __name__ == '__main__':
    main()