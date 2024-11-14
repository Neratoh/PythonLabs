def third_letter(word):
    result = ""
    for i in range(2, len(word), 3):
        result += word[i]
    return result

word = input("Введіть слово: ")

third_letters = third_letter(word)

print("Кожна третя літера:", third_letters)
