import math

                           #Завдання тип даних int()
w=5
print(type(w))

a=5
b=3
print(a+b)

f=10
g=5
print(f-g)

c=9
d=3
print(c/d)

l=2
z=8
print(l*z)

j=15
k=6
print(j//k)

x=8
c=5
print(x%c)

l=9
z=3
print(l**z)

ab=5
ac=3
bc=6
print((ab *ac)/bc)

print(math.pi) #число Пи
print(math.e)  #число Эйлера 
print(math.exp(math.pi)) #экспонента от числа Пи
print(math.log(math.pi)) #логорифм от числа Пи
print(math.log10(math.pi)) #логорифм по основанию 10 от числа Пи
print(math.log(5, 10)) #  логарифм 5 по основанию 10
print(math.log1p(10)) #  логарифм(1+x) от 10




                           #Завдання тип даних float()
a = 10.00
print(type(a))

#b = 1.000.000 
#print(type(b)) # итератор воспринимает вторую точку как оператор и выдает ошибку синтаксиса

print(float(5) + int(10)) # происходит явное и далее неявное приведение типов данных во float

a=2.12348569 
print(round(a,3))

b=float('-905.4')
print(type(b)) # происходит явное приведение типа string во float




                           # Завдання.  тип даних str()
a = 'Hello World'
print(type(a))  