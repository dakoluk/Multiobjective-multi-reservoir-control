import numpy as np
import matplotlib.pyplot as plt
import os
#C:\Users\dakoluk\Documents\Multiobjective-multi-reservoir-control\ZambeziSmashPython\data\qKafueFlats_1January1974_31Dec2005.txt
#C:\Users\dakoluk\Documents\Multiobjective-multi-reservoir-control\ZambeziSmashPython\data\qKafueFlats_1January2020_31Dec2100.txt
#os.chdir('../data')
data=np.loadtxt('qKafueFlats_1January2020_31Dec2100.txt')
fontsize=30
n_months=12
n_years=80
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
data=np.reshape(data, (n_years, n_months))
mean=np.mean(data, axis=0)

plt.plot(mean)
plt.xticks(np.arange(n_months),months, rotation=30, fontsize=fontsize)
plt.show()