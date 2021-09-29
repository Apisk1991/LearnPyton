# Реализовать склонение слова «процент» для чисел до 20. «5 процентов», «2 процента». Вывести все склонения для проверки.
percent = 0
end = ""
# while percent < 21:
for percent in range(21):
    if 10 < percent < 20:
        end = "ов"
    elif percent % 10 == 1:
        end = ''
    elif (percent % 10) in (0, 5, 6, 7, 8, 9):
        end = "ов"
    elif (percent % 10) in (2, 3, 4):
        end = "а"


    print(percent, 'процент' + end)


   