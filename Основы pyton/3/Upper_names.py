import re
import pprint

# f = "Марина"
# g = f[0]
# d = dict.fromkeys([g], f)
# print(d)

# for key in dict.keys():
# for key in dict.values():

#словарь, значения которого словарь

def thesaurus_adv(*args):
    result = {}
    for arg in args:
        match = re.search(r"([А-Яа-я])[А-Яа-я]+ ([А-Яа-я])[А-Яа-я]+", arg)
        surname_key = match.group(2)
        name_key = match.group(1)
        if surname_key not in result.keys():
            result[surname_key] = {name_key: [arg]}
        else:
            if name_key not in result[surname_key].keys():
                result[surname_key][name_key] = [arg]
            else:
                result[surname_key][name_key].append(arg)
    return result


pprint.pprint(thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова", "Петр Алексеев",
                            "Илья Иванов", "Анна Савельева", "Василий Суриков"))





