def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    num_vowels = 0
    num_consonants = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            elif char in consonants:
                num_consonants += 1

    return num_vowels, num_consonants

input_string = input("Введите строку: ")
vowels, consonants = count_vowels_and_consonants(input_string)

print("Количество гласных букв:", vowels)
print("Количество согласных букв:", consonants)
