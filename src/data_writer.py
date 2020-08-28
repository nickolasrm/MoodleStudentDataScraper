import csv

def saveData(data):
    print('Saving data...')

    with open('__outputStudentData.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', 
            quotechar='"', quoting=csv.QUOTE_MINIMAL)

        header = data['headers']['days'] + data['headers']['grades']
        header.insert(0, data['headers']['name'])
        writer.writerow(header)
        for i in range(0, len(data['data'])):
            row = data['data'][i]['days'] + data['data'][i]['grades']
            row.insert(0, data['data'][i]['name'])
            writer.writerow(row)

    print('Saved!')