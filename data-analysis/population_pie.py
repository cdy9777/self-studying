import csv
import matplotlib.pyplot as plt

f = open('gender.csv')
data = csv.reader(f)
next(data)
m = 0
fe = 0
loc = input('현재 살고 계신곳은 어디신가요? :')

for row in data:
    if loc in row[0]:
        for i in range(0, 101):
            m += int(row[i+3].replace(',', ''))
            fe += int(row[-i-1].replace(',', ''))
        break

gender = ['Man', 'Woman']
pop_data = [m, fe]
color = ['blue', 'red']

plt.rc('font', family='Malgun Gothic')
plt.axis('equal')
plt.pie(pop_data, labels=gender, colors=color, autopct='%.1f%%', startangle=90)
plt.legend()
plt.show()

# pie 그래프
# import matplotlib.pyplot as plt
# size = [2441,2312,1031,1233]
# label = ['A', 'B', 'AB', 'O']
# color = ['red', 'orange', 'yellow', 'green']
# plt.rc('font', family = 'Malgun Gothic')
# plt.axis('equal') #동그란 원을 그릴 수 있음
# plt.pie(size, labels=label, autopct = '%.1f%%', colors = color, explode=(0,0,0.5,0))
# plt.legend()
# plt.show()
