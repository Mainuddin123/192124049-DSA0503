import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(languages, popularity, color='skyblue', edgecolor='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Languages (Oct 2017 vs. a Year Ago)")

plt.grid(True, linestyle='--', linewidth=0.5, color='red', which='major')
plt.grid(True, linestyle=':', linewidth=0.5, color='black', which='minor')

plt.show()
