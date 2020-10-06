import numpy as np
import csv

def function(file):
    with open(file) as data:
        reader = csv.reader(data, delimiter = ",")
        reader = list(reader)
        reader = [int(x) for x in reader[0]]
        reader[0, 0] = np.sum(reader)
        reader = [str(x) for x in reader]
        formate = ','.join(reader)
        f = open("output.csv", "w")
        f.write(formate)
        f.close()
    

file = "input.csv"
function(file)