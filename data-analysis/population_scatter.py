import csv
import math
import matplotlib.pyplot as plt

f = open('gender.csv', 'r', encoding='cp949')
data = csv.reader(f)
next(data)

m = []
fe = []
result = []
loc = input('현재 살고 계신곳은 어디신가요? :')

for row in data:
    if loc in row[0]:
        for i in range(0, 101):
            m.append(int(row[i+3].replace(',', '')))
            fe.append(int(row[-i-1].replace(',', '')))
            result.append(
                math.sqrt(int(row[i+3].replace(',', ''))+int(row[i-101].replace(',', ''))))
        break

fe.reverse()

plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
plt.title(loc+' 성별 인구 그래프')
plt.figure(figsize=(10, 5), dpi=300)
plt.scatter(m, fe, c=range(101), s=result, alpha=0.5, cmap='jet')
plt.plot(range(max(m)), range(max(m)),  'g')
plt.xlabel('남성 인구')
plt.ylabel('여성 인구')
plt.colorbar()
plt.show()
