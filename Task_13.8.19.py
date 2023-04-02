ticket_1 = 890
ticket_2 = 1390
a = int(input("Введите количество билетов "))
summ = 0
for i in range(a):
    if a < i:
        break
    else:
        d = int(input("Укажите возраст посетителя "))
        if a >= 3:
            ticket_1 = 890 * 0.9
            ticket_2 = 1390 * 0.9
        if d <= 17:
            print("Проход на конференцию бесплатно")
        elif d >= 18 and d < 24:
            summ += ticket_1
            print(ticket_1,"руб.")
        else:
            summ += ticket_2
            print(ticket_2,"руб.")
print("Цена за все билеты", summ, "руб.")






