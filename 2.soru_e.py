from matplotlib import pyplot as plt
import numpy as np

a = np.array([514, 476, 497, 511, 484, 513, 471, 470, 441, 466, 443, 481, 502, 528, 459, 548, 521, 517,
463, 478, 473, 514, 542, 519, 522, 523, 546, 487, 486, 473, 527, 470, 440, 564, 499, 523,
484, 463, 461, 437, 555, 525, 461, 539, 466, 470, 486, 490, 543, 519])

fig, ax = plt.subplots(figsize =(10, 6))
n, bins, patches = ax.hist(a, bins=[437, 453, 469, 485, 501, 517, 533, 549, 565], color="blue", edgecolor='k', fill=True)
#normal frekans değerleri üzerinde özelliştirme yapmak için n ve patches ekledik
plt.xlabel('Maaşlar')
plt.ylabel('Frekans')
plt.title('Maaşların Frekansları Histogramı')

sinif_araligi = bins[1:] - bins[:-1] # her aralık genişliğini hesapladık
yuzdesel = sinif_araligi / np.sum(sinif_araligi) * 100 # yüzdelik frekanslarını hesapladık

plt.show()




