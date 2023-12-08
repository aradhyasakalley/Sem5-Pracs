# def bestFit(blockSize, m, processSize, n): 
      
#     # Stores block id of the block  
#     # allocated to a process  
#     allocation = [-1] * n  
      
#     # pick each process and find suitable  
#     # blocks according to its size ad  
#     # assign to it 
#     for i in range(n): 
          
#         # Find the best fit block for 
#         # current process  
#         bestIdx = -1
#         for j in range(m): 
#             if blockSize[j] >= processSize[i]: 
#                 if bestIdx == -1:  
#                     bestIdx = j  
#                 elif blockSize[bestIdx] > blockSize[j]:  
#                     bestIdx = j 
  
#         # If we could find a block for  
#         # current process  
#         if bestIdx != -1: 
              
#             # allocate block j to p[i] process  
#             allocation[i] = bestIdx  
  
#             # Reduce available memory in this block.  
#             blockSize[bestIdx] -= processSize[i] 
  
#     print("Process No. Process Size     Block no.") 
#     for i in range(n): 
#         print(i + 1, "         ", processSize[i],end = "         ")  
#         if allocation[i] != -1:  
#             print(allocation[i] + 1)  
#         else: 
#             print("Not Allocated") 
  
# # Driver code  
# if __name__ == '__main__':  
#     blockSize = [100, 500, 200, 300, 600]  
#     processSize = [212, 417, 112, 426]  
#     m = len(blockSize)  
#     n = len(processSize)  
  
#     bestFit(blockSize, m, processSize, n)

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