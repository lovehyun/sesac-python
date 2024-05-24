import csv

file_path = "mydata.csv"

with open(file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row[0]) # 리스트라서 인덱스로 레퍼런싱 해야함

