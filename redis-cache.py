import redis
from redis_lru import RedisLRU
import timeit

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


@cache
def fib_cache(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_cache(n - 1) + fib_cache(n - 2)


if __name__ == "__main__":
    print("Fibonacci 37 without cache: ", timeit.timeit(lambda: fib(37), number=1))
    print("Fibonacci 150 with cache: ", timeit.timeit(lambda: fib_cache(150), number=1))
