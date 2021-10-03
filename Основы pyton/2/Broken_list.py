import re


broken_list = ['инженер-конструктор Игорь',
               'главный бухгалтер МАРИНА',
               'токарь высшего разряда нИКОЛАй',
               'директор аэлита']
for line in broken_list:
    match = re.search(r"[а-яА-Я]+$", line)
    result = match.group()
    result = result.lower()
    result = result[0].upper() + result[1:]
    print("Привет,", result + "!")

