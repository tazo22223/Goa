fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(2, 20)]
print(fib)
