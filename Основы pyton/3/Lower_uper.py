spisok = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "zero": "ноль",
    "ten": "десять",



def num_translate(parametr1):
    all_lower_case = parametr1.lower()
    if parametr1[0].isupper():
        return spisok[all_lower_case][0].upper() + spisok[all_lower_case][1:]
    if parametr1 in spisok.keys():
        return spisok[parametr1]
    else:
        return None



print(num_translate("One"))
print(spisok.keys())