import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
names1 = []
names1.append(random.choices(names, k=4))
print(names1)

import os
print(os.name)


import datetime
dt = datetime.datetime.now()
thdt = datetime.timedelta(days=1000)
result = dt+thdt
print(result)


import random
a = ['камень', 'ножницы', 'бумага']
b = input("камень, ножницы, бумага")
if b == (random.choice(a)):
	print('ничья')
