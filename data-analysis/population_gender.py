import csv
import matplotlib.pyplot as plt

f = open('gender.csv', 'r', encoding='cp949')
data = csv.reader(f)
next(data)
m = []
fe = []
loc = input('현재 살고 계신곳은 어디신가요? :')

for row in data:
    if loc in row[0]:
        for i in range(0, 101):
            m.append(-int(row[i+3].replace(',', '')))
            fe.append(int(row[-i-1].replace(',', '')))
        break
fe.reverse()

plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
plt.title(loc + ' 성별 인구 분포')
plt.rcParams['axes.unicode_minus'] = False
plt.barh(range(101), m, color='blue', label='남')
plt.barh(range(101), fe, color='red', label='여')
plt.legend()
plt.show()

# plt.figure(figsize = (5,20))
# plt.yticks(range(101))
