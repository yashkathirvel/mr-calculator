# import libraries:

import csv

# ---------------------------------------------------------------------------------

# import atomic mass data:

with open('./periodic-table.csv', 'r') as file:

    reader = csv.DictReader(file)

    data = {}

    for row in reader:
        new_data = {row['Symbol'] : float(row['AtomicMass'])}
        data.update(new_data)

print(data['C'])
