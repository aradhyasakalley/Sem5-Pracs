x = 'mumbai'
print(type(x))

p = 786
print(type(p))

f = 12.3
print(type(f))

c = 2+4j
print(type(c))

l1 = [1, 'were', 76]
print(type(l1))

a = range(7)
for i in a:
    print(i)
print(type(a))

tp = ('qwert',)
print(type(tp))

Dict = dict()
Dict = {'Name': 'mumbai', 'Code':400104}
print(type(Dict))

set1 = set("the World is A beautiful pLace.")
print(set1)
print(type(set1))

print(type(True))
print(type(False))

n = None
print(n)
print(type(n)) 

b = bin(80)
print(b)
print(type(b))

j = 100
print(id(j))

print("***************")
#Operators in python
x = 10
print("Initial value: ",x)
x += 7
print("New value: ",x)
x -= 7
print("New value: ",x)
x *= 7

print("New value: ",x)
x /= 7
print("New value: ",x)
x %= 7
print("New value: ",x)
x //= 7
print("New value: ",x)
x **= 7
print("New value: ",x)
x = 2
x **= 7
print("New value: ",x)

x = 100
y = 5

#Arithmetic
opt = x+y
print(opt)

opt = x-y
print(opt)

opt = x*y
print(opt)

opt = x/y
print(opt)

opt = x**y
print(opt)

opt = x//y
print(opt)

opt = x%y
print(opt)

#Relational
t = 12
print(t)

t = y
print(t)

t+=3
print(t)

t-=3
print(t)

t*=3
print(t)

t/=2
print(t)

t%=2
print(t)

t**=2
print(t)

t//=2
print(t)

t=10
t &= 2
print(t)

t=10
t|=2
print(t)

t^=2
print(t)

t<<=2
print(t)

t>>=2
print(t)

#Comparison
print(t==y)
print(t!=x)
print(t>=x)
print(t<=x)

#Logical
print(x)
print(x > 50 and x < 112)
print(x > 3 or x < 4)
print(not(x > 50 and x < 112))

#Identity
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

print(x is not z)
print(x is not y)
print(x != y)

#Membership
print("banana" in x)
print("orange" not in x)

#Bitwise
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(3 << 2)
print(8 >> 2)
