import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f)
next(data)
high = []
low = []
years = []

for row in data:
    if row[4] and row[3] and row[0]:
        year = row[0].split('-')[0]
        month = row[0].split('-')[1]
        date = row[0].split('-')[2]
        if int(year) < 1998:
            continue
        else:
            if month == '07' and date == '28':
                high.append(float(row[4]))
                low.append(float(row[3]))
                years.append(year[2:])
            else:
                continue

plt.rc('font', family='Malgun Gothic')
plt.title('내 생일 기온 변화')
# plt.rcParams['axes.unicode_minus'] = False 마이너스 부호 깨짐 방지
plt.plot(years, high, 'r', label='highest')
plt.plot(years, low, 'b', label='lowest')
plt.legend(loc=9)
plt.show()
