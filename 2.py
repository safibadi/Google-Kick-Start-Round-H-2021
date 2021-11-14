T = int(input())

for i in range(T):
    N = int(input())
    P = input()

    count1 = 0
    previous = "U"
    for j in P:

        if j in {"B","A","G","P"}:
            if previous in {"B","A","G","P"}:
                previous = j
                continue

            else:
                count1 +=1
                previous = j
        else:
            previous = j

    count2 = 0
    previous = "U"
    for j in P:
        if j in {"Y","A","G","O"}:
            if previous in {"Y","A","G","O"}:
                previous = j
                continue

            else:
                count2 +=1
                previous = j

        else:
            previous = j

    count3 = 0
    previous = "U"
    for j in P:
        if j in {"R","A","O","P"}:
            if previous in {"R","A","O","P"}:
                previous = j
                continue

            else:
                count3 +=1
                previous = j  

        else:
            previous = j

    #print(count1,count2,count3)
    print("Case #{}:".format(i+1), count1+count2+count3)
        
