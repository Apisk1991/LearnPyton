import re


spisok2 = []
spisok3 = []
spisok = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for element in spisok:
    add_elem = re.sub(r"(?<!\d|\.)\d(?!\d)", r"0\g<0>" , element)
    match = re.search(r"\d+", add_elem)
    if match is not None:
        spisok2.append("'")
        spisok2.append(add_elem)
        spisok2.append("'")
    else:
        spisok2.append(add_elem)
print(spisok2)
# print(spisok3)

