from random import randint
break_loop = False
i = 0
x = randint(1, 20)
y = 10
while i < 5:
        print y
        z = 10 / 2 ** ( i + 1)
        i = i + 1
        if z == 0:
            z = 1
            break_loop = True
        if y == x:
            print 'uspeh'
            print x
            i = 5
        elif x < y:
            y = y - z
        else:
            y = y + z