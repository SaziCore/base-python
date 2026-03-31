total_spend = float(input("Сколько денег вы потратили за месяц: "))

if total_spend >= 15000:
    print("Ваш статус: LEGEND, скидка — 15%")
elif total_spend >= 5000:
    print("Ваш статус: VIP, скидка — 10%")
elif total_spend >= 1000:
    print("Вы постоянный клиент, скидка — 5%")
else:
    print("Вы новичок, скидка — 0%")

temperat = float(input("Напишите температуру на улице: "))
if temperat >= 30:
    print("Наденьте шорты!")
elif temperat >= 15:
    print("Комфортно, можно в футболке!")
elif temperat >= 0:
    print("Прохлодно, накиньте куртку")
else:
    print("На улице мороз, одевайтесь тепло!")

dnevnik = int(input("Какую оценку сегодня получили?: "))
if dnevnik == 5:
    print("Молодец, отличная оценка")
elif dnevnik == 4:
    print("Хорошо, молодец!")
elif dnevnik == 3:
    print("Плоховато, повторяй материал!")
elif dnevnik == 2:
    print("Плохо, иди учись!")
elif dnevnik == 1:
    print("Очень плохо, ты не готов!")
else:
    print("Такой оценки нету...")

km = float(input("Какое расстояние вам нужно преодолеть в км?: "))
if km <= 1:
    print("Пройдитесь пешком...")
elif km <= 5:  
    print("Возьмите велосипед или самокат")
elif km <= 50: 
    print("Едьте на автобусе или машине")
else:
    print("Бегите!!!")

vremya = float(input("Который час? (0-23): "))

if vremya < 5:
    print("Доброй ночи!")
elif vremya < 12:
    print("Доброе утро!")
elif vremya < 18:
    print("Добрый день!")
elif vremya < 23:
    print("Добрый вечер!")
else:
    print("Доброй ночи!") 