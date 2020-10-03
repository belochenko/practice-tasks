def limit_of_symbols():
    with open('input.txt', 'r') as input_file:
        data = list(input_file.read())
        space_index = 0

        for index, symbol in enumerate(data):
            if symbol == ' ':
                space_index = index

            if index != 0 and index % 39 == 0:
                data[space_index] = '\n' 

        formate = ''.join(data)
        f = open("output.txt", "w")
        f.write(formate)
        f.close()

limit_of_symbols()
