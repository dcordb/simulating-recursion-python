"""
Python generator recursion, tested at:

- https://codeforces.com/contest/1363/problem/E
- https://codeforces.com/gym/102483/problem/E
"""

from types import GeneratorType

mod = 10 ** 9 + 7

def f(n):
    if n == 1:
        yield 1

    else:
        res = yield f(n - 1)
        yield (n * res) % mod

dp = {}

def fib(n):
    if n in dp:
        yield dp[n]

    if n <= 2:
        dp[n] = 1

    else:
        x = yield fib(n - 1)
        y = yield fib(n - 2)

        dp[n] = (x + y) % mod

    yield dp[n]

def my_recursion(gen):
    stk = [gen]
    res = None
 
    while True:
        cur = stk[-1]
        obj = None
 
        if type(cur) is GeneratorType:
            try:
                obj = next(cur)
            except StopIteration: pass
 
        else:
            stk.pop()
 
            if not stk:
                res = cur
                break
            
            try:
                obj = stk[-1].send(cur)
            except StopIteration: pass
 
        if type(obj) is GeneratorType:
            stk.append(obj)
 
        else:
            stk[-1] = obj
 
    return res

print(my_recursion(fib(10**6)))
