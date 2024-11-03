import csv

filename = 'social_media_users.csv'

file = open(filename)
csv_file = csv.reader(file)

for line in csv_file:
    print(line[2:4])
