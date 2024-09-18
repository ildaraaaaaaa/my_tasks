# 1) Дано трехзначное число. Найти сумму и произведение его цифр.
# 2) Дано трехзначное число. Вывести число, полученное при прочтении исходного числа справа налево.
# 3) Дано трехзначное число. В нем зачерква цифру и приписали ее справа. Вывести полученное число.
# 4) Даны целые положительные числа A и B (A нули первую сле> B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). Используя операцию деления нацело, найти количество отрезков B, размещенных на отрезке AB.
# 5) Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок стоит B рублей. Определить, сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок.
# 6) Даны два круга с общим центром и радиусами R1 и R2 (R1 > R2). Найти площади этих кругов S1 и S2, а также площадь S3 кольца, внешний радиус которого равен R1, а внутренний радиус равен R2.

# 1st-3th programs
number = input("Введите ваше число: ")
if len(number) == 3:
    print("Сумма:", int(number[0]) + int(number[1]) + int(number[2]))
    print("Произведение:", int(number[0]) * int(number[1]) * int(number[2]))

    # 2nd program
    number = int(number)
    print(f"{number % 10}{int(number / 10) % 10}{int(number / 100)}")

    # 3rd program
    print(f"{number % 100}{int(number / 100)}")
else:
    print("Число не подходит под условие")

# 4th program
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
if A > B > 0:
    print("Количество вмещаемых B отрезков на отрезке AB:", int(A / B))
else:
    print("По условию задачи A > B , также они должны быть положительными")

# 5th program верное решение
X = int(input("Ввидете количество конфет, кг: "))
A = int(input("Ввидете ценну за взятое количество конфет, руб.: "))
Y = int(input("Ввидете количество ирисок, кг: "))
B = int(input("Ввидете ценну за взятое количество ирисок, руб.: "))
print("Ценна за 1кг конфет: ", A / X)
print("Ценна за 1кг ирисок: ", B / Y)
print("Шоколадные конфеты дороже ирисок в", round((A / X) / (B / Y)), "раза")

# 6th program верное решение
R1 = int(input("Радиус первого круга, R1: "))
R2 = int(input("Радиус второго круга, R2: "))
if R1 > R2:
    S1 = int(3.14 * (R1 ** 2))
    S2 = int(3.14 * (R2 ** 2))
    print("Площади кругов S1 и S2:", S1, "и", S2)
    print("Площадь кольца S3:", S1 - S2)
else:
    print("Значение R1 должно быть больше R2")
