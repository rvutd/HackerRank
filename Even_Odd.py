# Even Odd

n = int(input().strip())


# n is odd:
# 1. n is from 6 to 20 and greater than 20.
# 2. Therefore print Weird.

if n % 2 != 0 or 6 <= n <= 20:
    print("Weird", end="\n")

# n is even:
# 1. n is from 2 to 5 and greater than 20.
# 2. Therefore print Not Weird.

if (n % 2 == 0) and (2 <= n <= 5 or n > 20):
    print("Not Weird", end="\n")



