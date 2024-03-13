import csv

with open('0students.csv') as f, open('student_new.csv', 'w') as nf:
    data = list(csv.reader(f, delimiter = ';'))
    chel = 'Гарный Никита'
    a = []
    for stroka in data[1:]:
        if chel in stroka:
            print(f'ti poluchil: {stroka[-1]}, za proekt: {stroka[2]}')
        if stroka[-1] != '':
            a.append(int(stroka[-1]))
    mean = round(sum(a) / len(a), 3)
    print(mean)
    res = csv.writer(nf, delimiter = ';')
    for stroka in data:
        if stroka[-1] == '':
            stroka[-1] = str(mean)
        res.writerow(stroka)