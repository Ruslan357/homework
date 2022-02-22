#  Глава 1 Упражнение 1.3 (страница 28)

distance_km=10
time=43.5/60
distance_mile = distance_km/1.61
print('Средняя скорость = ', distance_mile/time, ' миль/час')



#  Глава 2 Упражнение 2.3 (страница 35)
width=17
height=12.0
delimiter='.'

print(width/2, type(width/2))
print(width/2.0, type(width/2.0))
print(height/3, type(height/3))
print(1+2*5, type(1+2*5))
print(delimiter*5,type(delimiter*5))

#  Глава 2 Упражнение 2.4  задача 1  (страница 35)
pi=3.1415926
R= 5 
print('Объем фиуры = ', 4/3*(pi*R**3))

#  Глава 2 Упражнение 2.4  задача 2  (страница 35)
price=24.95
discount=0.4
delivery_firs=3
delivery_after=0.75
number_of_books=60

total = number_of_books*((price*discount))-(delivery_after*(number_of_books-1)-delivery_firs)

print('Цена покупки 60 книг с доставкой = ', round(total,3), '$')


#  Глава 2 Упражнение 2.4  задача 3  (страница 35)
start=(6*60+52)/60
round1=(8*60+15)/60
round2=3*((7*60+12)/60)
round3=round1
time_of_run=round1+round2+round3

print('Я вернусь домой через',time_of_run,'минут')