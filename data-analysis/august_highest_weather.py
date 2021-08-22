import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f)
next(data)

day = []
for i in range(31):
    day.append([])

for row in data:
    if row[4]:
        if row[0].split('-')[1] == '08':
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))

plt.style.use('ggplot')  # 그래프 스타일 지정
plt.figure(figsize=(10, 5), dpi=300)  # 박스크기 수정, dpi는 그래프 해상도
plt.boxplot(day, showfliers=False)  # 아웃라이어 값, 즉 이상치 값 생략
plt.boxplot(day)
plt.show()
