# a=float(input('Side A:'))
# b=float(input('Side B:'))
# c=float(input('Side C:'))

a,b,c = input('Please enter 3 sides: ').split()
a=float(a)
b=float(b)
c=float(c)

print(a,b,c)

p = (a+b+c)/2

triang = (p*(p-a)*(p-b)*(p-c))**0.5
print(triang)