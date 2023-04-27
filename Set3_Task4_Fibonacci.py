def fibonacci(n1,n2):
    sum = n1 + n2
    return sum


n = int(input("Enter the length of fibonacci series:"))
fiblist = [0,1]
n1 = 0
n2 = 1
while n2 <= n:
    n1, n2 = n2, fibonacci(n1, n2)
    fiblist.append(n2)
print(f'The Fibonacci series for {n} : {" ".join(map(str, fiblist))}')