import csv

def open_csv(file_name, mode):
    try:
        file = open(file_name, mode, newline='', encoding='utf-8')
    except Exception as e:
        print(f"Файл {file_name} не вдалося відкрити! Помилка: {e}")
        return None
    else:
        print(f"Файл {file_name} було відкрито!")
        return file

def read_csv(file_name):
    data = []
    try:
        file = open_csv(file_name, "r")
        if file:
            reader = csv.reader(file)
            data = [row for row in reader]
            file.close()
            print(f"Вміст {file_name}:")
            for row in data:
                print(', '.join(row))
    except Exception as e:
        print(f"Не вдалося прочитати {file_name}. Помилка: {e}")
    return data

def write_csv(file_name, data):
    try:
        file = open_csv(file_name, "w")
        if file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)
            file.close()
            print(f"Дані успішно записано до {file_name}!")
    except Exception as e:
        print(f"Не вдалося записати до {file_name}. Помилка: {e}")

def search_country(data, country_name):
    headers = data[0]
    for row in data[1:]:
        if row[0].strip().lower() == country_name.strip().lower():
            return [headers, row]
    return []

def main():
    input_file = "data.csv"
    output_file = "search_results.csv"

    # Зчитування та виведення вмісту CSV файлу
    data = read_csv(input_file)

    if not data:
        return

    # Введення назви країни для пошуку
    country_name = input("Введіть назву країни для пошуку: ")

    # Пошук даних для введеної країни та запис результатів у новий CSV файл
    search_results = search_country(data, country_name)
    if search_results:
        write_csv(output_file, search_results)
    else:
        print(f"Дані для країни {country_name} не знайдено")

if __name__ == "__main__":
    main()


