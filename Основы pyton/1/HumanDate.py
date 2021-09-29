# Задание по переводу секунд в минуты, часы, дни
# 1 min 60 sec
# 1 hour 3600 seconds
# 1 day	86400 seconds


dur = int(input('Введите число'))

if dur >= 86400:
    day = dur // 86400
    dur = dur % 86400
    print(day, "дн. ")
if dur >= 3600:
    hour = dur // 3600
    dur = dur % 3600
    print(hour, "час. ")
if dur >= 60:
    min = dur // 60
    dur = dur % 60
    print(min, "мин. ")
    print(dur, "сек. ")





