import math

def factorial(numero):
    if numero <= 0:
        return 1
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial

def elevado(n,i):
    z = 1
    for k in range(1,i+1):
        z = z * n
    return z

def calcular_pi(k):
    suma = 0
    for n in range(1,k+1):
        a1 = factorial(2*n)
        a2 = elevado(16,n)
        a3 = elevado(factorial(n),2)
        b1 = a1 / (a2 * a3)
        b2 = 1 / (2 * n + 1)
        z = b1 * b2
        suma += z
    pi = 3 * (1 + suma)
    return pi

print(calcular_pi(10))

print(math.pi)

