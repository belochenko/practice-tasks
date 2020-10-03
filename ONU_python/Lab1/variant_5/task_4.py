import string

def analysis():
    input_file = open('input.txt', 'r').read().lower()

    punc = string.punctuation

    for p in punc:
        input_file.replace(p, '')

    feq = {}
    without_space = input_file.split(' ')
    for word in without_space:
        if len(word) in feq.keys():
            count = feq[len(word)]
            count += 1
            feq.update({len(word):count})
        else:
            feq.update({len(word):1})

    l_dict = {i:feq[i] for i in feq.keys() if feq[i] != 0}

    sum = 0
    for words in l_dict.keys():
        sum += round(l_dict[words]/len(without_space) * 100, 4)
        print(f'{words} - {round(l_dict[words]/len(without_space) * 100, 4)}%')
    


analysis()