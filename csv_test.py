import csv
# with open('new.csv', 'r', encoding='UTF8') as csv_file:
#      csv_reader = csv.reader(csv_file, delimiter='-')
#      print(csv_reader)
# #
#      next(csv_reader)
#      for line in csv_reader:
#          print(line)
#          # print(line[0])

# with open('test.csv', 'r', encoding='UTF8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('new.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='-',lineterminator='\n')
#
#         for line in csv_reader:
#             csv_writer.writerow(line)

with open('test.csv', 'r', encoding='UTF8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # next(csv_reader)
    for line in csv_reader:
        print(line)
        # print(line[0])