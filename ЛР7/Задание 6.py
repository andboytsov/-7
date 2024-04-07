def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

user_input = input("Введите строку для проверки на палиндром: ")
if is_palindrome(user_input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")
