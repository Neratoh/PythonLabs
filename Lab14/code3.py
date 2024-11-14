import matplotlib.pyplot as plt

# Дані про населення
countries = ["Україна", "Німеччина", "Франція", "Італія", "Іспанія", "Польща", "Румунія", "Нідерланди", "Бельгія", "Греція"]
populations = [41.2, 83.2, 67.0, 60.4, 47.4, 38.3, 19.1, 17.4, 11.5, 10.4]

# Створення функції для підписів
def absolute_value(val):
    return int(val / 100.*sum(populations))

# Створення кругової діаграми
plt.pie(populations, labels=countries, autopct=lambda p: '{:.1f}'.format(absolute_value(p)), startangle=140, colors=plt.cm.tab20.colors)

# Додаємо заголовок
plt.title("Населення країн (в мільйонах)")

# Відображаємо діаграму
plt.axis('equal')  # Забезпечити, щоб діаграма була круглою
plt.show()
