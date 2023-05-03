from machine import Pin
import time

st = time.time()
led = Pin("LED", Pin.OUT)
led.value(0)
cuantos = 0

def matrix_multiplication(A,B):
    rows_a = len(A)
    cols_a = len(A[0])
    rows_b = len(B)
    cols_b = len(B[0])
    global cuantos
    result = [[0 for row in range(cols_b)] for col in range(rows_a)]
    for s in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[s][j] += A[s][k] * B[k][j]
                cuantos += 1
    return result

led.toggle()

A = [[1,3,5],[2,4,7]]
B = [[-5,8,11],[3,9,21],[4,0,8]]

for i in range(1,1400):
    R = matrix_multiplication(A,B)

et = time.time()
led.toggle()
print (cuantos)
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')