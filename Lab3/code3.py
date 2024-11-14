def find_duplicate_words(sentence):
    words = sentence.split()
    duplicates = set([word for word in words if words.count(word) > 1])
    return duplicates

sentence = input("Введіть речення: ")

duplicate_words = find_duplicate_words(sentence)
if duplicate_words:
    print("Повторювані слова:", ', '.join(duplicate_words))
else:
    print("Повторюваних слів не знайдено.")

