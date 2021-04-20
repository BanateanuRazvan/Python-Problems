def findJudge(N, trust):
    list={}
    for i in range(1,N+1):
        list[i]=[]
    for i in range(len(trust)):
        list[trust[i][0]].append(trust[i][1])
    isThisJudge=0

    for i in range (1,N+1):

        if list[i]==[]:
            isThisJudge = i
    if isThisJudge==0:
        return -1
    else:
        ok=1
        for i in range (1,N):
            if isThisJudge not in list[i] and i!=isThisJudge:
                return -1
    
    return isThisJudge
   


N=3
trust=[[1,2],[2,3]]

judge = findJudge(N,trust)

print(judge)