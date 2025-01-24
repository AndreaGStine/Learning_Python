# importing csv module
import csv
import random

# csv file name
filename = 'aadr.us.txt'

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % csvreader.line_num)

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:1500]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')

    hilos = []

for r in rows:
    hilos.append([r[2], r[3]])

    midpoints = []

for h in hilos:
    midpoints.append((float(h[0]) + float(h[1])) / 3)

changes = []
trainingchanges = []
n = 0
while n <= 1563:
    changes.append(midpoints[n] - midpoints[n + 1])
    n = n + 1

n = 0
while n <= 300:
    trainingchanges.append(midpoints[n] - midpoints[n + 1])
    n = n + 1

print(max(trainingchanges))

avgchange = 0
for c in trainingchanges:
    avgchange = avgchange + abs(c)

avgchange = float(avgchange) / 300

print(avgchange)


