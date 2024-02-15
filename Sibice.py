from math import sqrt


def maximum(num , x, y, sqrt_num):
    if num > x and num > y and num > sqrt_num:
        return "NE"
    else:
        return "DA"

n, x, y = map(int, input().split())
list_of_answers = []
sqrt_num = sqrt(x ** 2 + y ** 2)
for i in range(n):
    num = int(input())
    list_of_answers.append(maximum(num , x , y , sqrt_num))

for j in list_of_answers:
    print(j)

