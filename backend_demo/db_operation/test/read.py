def read(str):
	with open(str) as f:
		res = []
		alldoc = f.read()
		items = alldoc.split('\n')
		dict = {}
		for item in items[0:1]:
			for i in range(0, len(item.split(','))):
				dict['{}'.format(i)] = item.split(',')[i]


		for item in items[1:]:
			temp = {}
			terms = item.split(',')
			for i in range(0, len(terms)):
				temp[dict['{}'.format(i)]] = terms[i]
			res.append(temp)

	return res

