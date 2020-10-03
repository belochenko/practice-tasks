import numpy as np


def cinema_hall(train):
	down = [i[::2] for i in train]
	cnt = 0
	maxcnt = 0
	dic = {}
	for index, lines in enumerate(down, start=1):
		for num in lines:
			if num == 0: 
				cnt += 1
			else:
				maxcnt = max(cnt, maxcnt)
				cnt = 0
				dic.update({index:maxcnt})
				
	return max(dic, key=dic.get)
	