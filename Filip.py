def Rev(x):
    sumz = 0
    while x != 0:
        sumz = x % 10 + sumz * 10
        x = x // 10
    return sumz


num_1, num_2 = map(int, input().split())
if Rev(num_1) > Rev(num_2):
    print(Rev(num_1))
else:
    print(Rev(num_2))