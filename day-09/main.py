numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[:3])

alfavit ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alfavit[::2])

text = input("Введите любой текст:")
print(text[::-1])

days = ["День 1", "День 2", "День 3", "День 4", "День 5"]
print(days[::-1])

scores = [45, 52, 78, 91, 23, 64, 88, 12, 33, 99]
first = scores[:1]
last = scores[-1:]
print(first + last)

users = ["Alex", "Ivan", "Oleg", "Dima", "Anna", "Egor", "Yura"]
print(users[::2])

s = "PythonIsCool"
ss = s[0:6]
sss = s[-4:]
print(ss + sss)

code = "1А2Б3В4Г5Д6Е7Ё8Ж"
digits = code[::2]
print(digits)

temps = [18, 22, 25, 30, 28, 24, 19]
middle_temps = temps[1:-1]
print(middle_temps)

a = [1, 2, 3]
b = a[:]
b[0] = 99
print("Список a:", a)
print("Список b:", b)