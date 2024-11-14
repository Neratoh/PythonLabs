def function():
    A = input("Введіть текст латинецею: ")

    B = A.lower()
    print("Текст:", B)

    vowels = set("aeiouy")
    consonants = set("bcdfghjklmnpqrstvwxyz")

    vowel_count = len([char for char in B if char in vowels])
    consonant_count = len([char for char in B if char in consonants])

    print("Голосні: ", vowel_count)
    print("Приголосні: ", consonant_count)

    if vowel_count > consonant_count:
        print("Голосних більше")
    else:
        print("Приголосних більше")

    return

function()

