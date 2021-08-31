massiv = [-1,-3,1,0,3,28]
print(massiv)
min_el = massiv[0]
n = 1
for element in massiv:
	if n == len(massiv):
		break
	if min_el >= element:
		min_el = element
	print(f'n = {n}, element = {element}, min_el = {min_el}')
	n += 1
print(min_el)