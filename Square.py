# To find square of numbers till the given end point

n = int(input())

for i in range(n):
    if i == n - 1:
        print(i * i, end="")
    else:
        print(i * i)