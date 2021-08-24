# 시간대 별 지하철 최대 승/하차 역(호선)
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv', 'r', encoding='utf-8')
data = csv.reader(f)
next(data)
next(data)
mx = [0] * 21
mx_station = [''] * 21

for row in data:
    row[4:] = map(int, row[4:])
    for i in range(4, 25):
        people = row[4 + (i-4) * 2] + row[5 + (i-4) * 2]
        if people > mx[i-4]:
            mx[i-4] = people
            mx_station[i-4] = '(' + str(i) + '시)' + row[3] + ' ' + row[1]

plt.title('시간대 별 지하철 최다 승하차 역& 호선 & 인원')
plt.rc('font', family='Malgun Gothic')
plt.bar(range(21), mx)
plt.xticks(range(21), mx_station, rotation=90)
plt.show()


# 시간대별 지하철 승차 인원
# import csv
# import matplotlib.pyplot as plt

# f = open('subwaytime.csv', 'r', encoding='utf-8')
# data = csv.reader(f)
# next(data)
# next(data)
# s_in = [0] * 21
# s_out = [0] * 21

# for row in data:
#     row[4:] = map(int, row[4:])
#     for i in range(4,25):
#         s_in[i-4] += row[4+(i-4)*2]
#         s_out[i-4] += row[5+(i-4)*2]

# plt.style.use('ggplot')
# plt.rc('font', family = 'Malgun Gothic')
# plt.title('지하철 시간대별 승하차 인원 추이')
# plt.xticks(range(21), range(4,25))
# plt.plot(s_in, label='승차')
# plt.plot(s_out, label='하차')
# plt.legend()
# plt.show()
