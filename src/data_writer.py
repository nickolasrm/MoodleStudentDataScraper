import csv

def saveData(data):
    print('Saving data...')

    with open('__outputStudentData.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', 
            quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(data['headers'])
        for row in data['data']:
            writer.writerow(row)

    print('Saved!')