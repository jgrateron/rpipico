import math

multi = 0
def factorial(numero):
    if numero <= 0:
        return 1
    global multi
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        multi += 1
        numero -= 1
    return factorial

def elevado(n,i):
    z = 1
    global multi
    for k in range(1,i+1):
        multi += 1
        z = z * n
    return z

def calcular_pi(k):
    suma = 0
    global multi
    for n in range(1,k+1):
        multi += 1
        a1 = factorial(2*n)
        a2 = elevado(16,n)
        a3 = elevado(factorial(n),2)
        multi += 1
        b1 = a1 / (a2 * a3)
        multi += 1
        b2 = 1 / (2 * n + 1)
        multi += 1
        z = b1 * b2
        suma += z
    multi += 1
    pi = 3 * (1 + suma)
    return pi

for i in range(1,17):
    print(i, calcular_pi(i),"(",multi,")")
    multi = 0

print("  ",math.pi)

