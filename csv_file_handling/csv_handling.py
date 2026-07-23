# https://docs.python.org/3/library/csv.html#module-csv

import csv, os

folder_path = os.path.dirname(__file__)
csv_path = os.path.join(folder_path, "MOCK_DATA.csv")

with open(csv_path) as csv_file:
    csv_file_data_from_reader = csv.reader(csv_file)
    for data in csv_file_data_from_reader:
        print(data)

with open(csv_path) as csv_file:
    csv_file_data_from_dict_reader = csv.DictReader(csv_file)
    for data2 in csv_file_data_from_dict_reader:
        print(data2)
