T = int(input())

for i in range(T):
    N = int(input())
    S = input()

    previousS = ""
    currentS = S

    while previousS != S:
        previousS = S
        while "01" in S:
            S = S.replace("01","2")

        while "12" in S:
            S = S.replace("12","3")

        while "23" in S:
            S = S.replace("23","4")

        while "34" in S:
            S = S.replace("34","5")

        while "45" in S:
            S = S.replace("45","6")

        while "56" in S:
            S = S.replace("56","7")
        
        while "67" in S:
            S = S.replace("67","8")

        while "78" in S:
            S = S.replace("78","9")

        while "89" in S:
            S = S.replace("89","0")

        while "90" in S:
            S = S.replace("90","1")

    print("Case #{}:".format(i+1), S)