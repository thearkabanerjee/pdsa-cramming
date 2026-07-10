a = int(input())
import time 
start = time.perf_counter()

primes = []
num = 2

while len(primes) < a:
    counter = 0

    for j in range(1, num + 1):
        if num % j == 0:
            counter += 1

    if counter == 2:
        primes.append(num)

    num += 1

print(primes)

end = time.perf_counter()

print (f"elapsed {end - start}")

print (end)
print (start)