#!/usr/bin/env python
import csv
import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]
output_rows = []

with open(input_filename, 'r') as input_file:
    reader = csv.reader(input_file)
    next(reader)

    for row in csv.reader(input_file, delimiter=','):
        # Strip the currency symbol, and multiply the amount by -1
        amount = float(row[2].replace('£', '')) * -1

        # Change the field order to be date, amount, description
        output_rows.append((row[0], amount, row[1]))

with open(output_filename, 'w') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(output_rows)
