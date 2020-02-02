for i in range(1, 11):
    for j in range(1, 11):
        while True:
            print( i, 'x', j, '= ?' )
            r = int(input())
            if r == i*j:
                break