massiv = list(range(5,1,-1))
print(massiv)
n = 0
for element in massiv:
	f = n+1
	if f == len(massiv):
		break
	if massiv[n] < massiv[f]:
		min_el = massiv[n]
	else: 
		min_el = massiv[f]
	print(f'n = {n}, f = {f}')
	n = f
print(min_el)