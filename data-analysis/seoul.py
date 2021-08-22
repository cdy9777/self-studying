import csv

f = open('seoul.csv', 'r', encoding='cp949')  # cp949는 window 한글 인코딩 방식
data = csv.reader(f, delimiter=',')  # delimiter는 구분자

high_temp = 0
high_temp_day = '1904-01-01'

for row in data:
    if row[4]:
        high_temp = max(high_temp, float(row[4]))
        if high_temp == float(row[4]):
            high_temp_day = row[0]
    else:
        continue

print('서울이 가장 더웠던 날 :', high_temp_day, '(최고기온 :', high_temp, ')')

f.close()
