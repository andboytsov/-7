i = 1
j = 1
while i < 11:
    while j < 11:
        print(i * j, end='\t')
        j += 1
    print('\n')
    j = 1
    i += 1
