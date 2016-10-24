import scipy as SP

ins = open("map.txt","r")
data = []
for line in ins:
	number_strings = line.split()
	numbers = [float(n) for n in number_strings]
	data.append(numbers)

data = SP.array(data)
static = SP.zeros([140, 200])

size = static.shape
row = size[0]
col = size[1]

exit = [(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0)]

for i in range(row):
	for j in range(col):
		dist = []
		for des in exit:
			d = abs(i - des[0]) + abs(j - des[1])
			dist.append(d)
		static[i, j] = min(dist)

SP.savetxt('static.txt', static,fmt = '%.1f')