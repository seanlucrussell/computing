def memoize(func):
    memo = {}
    def wrapper(*args):
        if not args in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrapper

@memoize
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

@memoize
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

@memoize
def lcs(a,b):
    if len(a) == 0:
        return a
    if len(b) == 0:
        return b
    if a[-1] == b[-1]:
        return lcs(a[:-1],b[:-1]) + a[-1]
    return max(lcs(a,b[:-1]),lcs(a[:-1],b),key=len)
