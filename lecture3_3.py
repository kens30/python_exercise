for i in range(6):
    asterCount = pow(i, 2)
    tmpAster = str(i) + ':'
    for o in range(asterCount):
        tmpAster = tmpAster + '*'
    print(tmpAster)
