import random
import re


prices = [str(round(random.random() * 100, 2)) for _ in range(10)]
prices2 = prices.copy()
prices2.sort(reverse=True)
for n in prices:
    match = re.search(r"(\d+)\.(\d+)", n)
    rubl = match.group(1)
    kopps = match.group(2)
    if len(kopps) <= 1:
        kopps = kopps + "0"
        print(kopps)
    print(rubl + "руб", kopps + "коп")
print(prices2)
for elem in prices2[-9:-4]:
    print(elem)