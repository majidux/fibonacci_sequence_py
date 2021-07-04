def Fibonacci(num, memo = {}):
    if num in memo: return memo[num]
    elif num <= 2:
        return 1
    else:
        memo[num] = Fibonacci(num - 1, memo) + Fibonacci(num - 2, memo)
    return memo[num]