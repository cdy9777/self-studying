# 서울 지하철 최대 유인승차 비율
import csv

f = open('subwayfee.csv', 'r', encoding='utf-8')
data = csv.reader(f)
next(data)
Paid_ride_per = 0
loc = ''
line_num = ''
for row in data:
    row[4:8] = [int(row[4]), int(row[5]), int(row[6]), int(row[7])]
    if row[4] + row[6] >= 100000:
        rate = round(row[4] * 100 / (row[4] + row[6]), 2)
        row.append(rate)
        if rate > Paid_ride_per:
            Paid_ride_per = rate
            loc = row[3]
            line_num = row[1]
    else:
        continue

print(loc, line_num, Paid_ride_per)

# 서울 지하철 승차/하차 별 최다 역
# import csv

# f = open('subwayfee.csv', 'r', encoding='utf-8')
# data = csv.reader(f)
# next(data)

# mx = [0]*4
# mx_station = [''] * 4

# for row in data:
#     for i in range(4,8):
#         row[i] = int(row[i])
#         if mx[i-4] < row[i]:
#             mx[i-4] = row[i]
#             mx_station[i-4] = row[3] + ' ' + row[1]

# print('유인승차 최다 역: ' + mx_station[0], mx[0])
# print('유인승차 최다 역: ' + mx_station[1], mx[1])
# print('무인승차 최다 역: ' + mx_station[2], mx[2])
# print('무인하차 최다 역: ' + mx_station[3], mx[3])

# 지하철 역+노선 승차/하차 비용 비율
# import csv
# import matplotlib.pyplot as plt

# f = open('subwayfee.csv', 'r', encoding='utf-8')
# data = csv.reader(f)
# next(data)

# loc = input('어떤 역을 검색하시겠습니까?')
# line_num = ''
# per = []
# for row in data:
#     if row[3] == loc:
#         for i in range(4,8):
#             per.append(int(row[i]))
#             line_num = row[1]
#         break
# label = ['유인승차', '유인하차', '무인승차', '무인하차']
# color = ['red', 'green', 'blue', 'white']
# plt.rc('font', family = 'Malgun Gothic')
# plt.title(loc + ' ' + line_num)
# # plt.figure(dpi=100)
# plt.pie(per, labels=label, colors=color, autopct = '%1.f%%' )
# plt.axis('equal')
# plt.savefig(row[3] + ' ' + row[1] + '.png')
# plt.show()
