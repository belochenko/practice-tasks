import numpy as np
import csv
import re


def function(f):
    with open(f, 'r') as data:
        reader = csv.reader(data, delimiter=",")
        reader = list(reader)
        reader = [[int(x) for x in line] for line in reader]
        reader[0][0] = np.sum(reader)
        reader = [[int(y) for y in x] for x in reader]
        formate = re.sub('], +', '\n', str(reader))
        formate = re.sub('[\[\]]+', '', formate)
        with open("output.csv", "w") as f:
            f.write(formate)


file = "input.csv"
function(file)
