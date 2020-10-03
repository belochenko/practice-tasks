import string


def analysis():
    input_file = open('input.txt', 'r').read().lower()
    a = string.ascii_letters + string.digits + string.punctuation

    feq = {}
    for char in a:
        feq.update({char:input_file.count(char)})

    l_dict = {i:feq[i] for i in feq.keys() if feq[i] != 0}

    sum = 0
    for char in l_dict.keys():
        sum += round(l_dict[char]/len(input_file) * 100, 4)
        print(f'{char} - {round(l_dict[char]/len(input_file) * 100, 4)}%')

    print(f'Пробелов в тексте {round(100 - sum, 4)}%')

analysis()