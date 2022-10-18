def sum(a, b):
    return a + b
print(sum(20, 30))

x = int(input())
def sum (a, b):
    return a + b 
c = sum(20, x)
print(c)


x = 20
b = 56
def sum(int1):
    global b
    b  = 30
    v = b + int1
    print(v)
c = sum(x)
print(b)


def func():
    print("Hello world!")
func()
func()
func()




name = input('Введите ваше имя:')
born = int(input('Введите год рождения:'))
def func(a, b):
    age = 2022 - b
    print(f"Привет {a}!\n, Тебе {age}!")
func(name, born)
