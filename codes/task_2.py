def ToNumberSystem_x(n, x):
    num = ''
    while (n > 0):
        num = str(n % x) + num
        n //= x
    
    return num

def F(n):
    counter = 0
    for x in range(2, 9 + 1):
        n_x = ToNumberSystem_x(abs(n), x)

        if (n < 0):
            n_x += n_x[-1]
        else:
            n_x = str(x * int(n_x))

        if (int(n_x) % 5 == 0):
            counter += 1

    return counter

result = 0
for n in range(-99, 99 + 1):
    if n != 0:
        if (F(n) >= 5):
            result += 1
print(result)
