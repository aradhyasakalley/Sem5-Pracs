fileRead = open("T1.txt","r")
List = list()
f = fileRead.read()
f = f.split()

for line in f:
    List.append(str(line))
    List.sort(key=lambda item:(item,len(item)))
print('the list of sorted words is:')
print(List)

fileWrite = open("T2.txt","w")
for i in range(len(List)):
    fileWrite.write(str(List[i]))
    fileWrite.write("\n")
    
