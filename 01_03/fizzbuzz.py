numbers = list(range(0,101))
# print(numbers)

for i in range(1,101):
    if numbers[i] % 3 == 0 and numbers[i] % 5 ==0:
        numbers[i] = 'fizz,buzz'
    elif numbers[i] % 3 == 0:
        numbers[i] = 'fizz'
    elif numbers[i] % 5 ==0:
        numbers[i] = 'buzz'

print(numbers)