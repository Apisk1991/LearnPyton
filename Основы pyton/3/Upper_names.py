# f = "Марина"
# g = f[0]
# d = dict.fromkeys([g], f)
# print(d)

# for key in dict.keys():
# for key in dict.values():

def thesaurus(*args):
    result = {}
    for arg in args:
        gkey = arg[0]
        if gkey not in result.keys():
            result[gkey] = [arg]
        else:
            result[gkey].append(arg)
    return result


print(thesaurus("Марина", "Иван", "Гога", "Миша"))





