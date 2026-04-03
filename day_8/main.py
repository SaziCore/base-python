money = ["USD", "EUR", "GBP", "BYN", "RUB"]  
money[1] = "CNY"
money.append("TRY")
money.insert(0, "Валюты в мире: ")
money.pop(3)
money.remove("RUB")
print(money)
print(*money)

pet = ["корова", "собака", "кот", "свинка", "гусь", "хомяк",]
pet[-1] = "морская свинка"
pet.append("Лошадь")
pet.pop(4)
pet.insert(3, "гусь")
pet.remove("кот")
print(*pet)
