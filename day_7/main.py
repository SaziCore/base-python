shoping_list = ["хлеб", "молоко" , "яйца"]
print(len(shoping_list))
print(shoping_list[0])
print(shoping_list[-1])

my_name = "Sazi"
favorite_things =[my_name, 5, "Минск"]
print(my_name[0])
print(favorite_things[-1])

print("Регестрация в системе: ")
name = input("Введите ваше имя: ")
age = (input("Введите ваш возраст: "))
sity = input("В каком городе вы живете?: ")
game1 = input("Любимая игра №1: ")
game2 = input("Любимая игра №2: ")
game3 = input("Любимая игра №3: ")
profil = [name, age, sity, game1, game2, game3]
print(f"Проверьте свои данные: ")
print(f"Имя: {profil[0]}")
print(f"Возраст: {profil[1]}")
print(f"Город: {profil[2]}")
print(f"Ваши любимые игры: {profil[3]}, {profil[4]}, {profil[5]}")
print("-" * 20) 
print("--- Дополнительный анализ ---")
city_start = profil[2][0]
print(f"Твой город начинается на букву: {sity[0]}")
years_to_100 = 100 - int(profil[1])
age_number = int(profil[1])
years_left = 100 - age_number
print(f"Тебе стукнет 100 лет через {years_left} лет!")
if "Dota" in profil or "дота" in profil:
    print("Вижу Доту в списке. Ну ты и тигр!")
else:
    print("Доты нет, но игры отличные.")
user_id = profil[0][0] + profil[2][-1] + profil[1]
print(f"Твой уникальный ID сгенерирован: {user_id}")
if len(profil[0]) > 5:
    print("У тебя довольно длинное имя!")
else:
    print("Имя короткое, легко запомнить.")

