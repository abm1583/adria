k = int(input('сумма кредита: '))
p = int(input('процентная ставка: '))
m = int(input('количество месяцев:'))
a = k*0.01*p*(1+0.01*p)**m/((1+0.01*p)**m-1)

print(round(a , 2))
