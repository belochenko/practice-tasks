import re 

def less_three():
    open_file = open('input.txt', 'r')
    data = open_file.read()
    res = re.sub(r'\b\w{1,3}\b', '', data)
    open_file.close()

    f = open("output.txt", "w")
    f.write(res)
    return(res)
    f.close()
    