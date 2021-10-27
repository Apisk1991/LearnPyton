import requests
import re
import datetime


def currency_rates(Cash):
    original_webpage = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    my_pattern = r">" + Cash + r"<.*?Nominal>(.*?)<.*?Value>(.*?)<"
    match = re.search(my_pattern, original_webpage.text, re.DOTALL)
    Zapyatochka = float(re.sub(r",", ".", match.group(2)))
    _date = re.search(r"ValCurs Date=\"([\d]{2}.[\d]{2}.[\d]{4})\"", original_webpage.text)
    Spisok = _date.group(1).split('.')
    date = datetime.date(day=int(Spisok[0]), month=int(Spisok[1]), year=int(Spisok[2]))
    if match:
        return Zapyatochka / int(match.group(1)), date

Cash_names = ['EUR', "KZT", "DKK", "USD"]
for Name in Cash_names:
    Jopa, piska = (currency_rates(Cash=Name))
    print(Jopa)
print(piska)


# massiv = ['1', 'второй', 'third']
# for elem in massiv:
#     print(elem)
chisla = [shag for shag in range(11)]
# for shag in range(11):
#     chisla.append(shag)
print(chisla)



