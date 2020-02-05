import csv

with open('titanic.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # set the counter
    female_survive = 0
    male_survive = 0
    female_no_survive = 0
    male_no_survive = 0
    # iterate over rows
    for row in csv_reader:
        # if passenger is female and if she survived, increase the counter
        if row[1] == '1' and row[4] == 'female':
            female_survive += 1
        elif row[1] == '1' and row[4] == 'male':
            male_survive += 1
        elif row[1] == '0' and row[4] == 'female':
            female_no_survive += 1
        elif row[1] == '0' and row[4] == 'male':
            male_no_survive += 1
# print(female_survive)]

"""
Questions:
1. Average age of a male passenger?
2. How many died who were under the age of 18?
3. Average price of fare paid by survivors? Non-survivors?
4. Do sibilings of survivors also survive?
5. Most common last name?
6. Correlation between port of embarkation and survival?
7. Amount of family affect patriarch survival?
8. Of women above the age of
"""
