###
n是被划分的整数，m是n的一个划分
f(n, m) =
    1                         (n = 1 or m = 1) 
    f(n, n)                   (n < m) 
    1 + f(n, m-1)             (n = m) 
    f(n-m, m) + f(n, m-1)    (n > m) 
###

console.log do (n = 100, m = 99) ->
    if n is 1 or m is 1
        1
    else if n < m
        arguments.callee n, n
    else if n is m
        1 + arguments.callee n, m - 1
    else
        arguments.callee(n - m, m) + arguments.callee(n, m - 1)