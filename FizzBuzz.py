num_1, num_2, x = map(int, input().split())
for i in range(1 , x+1):
    if i % num_1 == 0  and i % num_2 == 0 :
        print("FizzBuzz")
    elif i%num_1==0:
        print("Fizz")
    elif i % num_2 == 0:
        print("Buzz")
    else:
        print(i)