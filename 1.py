def utility(F):

    dct = dict()
    for i in range(97,123):
        try:
            lower = max(ord(temp) for temp in F if ord(temp) <= i)
        except:
            lower = ord(F[-1])

        try:
            upper = min(ord(temp) for temp in F if ord(temp) >= i)
        except:
            upper = ord(F[0])
        
        if i - lower >= 0:
            lowerop = i - lower
        else:
            lowerop = i - lower + 26

        if upper - i >= 0:
            upperop = upper - i
        else:
            upperop = upper - i + 26

        dct[chr(i)] = min(lowerop, upperop)
    
    return dct

T = int(input())

for i in range(T):
    S = input()
    F = input()

    tempf = []
    for k in F:
        tempf.append(k)

    dct = utility(tempf)

    operation = 0
    for j in S:
        operation += dct[j]

    print("Case #{}:".format(i+1), operation)

        
