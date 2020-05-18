import cProfile
n = int(input())    # число, до которого хотим найти простые числа
def sieve(n):
    numbers = list(range(2, 1000))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    a = list(filter(lambda x: x != 0, numbers))
    return a[n+1]
# def prime(n):
#     if n < 3:
#         return


print(sieve(n))