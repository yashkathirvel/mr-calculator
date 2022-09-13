# import libraries:

import csv
import re

# ---------------------------------------------------------------------------------

def main():

    # import atomic mass data:

    with open('./periodic-table.csv', 'r') as file:

        reader = csv.DictReader(file)
        data = {}

        for row in reader:
            new_data = {row['Symbol'] : float(row['AtomicMass'])}
            data.update(new_data)

    # user input and separate string:

    form = input('Please enter your molecular formula (ex. H2O, HBr, CH3COOH): \n')

    # regex that separates strings at each uppercase letter:

    sep_form = re.sub(r"([A-Z])", 
                    r" \1", 
                    form).split()

    # map and function that adds 1 to unnumbered elements:

    fixed_form = list(map(lambda x:  x + '1' if x.isalpha()==True else x,
                        sep_form))

    # init molecular weight variable:

    mr = 0

    # calculate molecular weight

    for i in fixed_form:
        match = re.match(r"([a-z]+)([0-9]+)", 
                        i, 
                        re.I)
        if match:
            items = match.groups()
            mr += data[items[0]] * float(items[1])

    print('The molecular weight is', mr)

# ---------------------------------------------------------------------------------

if __name__ == "__main__":
    main()