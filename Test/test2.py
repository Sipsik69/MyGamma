# a=float(input('Side A:'))
# b=float(input('Side B:'))

a, b = input('Side A, B: ').split(', ')
c = (float(a)**2 + float(b)**2)**0.5


print(c)