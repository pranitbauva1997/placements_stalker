import sys

import tabula


def get_map(filename):
    map_roll_no_to_name = {}

    with open('students.csv') as f:
        students_raw = f.read()
        students = students_raw.split('\n')
        for student in students:
            student = student.split(',')

            if student[0] == '':
                continue

            if len(student) < 3:
                continue

            map_roll_no_to_name[student[0]] = (student[1][3:], student[2])

    with open('students_hall.csv') as f:
        students_raw = f.read()
        students = students_raw.split('\n')
        for student in students:
            student = student.split(',')

            if student[0] == '':
                continue

            if len(student) < 3:
                continue

            temp1, temp2 = map_roll_no_to_name[student[0]]
            map_roll_no_to_name[student[0]] = (temp1, temp2, student[4])

    return map_roll_no_to_name

json = tabula.read_pdf(sys.argv[1], output_format='json')
json = json[0]
data = json['data']

roll_nos = []

for row in data:
    for entry in row:
        roll_nos.append(entry['text'])

mapping = get_map('students.csv')

for student in roll_nos:
    try:
        print(student + ': ' + str(mapping[student]))
    except Exception as e:
        continue


