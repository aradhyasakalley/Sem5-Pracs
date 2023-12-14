num = int(input('enter the number for factorial : '))
fact = 1

for i in range(num+1):
    if i == 0:
        pass
    else :
        fact = fact*i

print(f'factorial is {fact}')


num = int(input('enter the number for fibonnaci : '))


a = 0
b = 1
c = 0

print(f'{a}')
print(f'{b}')
for i in range(num-2):
    c = a+b
    print(f'{c}')
    a=b
    b=c

