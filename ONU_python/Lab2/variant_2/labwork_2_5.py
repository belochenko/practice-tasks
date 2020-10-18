import numpy as np
import csv


def function(f):
    with open(f) as data:
        reader = csv.reader(data, delimiter=",")
        reader = list(reader)
        #reader = [int(x) for x in reader[0]]
        reader1 = reader.astype(int)
        mid = np.mean(reader)
        index = np.argmax(reader)
        reader[index] = mid
        reader = [str(x) for x in reader]
        formate = ','.join(reader)
        f = open("output.csv", "w")
        f.write(formate)
        f.close()
    

file = "../variant_3/input.csv"
function(file)
