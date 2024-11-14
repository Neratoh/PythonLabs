import json

countries = [
    {"Назва": "Україна", "Населення": 41.2, "Площа": 603.5},
    {"Назва": "Німеччина", "Населення": 83.2, "Площа": 357.4},
    {"Назва": "Франція", "Населення": 67.0, "Площа": 643.8},
    {"Назва": "Італія", "Населення": 60.4, "Площа": 301.3},
    {"Назва": "Іспанія", "Населення": 47.4, "Площа": 505.9},
    {"Назва": "Польща", "Населення": 38.3, "Площа": 312.7},
    {"Назва": "Румунія", "Населення": 19.1, "Площа": 238.4},
    {"Назва": "Нідерланди", "Населення": 17.4, "Площа": 41.5},
    {"Назва": "Бельгія", "Населення": 11.5, "Площа": 30.7},
    {"Назва": "Греція", "Населення": 10.4, "Площа": 131.6}
]

jsonData = json.dumps(countries, ensure_ascii=False)
with open("countries.json", "wt", encoding="utf-8") as file:
    file.write(jsonData)

def load_data():
    with open("countries.json", "rt", encoding="utf-8") as file:
        return json.load(file)

def save_data(data):
    jsonData = json.dumps(data, ensure_ascii=False)
    with open("countries.json", "wt", encoding="utf-8") as file:
        file.write(jsonData)

def view_data():
    data = load_data()
    for country in data:
        print(country)

def add_country():
    data = load_data()
    name = input("Назва: ")
    population = float(input("Населення (в мільйонах): "))
    area = float(input("Площа (в тисячах кв. км): "))
    data.append({"Назва": name, "Населення": population, "Площа": area})
    save_data(data)

def delete_country():
    data = load_data()
    name = input("Введіть назву країни для видалення: ")
    data = [country for country in data if country["Назва"] != name]
    save_data(data)

def search_country():
    data = load_data()
    field = input("Пошук за полем (Назва/Населення/Площа): ")
    value = input("Введіть значення для пошуку: ")
    if field in ["Населення", "Площа"]:
        value = float(value)
    results = [country for country in data if country[field] == value]
    for result in results:
        print(result)

def max_density_country():
    data = load_data()
    max_density = -1
    country_name = ""
    for country in data:
        density = country["Населення"] / country["Площа"]
        if density > max_density:
            max_density = density
            country_name = country["Назва"]
    result = {"Країна з максимальною щільністю населення": country_name}
    save_data(data + [result])
    print(result)

while True:
    print("Виберіть опцію:\n 1 - Додати дані\n 2 - Переглянути дані\n 3 - Видалити дані\n 4 - Пошук даних\n 5 - Країна з максимальною щільністю населення\n 6 - Вихід")
    x = int(input("Виберіть опцію: "))
    if x == 1:
        add_country()
    elif x == 2:
        view_data()
    elif x == 3:
        delete_country()
    elif x == 4:
        search_country()
    elif x == 5:
        max_density_country()
    elif x == 6:
        break
