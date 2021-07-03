## Fibonacci sequence in python

#### Dynamic programming :=> memoization


![alt text][logo]

[logo]: https://raw.githubusercontent.com/majidux/fibonacci_sequence_py/main/algorithm.jpeg

#### Time complexity:

T(num in memo) = O(1)

T(n<=1) = O(1)

T(n) = T(n-1) + T(n-2) + O(1)

n = 1

T(n-1) = O(2n-1)

T(n) = T(n-1) + T(n-2) + O(1)

T(n) = O(2n-1) + O(2n-2) + O(1) = O(2n)
