n = int(input())
arr = list(map(int, input().split()))

loa = len(arr)
max1 = 0
max2 = -101


def runner_up():

    for se in range(n):
        for oe in range(n):

            if arr[se] < arr[oe] > max1:
                max1 = arr[oe]

    for se in range(n):

        if max1 > arr[se] > max2:
            max2 = arr[se]

    return print(max2)


runner_up()
