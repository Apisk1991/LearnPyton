# Для кубов нечётных чисел от 1 до 1000. Вычислить сумму и вывести на экран те числа,
# сумма цифр которых делится нацело на 7
# Вывести в формате: число: хххххххх sum: xxx
#
# 1 вычислить остатки от деления
# 2 сложить остаток с другими остатками
# 3 поделить результат на 7 без остатка
# 4 вывести число и сумму

# num = int(input("Введите целое: "))
# sum = 0
# while (num != 0):
#     sum = sum + num % 10
#     num = num // 10
# print("Сумма цифр числа равна: ", sum)
#
#
import tqdm

n = 1
p = 0
seven = tuple([item for item in range(7, 7 * 10 + 1, 7)])
for n in tqdm.trange(1, 1001, 2):
    kub = n ** 3
    textkub = str(kub)
    summa = 0
    for element in textkub:
        summa += int(element)
    # if summa in seven:
    if summa % 7 == 0:
        print(n, textkub, summa)
        pass
    # n = n + 2



