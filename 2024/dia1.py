f = open("input1.txt", "r")
left = []
right = []
for ln in f:
	vals = ln.split()
	left.append(vals[0])
	right.append(vals[1])

left.sort()
right.sort()
qtd = len(left)

soma = 0
for x in range(0, qtd):
	print(left[x] + "   " + right[x])
	soma = soma + (abs(int(right[x]) - int(left[x])))

print(soma)
