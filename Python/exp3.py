#tuple

tup = ('apple', 'banana', 'cherry', 24, 656, True, 'apple')
print(len(tup))
print(tup.index('apple'))
print(tup.count('apple'))

st = (2,5,9,3,88,14,4,1,10,111,6,8,7,-27)
aft = sorted(st)
print('Sorted tuple: ', aft) 
print(max(st))
print(min(st))
print(sum(st))


#set

myset = {1, 56, 99, 32, 'were', 'of', 'r', 'u' }
print(myset)
myset.add('save')
print(myset)
myset.discard('of')
myset.discard(6)
print(myset)
myset.pop()
print(myset)
#myset.remove(2)
myset.remove(1)
print(myset)
myset.clear()
print(myset)

#dictionary

dict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}
dicta = dict.copy()
print(dicta)
dict3 = (1,2,4)
print(dict.fromkeys(dict3,'as'))
print('Key 3 has value: ', dict.get(3))
dict.pop(2)
print(dict)
dict.clear()
print(dict)

#function

l = [11,54,22,54,90,11,2,6,33,11,54,9,54,7,101,65,33,87,54,56]

def histogram(l):

    count = 0
    for i in l:
        for j in range(0,len(l)):
            if i==l[j]:
                    count = count+1
        print(i,count)
        count = 0

histogram(l)

#perfect num

x = int(input('Enter a number: '))

fac = []
    
for i in range(1,x):
    if x%i==0 :
        fac.append(i)

sum = 0
for i in fac:
    sum = sum+i

if sum == x:
    print(x, 'is a perfect number')

#tower of hanoi

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
        
n = int(input('Enter number of disks: '))
TowerOfHanoi(n,'A','C','B')

#map function

# creating empty lists
list1 = []
list2 = []
# number of element in each list
n1 = int(input("Enter the number of elements in list 1: "))
print("Enter elements in list 1: ")
list1 = list(map(int, input().split()))[:n1]
print(list1)
n2 = int(input("Enter the number of elements in list 2: "))
print("Enter elements in list 2: ")
list2 = list(map(int, input().split()))[:n2]
print(list2)
result = list(map(lambda a, b: a + b, list1, list2))
print("The list of element-wise sum of the two lists is: ", str(result))

#map & filter

arr = []
n = int(input("Enter the number of elements in the array: "))
print("Enter elements in the array:")
arr = list(map(int, input().split()))[:n]
print(arr)
print("The list of cubes of odd numbers in the array is:")
arr2 = list(map(lambda x: x ** 3, filter(lambda x: x % 2 != 0, arr)))
print(arr2)
