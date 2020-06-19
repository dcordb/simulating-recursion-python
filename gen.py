from collections.abc import Generator

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

        if isinstance(cur, Generator):
            obj = next(cur)

        else:
            stk.pop()

            if not stk:
                res = cur
                break

            obj = stk[-1].send(cur)

        if isinstance(obj, Generator):
            stk.append(obj)

        else:
            stk[-1] = obj

    return res

print(my_recursion(fib(1000)))
