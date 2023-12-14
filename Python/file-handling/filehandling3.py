fileRead = open("words.txt", "r")
List = list()
f = fileRead.read()
f = f.split()

for line in f:
 List.append(str(line)[::-1])
 List.sort(key=lambda item: (item, len(item)))
print("List of reversed words in order is:")
print(List)
fileWrite = open("reversed-words.txt", "w")
for i in range(len(List)):
 fileWrite.write(str(List[i]))
 fileWrite.write("\n")

    