with open('user.csv') as f:
	res = []
	alldoc = f.read()
	items = alldoc.split('\n')
	dict = {}
	for item in items[0:1]:
		for i in range(0, len(item.split(','))):
			dict['{}'.format(i)] = item.split(',')[i]

	print(dict)
	temp = {}
	for item in items[1:]:
		terms = item.split(',')
		for i in range(0, len(terms)):
			temp[dict['{}'.format(i)]] = terms[i]
			res.append(temp)
	print(res)


		