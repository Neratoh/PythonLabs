countries = {
    "Country1": {"population": 10, "area": 100},
    "Country2": {"population": 20, "area": 150},
    "Country3": {"population": 30, "area": 200},
    "Country4": {"population": 40, "area": 250},
    "Country5": {"population": 50, "area": 300},
    "Country6": {"population": 60, "area": 350},
    "Country7": {"population": 70, "area": 400},
    "Country8": {"population": 80, "area": 450},
    "Country9": {"population": 90, "area": 500},
    "Country10": {"population": 100, "area": 550},
}

def print_all(countries):
    for country, data in countries.items():
        print(f"{country}: Населення - {data['population']} млн, Площа - {data['area']} тис. км²")

def add_country(countries):
    name = input("Введіть назву країни: ")
    population = float(input(f"Введіть населення країни {name} (в мільйонах): "))
    area = float(input(f"Введіть площу країни {name} (в тисячах квадратних км): "))
    countries[name] = {"population": population, "area": area}
    print(f"Добавлено країну: {name}.")

def delete_country(countries):
    name = input("Введіть назву країни, яку потрібно видалити: ")
    if name in countries:
        del countries[name]
        print(f"Видалено країну: {name}.")
    else:
        print(f"Країну {name} не знайдено в словнику.")

def print_sorted(countries):
    sorted_countries = {k: countries[k] for k in sorted(countries)}
    print("Відсортований словник:")
    for country, data in sorted_countries.items():
        print(f"{country}: Населення - {data['population']} млн, Площа - {data['area']} тис. км²")

def country_with_max_density(countries):
    max_density = 0
    country_name = ""
    for country, data in countries.items():
        density = data["population"] / data["area"]
        if density > max_density:
            max_density = density
            country_name = country
    print(f"Країна з максимальною щільністю населення: {country_name}")

while True:
    print("\nОберіть дію:")
    print("1. Вивести всі країни")
    print("2. Додати країну")
    print("3. Видалити країну")
    print("4. Вивести відсортований словник")
    print("5. Визначити країну з максимальною щільністю населення")
    print("6. Вийти")

    choice = input("Ваш вибір: ")

    if choice == '1':
        print_all(countries)
    elif choice == '2':
        add_country(countries)
    elif choice == '3':
        delete_country(countries)
    elif choice == '4':
        print_sorted(countries)
    elif choice == '5':
        country_with_max_density(countries)
    elif choice == '6':
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")
