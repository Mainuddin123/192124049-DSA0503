import numpy as np
import matplotlib.pyplot as plt

groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]

bar_width = 0.35

x = np.arange(len(groups))

plt.bar(x - bar_width/2, means_men, bar_width, label='Men', color='lightblue')

plt.bar(x + bar_width/2, means_women, bar_width, label='Women', color='lightcoral')

plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(x, groups)
plt.legend()

plt.show()
