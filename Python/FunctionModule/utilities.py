def factorial(x):
    answer = 1
    for i in range(1, x+1):
        answer *= i
    return answer


def summation(x, N):
    add = 0
    for i in range(1, N+1):
        add += i
    return add * x


if __name__ == "__main__":
    # The test of the factorial function
    print(factorial(3))
    # The test of the summation function
    print(summation(2, 5))
