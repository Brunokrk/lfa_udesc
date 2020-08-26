dicio = {'X': [ 'A', 'B'], 'Y': ['C', 'D']}
value = 'A'
for k in dicio:
    if value in dicio[k]:
        value = k
        print(value)

