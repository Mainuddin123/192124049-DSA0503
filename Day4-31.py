import numpy as np
import matplotlib.pyplot as plt

groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
std_dev_men = [4, 3, 4, 1, 5]
std_dev_women = [3, 5, 2, 3, 3]

bar_width = 0.35

x = np.arange(len(groups))

plt.bar(x, means_men, bar_width, label='Men', yerr=std_dev_men, color='lightblue', edgecolor='black', capsize=5)
plt.bar(x, means_women, bar_width, label='Women', yerr=std_dev_women, bottom=means_men, color='lightcoral', edgecolor='black', capsize=5)

plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Error Bars')
plt.xticks(x, groups)
plt.legend()
plt.show()
