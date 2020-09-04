from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

mod = 10**9 + 7
dp = [ -1 for _ in range(10**6 + 1) ]

@bootstrap
def fib(n):
    if dp[n] != -1:
        yield dp[n]

    if n <= 2:
        dp[n] = 1

    else:
        x = yield fib(n - 1)
        y = yield fib(n - 2)

        dp[n] = (x + y) % mod

    yield dp[n]

print(fib(10**6))