import math
x=int(input("Enter the number whose sqrt has to be found:"))
print(math.sqrt(x))


x=int(input("Enter the length of the rectangle : "))
y=int(input("Enter the breadth of the rectangle : "))
perimeter=2*(x+y)
area=x*y
print(f"The perimeter is:{perimeter}")
print(f"The area is:{area}")


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
temp=a
a=b
b=temp

print(f"The new a after swap is:{a}")
print(f"The new a is:{b}")
#part 2
sum1=a+b
sum2=a-b
a=int((sum1-sum2)/2)
b=int((sum1+sum2)/2)
print(f"The new a after swap is:{a}")
print(f"The new a is:{b}")


x=["apple","oneplus","lenovo","hp","samsung"]
z=["mi","pastonji"]
y=("apple","oneplus","lenovo","hp","samsung")
x.append("dell")
print(x)
x=x+z
print(x)
x.pop()
print(x)
x.insert(2,"sony")
print(x)
z=("DELL",)#"sony")
a=y+z
#print(a)
#print(a.index("DELL"))
#y.add("DELL")
print(a)


a=int(input("Enter the number whose factorial has to be found : "))
#i=1
fact=1
for i in range(a+1):
    if i==0:
        pass
    else:
        fact=fact*i
print(f"The factorial is:{fact}")


n=int(input("Enter the number of elements in the Fibonacci Series:"))
a=0
b=1
c=0
print("The series is:")
print(f"{a}")
print(f"{b}")
for i in range(n-2):
    c=a+b
    print(f"{c}")
    a=b
    b=c



a=int(input("Enter the number whose factorial has to be found : "))
i=1
fact=1
while a!=0:
    fact=fact*a
    a=a-1
print(f"The factorial is:{fact}")


n=int(input("Enter the year to check if it is leap or no : "))
if n%400==0:
    print(f"{n} is a leap year")
elif n%100==0:
    print(f"{n} is not a leap year")
elif n%4==0:
    print(f"{n} is a leap year")
else:
    print(f"{n} is not a leap year")


n=int(input("Enter the marks:"))
if n>90 and n<=100:
    print("You have secured distinction")
elif n>70 and n<=90:
    print("Your score is respectable")
elif n>40 and n<=70:
    print("You need to improve")
else:
    print("Get out of the college")


n=int(input("Enter a number : "))
for i in range(n):
    if i==0:
        print("This is demonstration for pass statement")
        pass
    elif i==4:
        print("This is a demo for the continue statement")
        continue
    elif i==10:
        print("This was a long journey. Breaking the loop")
        break
    else:
        print(i)
