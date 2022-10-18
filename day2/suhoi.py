def fibonacci():
    a, b = 1, 1
    print(a,b)
    for i in range(10):
        a, b = b, a + b
        print(b)


gen = fibonacci()

print(gen)
