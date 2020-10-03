E = float(input('Enter precision Е: '))
p = []
first_val, second_val  = 2/3, 5/6
p.append(first_val)
p.append(second_val)
ans = p[0] * p[1]
dif = p[1] - p[0]
n = 3
i = 1
while (dif > E):
    n += 1
    val = 1 - 2/(n*(n+1))
    p.append(val)
    ans *= val
    dif = p[i + 1] - p[i]
    i += 1

print(f'Answer = {ans}')

