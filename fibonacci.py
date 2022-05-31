def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n - 1) + fib(n - 2)


#print(fib(10))
longitud=int(input("Ingrese la longitud para la serie Fibonacci:"))
for n in range(longitud):
   print(fib(n))