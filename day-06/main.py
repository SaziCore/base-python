age = True
has_invite = False
if age and has_invite:
    print("Входите")
else:
    print("Вход запрещен")

has_card = False
is_dr = True
if has_card or is_dr:
    print("Скидка 10%")
else:
    print("Скидки нет")

online = False
if not online:
    print("Сервер закрыт")
else:
    print("Сервер работает")

balanc = 5000
banned = False
if balanc >= 4600 and not banned:
    print("Игра на аккаунте!")
else:
    print("Покупка не доступна")

vip_ticket = True
age = 20
pas_tic = True
if (pas_tic and age >= 18) or vip_ticket:
    print("Проходите")
else:
    print("Проход воспрещен!")

button1 = True
button2 = True
error = False
test_mode = False
if (button1 and button2 and not error) or test_mode:
    print("Полетели!")
else:
    print("Полет невозможен")
