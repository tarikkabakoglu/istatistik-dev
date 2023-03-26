import matplotlib.pyplot as plt

frekanslar = [6, 23, 30, 35, 32, 48, 42, 40, 28, 27, 26, 14, 10.8, 4.4, 0.8]
sinirlar = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 35, 40, 45]

fig, ax = plt.subplots()
ax.hist(sinirlar[:-1], bins=sinirlar, weights=frekanslar, edgecolor='black')

plt.xlabel('Değerler')
plt.ylabel('Frekans')
plt.title('Frekans Tablosu Histogramı')

plt.show()
