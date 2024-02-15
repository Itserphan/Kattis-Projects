nums = [int(input()) for x in range(10)]

def modulo(x):
    return x % 42


def modulo_2(y):
    while y < 42:
        y += y
    return y % 42


summed = set()
for x in range(len(nums)):
    if 0 <= nums[x] <= 41:
        summed.add(nums[x])
    elif nums[x] >= 42:
        summed.add(modulo(nums[x]))
print(len(summed))