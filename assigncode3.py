import csv
data_dict = csv.DictReader(open("Dataset-movies.csv"))
print("file as dictionary is:")
for i in data_dict:
    print(i)
