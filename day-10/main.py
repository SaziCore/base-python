name1 = " иВАН  "
capitaliz_name1 = name1.strip().capitalize()
print(capitaliz_name1)

email = " MyEMAilYandex.Ru  "
clean_email = email.strip().lower()
is_russian = email.endswith(".ru")
is_russian = clean_email.endswith(".ru")
if is_russian: 
    print(f"Почта {clean_email} подтверждена")
else:
    print("Ваша почта не подходит, нужен .ru")

message = "ПРИВЕТ"
is_shouting = message.isupper()
if is_shouting:
    quiet = message.lower()
    print(quiet)
else:
    print("Ты и так спокойно говоришь")

user_nickname = input("Введите ваш ник: ")
clean_nickname = user_nickname.strip()
new_nick = clean_nickname.replace(" ", "_")
print(new_nick)

name = input("Введите ваше имя: ")
if name.isdigit():
    print("Введи имя без чисел!")
else:
    print("Ок")

secret_key = "ID-998877-PROJECT"
numbers = secret_key[3:9]
print(numbers)

news = input("Введите любую новость: ")
clean_news = news.strip().upper()
short_news = clean_news[:10] + "..."
print(short_news)