import matplotlib.pyplot as plt

years = [2005, 2010, 2015, 2020, 2025]
ukraine_data = [5, 3.7, 4, 2.9, 2]
usa_data = [1, 2, 1, 3, 2.2]

plt.plot(years, ukraine_data, label='Україна', color='blue', linewidth=2, linestyle='-')
plt.plot(years, usa_data, label='США', color='red', linewidth=2, linestyle='-')

plt.xlabel('Рік')
plt.ylabel('Кількість дітей, які не відвідують школу (%)')
plt.title('Динаміка показника "Діти, які не відвідують школу" за останні 20 років')

plt.legend()

plt.grid(True)
plt.show()

ukraine_data = [5, 4, 3, 2, 1]
usa_data = [1, 1, 1, 1, 1]

plt.bar(years, ukraine_data, label='Україна', color='blue')
plt.bar(years, usa_data, label='США', color='red', bottom=ukraine_data)

plt.xlabel('Рік')
plt.ylabel('Кількість дітей, які не відвідують школу (%)')
plt.title('Значення показника "Діти, які не відвідують школу" за останні 20 років')
plt.legend()

plt.show()
