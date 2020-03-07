# nth Fibonacci number with bottom up approach, not recursive.

def fibonacci_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    arr = [None] * (n+1)
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]
