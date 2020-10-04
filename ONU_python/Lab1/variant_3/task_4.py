import math

wordslist = []

with open('../../../../input.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    for letters in data:
        if letters.isalpha() or letters == ' ':
            wordslist += letters

wordslist = ''.join(wordslist).strip().split(' ')
while "" in wordslist:
    wordslist.remove("")

short = []
long = []

for word in wordslist:
    if len(word) < 4:
        short.append(word)
    elif len(word) > 10:
        long.append(word)

shortperc = math.ceil((len(short) * 100)/len(wordslist))
longperc = math.ceil((len(long) * 100)/len(wordslist))

print(f'''Percent of short words is {shortperc}%\nPercent of long words is {longperc}% ''')