
import re
#!pip install csv
import csv 

def clean_naw(input_string):
    output = re.sub("\S*@\S*\s?", "", input_string) # zoekt mail adressen
    output = re.sub("\w*\d{1,}\w*", "", output) # zoekt combinaties met cijfers
    return output
    
output = "output.csv"
with open('input.csv', "r+", encoding= 'utf-8', newline='') as file, open(output, "w+", encoding='utf-8', newline='') as outFile:
    reader = csv.reader(file, delimiter=';')
    writer = csv.writer(outFile, delimiter=';')
    header = next(reader)
    writer.writerow(header)
    for row in reader:
        colValues = []
        for col in row:
            if col:
                colValues.append(clean_naw(col).strip('\n'))
        writer.writerow(colValues)

