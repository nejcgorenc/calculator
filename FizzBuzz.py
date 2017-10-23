x = int(raw_input('Vnesi stevilo do katerega stejem')) + 1

for i in range(1, x):
    a = i % 3
    b = i % 5

    if a == 0 and b == 0:
        print 'FizzBuzz'
    elif a == 0:
        print 'Fizz'
    elif b == 0:
        print 'Buzz'
    else:
        print i