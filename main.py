import tabula import read_pdf

json = read_pdf('test.pdf', output_format='json')
json = json[0]
data = json['data']

roll_nos = []

for row in data:
    for entry in row:
        roll_nos.append(entry['text'])


