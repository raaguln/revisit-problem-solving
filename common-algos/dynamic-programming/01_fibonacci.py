import time

# Top down - Naive
def naive_fib(n):
  if n <= 2:
    result = 1
  else:
    result = naive_fib(n-1) + naive_fib(n-2)
  return result

# Top down - DP
cache = {}
def memoized_fib(n):
  if n in cache:
    return cache[n]
  if n <= 2:
    result = 1
  else:
    result = memoized_fib(n-1) + memoized_fib(n-2)
  cache[n] = result
  return result

# Bottom up - DP
def memoized_fib2(n):
  if n <= 2:
    return 1
  a, b = 1, 1
  for i in range (3, n+1):
    temp = a + b
    a = b
    b = temp
  return b

start_time = time.time()
print(naive_fib(30))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(memoized_fib(30))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(memoized_fib2(30))
print("--- %s seconds ---" % (time.time() - start_time))