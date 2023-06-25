import csv

def exchange_values(csv_file, output_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        for i in range(1, len(row)):
            value = int(row[i])
            row[i] = str(255 - value)

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Values exchanged successfully. Updated CSV saved as '{output_file}'.")

# Usage example
csv_file = 'mydigits.csv'
output_file = 'selfmade.csv'
exchange_values(csv_file, output_file)

