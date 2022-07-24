# import libraries:

import csv
from os import sep
import re
import string

# ---------------------------------------------------------------------------------

# import atomic mass data:

with open('./periodic-table.csv', 'r') as file:

    reader = csv.DictReader(file)

    data = {}

    for row in reader:
        new_data = {row['Symbol'] : float(row['AtomicMass'])}
        data.update(new_data)

# user input and separate string:

form = 'C10H15N'

# regex that separates strings at each uppercase letter:

sep_form = re.sub(r"([A-Z])", 
                  r" \1", 
                  form).split()

# map and function that adds 1 to unnumbered elements:

fixed_form = list(map(lambda x:  x + '1' if x.isalpha()==True else x,
                      sep_form))

for i in fixed_form:
    match = re.match(r"([a-z]+)([0-9]+)", i, re.I)
    if match:
        items = match.groups()
        print(items[0])




