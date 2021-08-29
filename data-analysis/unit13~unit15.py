import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

df = pd.read_csv('age.csv', encoding='cp949', index_col=0)
df1 = df.astype(int)
df1 = df1.div(df['2021년07월_계_총인구수'], axis=0)
del df1['2021년07월_계_총인구수'], df1['2021년07월_계_연령구간인구수']
df3 = df1.dropna(axis=0)

name = input('지역명을 입력하세요. :')
location = df1.index.str.contains(name)
df2 = df1[location]


x = df3.sub(df2.iloc[0], axis=1)
y = np.power(x, 2)
z = y.sum(axis=1)
z.dropna(axis=0)
i = z.sort_values().index[:5]
df3.loc[i].T.plot()
plt.show()


# df1.loc[np.power(df1.sub(df2.iloc[0], axis=1),2).sum(axis=1).sort_values().index[:5]].T.plot()
#  18~23 한줄 처리

# unit14
np.seterr(divide='ignore', invalid='ignore')
f = open('age.csv', 'r', encoding='cp949')
data = csv.reader(f)
next(data)
data = list(data)

location = input('인구 구조를 알고 싶은 지역의 이름을 입력해 주세요 :')
loc_age = []

for row in data:
    for i in range(len(row) - 1):
        row[i+1] = row[i+1].replace(',', '')
    if location in row[0]:
        home = np.array(row[3:], dtype=int) / int(row[2])
        continue
    loc_age.append(row)


min_sum = 1000
min_sum_loc = ''
min_sum_loc_plot = 0

for row in loc_age:
    loc_now = np.array(row[3:], dtype=int)/int(row[2])
    sum = np.sum(abs(home - loc_now))

    if min_sum > sum:
        min_sum = sum
        min_sum_loc = row[0]
        min_sum_loc_plot = loc_now

plt.rc('font', family='Malgun Gothic')
plt.title(location + '지역의 인구 구조와 비슷한 인구구조를 가진 지역 :' + min_sum_loc)
plt.plot(min_sum_loc_plot, 'red', label=min_sum_loc)
plt.plot(home, 'blue', label=location)
plt.legend()
plt.show()


# unit 13

x = np.random.randint(-100, 100, 1000)
y = np.random.randint(-100, 100, 1000)
size = np.random.rand(1000)*100

# mask1= abs(x) > 50
# mask2 = abs(y) > 50

# x = x[mask1+mask2]
# y = y[mask1+mask2]

plt.scatter(x, y, s=size, c=size, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()
