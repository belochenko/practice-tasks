import numpy as np
import operator
import random

hall = np.zeros(15*30)
hall[:random.randint(200,351)] = 1
np.random.shuffle(hall)
hall = hall.reshape((15,30))
listhall = [list(d) for d in hall]
cnt = 0
maxcnt = 0
dic = {}
for n,lines in enumerate(listhall, start=1):
    for num in lines:
        if num == 0:
            cnt += 1
        else:
            maxcnt = max(cnt, maxcnt)
            cnt = 0
            dic.update({n:maxcnt})

print(listhall)
#print(max(dic, key=dic.get))