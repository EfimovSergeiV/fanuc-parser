"""
Зависимость для этого примера:
pip install matplotlib

Строим график из двух сварок, собранных в SQLite базу данных
"""

import sqlite3
import matplotlib.pyplot as plt


conn = sqlite3.connect(f'26-data.db')   # Путь до базы данных 2X-data.db
cursor = conn.cursor()

cursor.execute("SELECT * from welding")
data = cursor.fetchall()

times = []
gin2 = [] # Вольтаж !
gin3 = [] # Ток !
gin4 = [] # Скорость подачи проволоки 
gin5 = [] # Ток двигателя
gout2 = [] # Номер работы
gout3 = [] # Скорость подачи проволоки 2
gout4 = [] # Коррекция напряжения
gout5 = [] # Динамика
pns = [] # PNS

for weld in data:
    times.append(weld[13])
    gin2.append(int(weld[3]) / 320)
    gin3.append(int(weld[4]) / 30.5)
    gout2.append(int(weld[8]))


fig, ax = plt.subplots()
plt.style.use('_mpl-gallery')

ax.plot([i for i in range(0,len(times),1)], gin3, linewidth=1, color='#166534', label='Current')
ax.plot([i for i in range(0,len(times),1)], gin2, linewidth=1, color='#880808', label='Voltage')
ax.grid(True)

plt.legend(loc='best', fontsize=14)
plt.show()
conn.close()