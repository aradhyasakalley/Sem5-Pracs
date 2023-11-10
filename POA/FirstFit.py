def FirstFit(block_sizes,m,process_sizes,n):
    allocation = [-1]*n
    for i in range(n):
        for j in range(m):
            if process_sizes[i] <= process_sizes[j]:
                allocation[i] = j;
                block_sizes[j] = block_sizes[j] - process_sizes[i]
                break
    
    print("No.","       size","Allocated Memory",process_sizes[i])
    for i in range(n):
        print(" ",i+1,"        ",process_sizes[i],"      ", end="")
        if allocation[i] != -1:
            print(allocation[i]+1)
        else:
            print("Not allocated")

if __name__ == '__main__':
    block_sizes = [100,200,300,400,500]
    process_sizes = [81,123,213,332,431]
    m = len(block_sizes)
    n = len(process_sizes)
    FirstFit(block_sizes,m,process_sizes,n)