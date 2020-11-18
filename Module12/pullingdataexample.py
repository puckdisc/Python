import csv

with open('ExampleCSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # The first row is treated differently because it is the header row
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row)
            line_count += 1
    print(f'processed {line_count} rows')
