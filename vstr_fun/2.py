num = int(input('chislo 1: '))
num2 = int(input('chislo 2: '))
num3 = int(input('chislo 3: '))
num4 = int(input('chislo 4: '))
num5 = int(input('chislo 5: '))
set = set()
set.add(num)
set.add(num2)
set.add(num3)
set.add(num4)
set.add(num5)
x = sorted(set)
b = slice(0, 1)
print('Samoe malenkoe chislo: ', x[b])
