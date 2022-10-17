import cProfile

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def factorial(n):
    if n == 1:
        return n
    else:
        return factorial(n -1) * n


def count(n):
    cnt = 0
    for _ in range(n):
        cnt += 1

    return cnt

def profilePermutations():
    cProfile.run("count(factorial(len(my_list)))")

profilePermutations()





