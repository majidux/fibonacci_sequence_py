
# def Fibonacci2(n, memo = {}):
#     if n <= 2:
#         return 1
#     else:
#         return Fibonacci2(n-1)+Fibonacci2(n-2)
 
# print(Fibonacci2(123))


def Fibonacci(num, memo = {}):
    if num in memo: return memo[num]
    elif num <= 2:
        return 1
    else:
        memo[num] = Fibonacci(num - 1, memo) + Fibonacci(num - 2, memo)
    return memo[num]
 
print(Fibonacci(1))