i = 2
while i < 10:
    j = 1   # i=2, j=1 이고 i=3, j=1
    while j < 10:
        print(f'{i} * {j} = {i*j}')
        j += 1
    i += 1
