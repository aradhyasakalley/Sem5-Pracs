def bestFit(blockSizes,m,processSizes,n) : 
    allocation = [-1]*n
    for i in range(n):
        bestIndex = -1
        
        for j in range(m):
            if blockSizes[j] >= processSizes[i]:
                if bestIndex == -1:
                    bestIndex = j
                elif blockSizes[bestIndex] >= blockSizes[j]:
                    bestIndex = j
                    
        if bestIndex != -1:
            allocation[i] = bestIndex
            blockSizes[bestIndex] -= processSizes[i]
        
    print("PNo...PSize...BNum")
    for i in range(n):    
        print(i+1,"    ",processSizes[i],end="     ")
        if allocation[i] != -1 :
            print(allocation[i]+1)
        else : 
            print("not allocated")
            
    


if __name__ == '__main__' :
    blockSizes = [100, 500, 200, 300, 600]
    processSizes = [212,417,112,426]
    m = len(blockSizes)
    n = len(processSizes)
    
    bestFit(blockSizes,m,processSizes,n)